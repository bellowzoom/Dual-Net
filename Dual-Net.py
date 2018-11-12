import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch
import torchvision
import torchvision.transforms as transforms
import torch.backends.cudnn as cudnn
from torch.utils.data import DataLoader
from torch.optim.lr_scheduler import ReduceLROnPlateau
import torch.optim as optim
from sklearn.metrics.ranking import roc_auc_score
from multi_model.multi_data import DatasetGenerator
from multi_model.Densenet121_sub import densenet121_sub
import numpy as np
from datetime import datetime
from sklearn import metrics
import matplotlib.pyplot as plt
from pylab import *


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.positive = densenet121_sub()
        self.side = densenet121_sub()
        self.fc_out = nn.Sequential(nn.Linear(2048, 16))

    def forward(self, x, y):
        x = self.positive(x)
        y = self.side(y)
        z = torch.cat([x, y], 1)
        # z = torch.add(x,y)
        z = F.sigmoid(self.fc_out(z))

        return z


pathDirData = '/home/huangxin/dataset/dul_16/'
pathFileTrain = '../dataset/dul_16_tr.txt'
pathFileTest = '../dataset/dul_16_ts_expand.txt'
binary_ts = '../dataset/dul_16_binary_ts.txt'
binary_tr = '../dataset/dul_16_binary_tr.txt'
dul_pth = '../pth_16/dul_concat.pth.tar'
temp_pth = '../pth_16/dul_binary.pth.tar'
test_pth = '../pth_16/dul_concat_best.pth.tar'
add_pth = '../pth_16/613_epoch_dul_add_100.pth.tar'


def train():
    transformList = []
    normalize = transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    transformList.append(transforms.Resize([256, 256]))
    transformList.append(transforms.RandomResizedCrop(224))
    # transformList.append(transforms.RandomHorizontalFlip())
    transformList.append(transforms.ToTensor())
    transformList.append(normalize)
    transformSequence = transforms.Compose(transformList)

    datasetTrain = DatasetGenerator(pathImageDirectory=pathDirData, pathDatasetFile=pathFileTrain,
                                    transform=transformSequence)
    dataLoaderTrain = DataLoader(dataset=datasetTrain, batch_size=32, shuffle=True, num_workers=32,
                                 pin_memory=True)
    loss = torch.nn.BCELoss(size_average=True)

    net = Net().cuda()
    net = torch.nn.DataParallel(net).cuda()
    modelCheckpoint = torch.load(temp_pth)
    net.load_state_dict(modelCheckpoint['state_dict'])
    # 冻结参数
    # for i,p in enumerate(net.parameters()):
    #     if i<724:
    #         p.requires_grad = False
    lr = 0.001

    # optimizer = optim.Adam(net.parameters(), lr, betas=(0.9, 0.999), eps=1e-08, weight_decay=1e-5)
    optimizer = optim.Adam(filter(lambda pa: pa.requires_grad, net.parameters()), lr, betas=(0.9, 0.999),
                           eps=1e-08, weight_decay=1e-5)

    for epoch in range(201):
        lossTrain = 0.0
        lossTrainNorm = 0
        round_time = datetime.now().strftime('%H:%M')
        print('——————————————————第' + str(epoch) + '轮/lr:' + str(lr) + '/' + round_time + '——————————————————')
        for batchID, (input_1, input_2, target) in enumerate(dataLoaderTrain):
            target = target.cuda(async=True)
            varTarget = torch.autograd.Variable(target)
            varOutput = net(Variable(input_1), Variable(input_2))
            lossvalue = loss(varOutput, varTarget)
            lossTrain += lossvalue.data[0]
            lossTrainNorm += 1
            optimizer.zero_grad()
            lossvalue.backward()
            optimizer.step()
        print(str(lossTrain / lossTrainNorm))

        torch.save({'state_dict': net.state_dict()}, '../pth_16/615_dul_concat_final_two_' + str(epoch) + '.pth.tar')
        if epoch < 50:
            lr = 0.001
        elif 50 < epoch < 100:
            lr = 0.0001
        elif epoch > 100:
            lr = 0.00001

        if (epoch % 10 == 0):
            torch.save({'state_dict': net.state_dict()}, '../pth_16/619_dul_binary_static_' + str(epoch) + '.pth.tar')


def test(test_pth):
    CLASS_NAMES = ['Opacity', 'Cardiomegaly', 'Pulmonary Atelectasis', 'Calcinosis', 'Lung/hypoinflation',
                   'Calcified Granuloma', 'Thoracic Vertebrae/degenerative', 'Lung/hyperdistention',
                   'Spine/degenerative', 'Aorta/tortuous', 'Pleural Effusion', 'Atherosclerosis',
                   'Airspace Disease', 'Granulomatous Disease', 'Nodule', 'Scoliosis']
    # CLASS_NAMES=['abnormal']
    cudnn.benchmark = True

    net = Net().cuda()
    net = torch.nn.DataParallel(net).cuda()

    modelCheckpoint = torch.load(test_pth)
    net.load_state_dict(modelCheckpoint['state_dict'])

    normalize = transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])

    transformList = []
    transformList.append(transforms.Resize([256, 256]))
    transformList.append(transforms.TenCrop([224, 224]))
    transformList.append(transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])))
    transformList.append(transforms.Lambda(lambda crops: torch.stack([normalize(crop) for crop in crops])))
    transformSequence = transforms.Compose(transformList)

    datasetTest = DatasetGenerator(pathImageDirectory=pathDirData, pathDatasetFile=pathFileTest,
                                   transform=transformSequence)
    dataLoaderTest = DataLoader(dataset=datasetTest, batch_size=32, num_workers=8, shuffle=False,
                                pin_memory=True)

    outGT = torch.FloatTensor().cuda()
    outPRED = torch.FloatTensor().cuda()

    for i, (input1, input2, target) in enumerate(dataLoaderTest):
        target = target.cuda()
        outGT = torch.cat((outGT, target), 0)
        bs, n_crops, c, h, w = input1.size()
        varInput1 = torch.autograd.Variable(input1.view(-1, c, h, w).cuda(), volatile=True)
        varInput2 = torch.autograd.Variable(input2.view(-1, c, h, w).cuda(), volatile=True)
        out = net(varInput1, varInput2)
        outMean = out.view(bs, n_crops, -1).mean(1)
        outPRED = torch.cat((outPRED, outMean.data), 0)

    plt_roc(outGT, outPRED)
    aurocIndividual = computeAUROC(outGT, outPRED, 16)
    aurocMean = np.array(aurocIndividual).mean()
    print('AUROC mean ', aurocMean)

    for i in range(0, len(aurocIndividual)):
        print(CLASS_NAMES[i], ' ', aurocIndividual[i])

    return


def computeAUROC(dataGT, dataPRED, classCount):
    outAUROC = []
    datanpGT = dataGT.cpu().numpy()
    datanpPRED = dataPRED.cpu().numpy()
    for i in range(classCount):
        outAUROC.append(roc_auc_score(datanpGT[:, i], datanpPRED[:, i]))

    return outAUROC


def plt_roc(dataGT, dataPRED):
    CLASS_NAMES = ['Opacity', 'Cardiomegaly', 'Pulmonary Atelectasis', 'Calcinosis', 'Lung/hypoinflation',
                   'Calcified Granuloma', 'Thoracic Vertebrae/degenerative', 'Lung/hyperdistention',
                   'Spine/degenerative', 'Aorta/tortuous', 'Pleural Effusion', 'Atherosclerosis',
                   'Airspace Disease', 'Granulomatous Disease', 'Nodule', 'Scoliosis']
    plt.switch_backend('agg')
    y = dataGT.cpu().numpy()
    ##设置pred值：表示预测后的值
    pred = dataPRED.cpu().numpy()
    ##设置y值：表示实际值

    np.savetxt('concat.txt', y)
    np.savetxt('concat_pred.txt', pred)
    # for i in range(16):
    #     plt.clf()
    #     fpr, tpr, thresholds = metrics.roc_curve(y[:, i], pred[:, i], pos_label=1)
    #
    #     plt.xlim([0.0, 1.0])
    #     plt.ylim([0.0, 1.0])
    #     # 绘图
    #     plt.xlabel(CLASS_NAMES[i], fontsize=18)
    #     # plt.legend(loc="lower right")
    #     plt.plot(fpr, tpr)
    #     plt.plot([0, 1], [0, 1], 'k--')
    #     plt.show()
    #     plt.savefig('./ROC/'+CLASS_NAMES[i].replace('/',' ')+'.png')
    # print('okay~!')


test(test_pth)
# train()







