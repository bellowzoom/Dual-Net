import os
import shutil

originalroot='/home/huangxin/openi/original/'
healthroot='/home/huangxin/openi/health/'
# doubleroot='/home/huangxin/openi/double/'

# with open('./dataset/tag_new.txt','r') as ft:
#     f_data=ft.read().split('\n')

# for line in f_data:
#     dir=line.split()[0].split('|')[0]
#     img='CXR'+dir.split('/')[-1]
#     label=line.split()[1]
#     old_dir=originalroot+img
#     new_dir=doubleroot+img
#     if os.path.exists(old_dir):
#         shutil.copyfile(old_dir, new_dir)
#     else:
#         print(line)
#

# side_tree=os.walk('/home/huangxin/openi/side')
# positive_tree=os.walk('/home/huangxin/openi/positive')
#
# side_list=[]
# positive_list=[]
#
# for root,dirs,files in side_tree:
#     for name in files:
#         side_img=os.path.join(root,name)
#         # print(name[3:])
#         side_list.append(name[3:])
#
# for root,dirs,files in positive_tree:
#     for name in files:
#         side_img=os.path.join(root,name)
#         # print(name[3:])
#         positive_list.append(name[3:])
#
#
# for s in side_list:
#     for f in f_data:
#         if s in f:
#             sname='CXR'+s
#             fl=f.split(' ')[-1]
#             print(sname+' '+fl)
#
#
# print('~~~~')
# p_list=[]
#
# for p in positive_list:
#     for s in side_list:
#         ps = '-'.join(s.split('-')[:-1])
#         if ps in p:
#             p_list.append(p)
#
# print(len(p_list))
# print(len(positive_list))
#
# for p1 in p_list:
#     for f1 in f_data:
#         if p1 in f1:
#             l1=f1.split()[-1]
#             print('CXR'+p1+' '+l1)


# with open('./dataset/side.txt','r') as fs:
#     f_side=fs.read().split('\n')
#
# with open('./dataset/positive.txt','r') as fp:
#     f_positive=fp.read().split('\n')
#
# with open('./dataset/sick_double.txt','w') as fd:
#     for s in f_side:
#         s1='-'.join(s.split()[0].split('-')[:-1])
#         for p in f_positive:
#             p1 = '-'.join(p.split()[0].split('-')[:-1])
#             if s1 == p1:
#                 print(p.split()[0]+' '+s.split()[0]+' '+p.split()[1])


# with open('./dataset/my_list.txt','r') as fs:
#     myl=fs.read().split('\n')
#
# h_list=[]
# for m in myl:
#     l=m.split()[1]
#     if l == '0':
#         # img='CXR'+m.split()[0]
#         # img_old=os.path.join(originalroot,img)
#         # img_new=os.path.join(healthroot,img)
#         # if os.path.exists(img_old):
#         #     shutil.copyfile(img_old,img_new)
#         # else:
#         #     print('l')
#         h_list.append(l)



# side_tree=os.walk('/home/huangxin/openi/health_side')
# positive_tree=os.walk('/home/huangxin/openi/health_positive')
#
# side_list=[]
# positive_list=[]
#
# for root,dirs,files in side_tree:
#     for name in files:
#         side_img=os.path.join(root,name)
#         # print(name[3:])
#         side_list.append(name[3:])
#
# for root,dirs,files in positive_tree:
#     for name in files:
#         side_img=os.path.join(root,name)
#         # print(name[3:])
#         positive_list.append(name[3:])

# pp_list=[]
# for s in positive_list:
#     pp = '-'.join(s.split('-')[:-1])
#     pp_list.append(pp)
# pp_set=set(pp_list)
# for se in pp_set:
#     if pp_list.count(se)>1:
#         print(se, pp_list.count(se))


#
# print('~~~~')
# p_list=[]
# s_list=[]
# h_lable='0 0 0 0 0 0 0 0 0 0 0 0 0 0'
# for p in positive_list:
#     for s in side_list:
#         ps = '-'.join(s.split('-')[:-1])
#         if ps in p:
#             print(p+ ' '+s+' '+h_lable)
#
#             p_list.append(p)
#             s_list.append(s)

# for s in side_list:
#     for p in positive_list:
#         ps = '-'.join(p.split('-')[:-1])
#         if ps in s:
#             print(s)
#             p_list.append(s)

#
# print(len(positive_list))
# print(len(side_list))
# print(len(p_list))
# print(len(s_list))




# with open('./dataset/sick_double.txt','r') as fs:
#     sd_list=fs.read().split('\n')
#
#
# with open('./dataset/sick_test.txt','r') as fs:
#     st_list=fs.read().split('\n')
#
# temp_list=[]
# for sd in st_list:
#     if sd!='':
#         temp_list.append(sd)
#
# for sd in sd_list:
#     if sd not in temp_list:
#         print(sd)


# with open('./dataset/sick_train.txt','r') as fs:
#     str_list=fs.read().split('\n')
#
# n1_list=[]
# n2_list=[]
# n3_list=[]
# n4_list=[]
# n5_list=[]
# n6_list=[]
# n7_list=[]
# n8_list=[]
# n9_list=[]
# n10_list=[]
# n11_list=[]
# n12_list=[]
# n13_list=[]
# n14_list=[]
# n15_list=[]
#
#
# for sd in str_list:
#     if '1 0 0 0 0 0 0 0 0 0 0 0 0 0' in sd:
#         n1_list.append(sd)
#     elif '0 1 0 0 0 0 0 0 0 0 0 0 0 0' in sd:
#         n2_list.append(sd)
#     elif '0 0 1 0 0 0 0 0 0 0 0 0 0 0' in sd:
#         n3_list.append(sd)
#     elif '0 0 0 1 0 0 0 0 0 0 0 0 0 0' in sd:
#         n4_list.append(sd)
#     elif '0 0 0 0 1 0 0 0 0 0 0 0 0 0' in sd:
#         n5_list.append(sd)
#     elif '0 0 0 0 0 1 0 0 0 0 0 0 0 0' in sd:
#         n6_list.append(sd)
#     elif '0 0 0 0 0 0 1 0 0 0 0 0 0 0' in sd:
#         n7_list.append(sd)
#     elif '0 0 0 0 0 0 0 1 0 0 0 0 0 0' in sd:
#         n8_list.append(sd)
#     elif '0 0 0 0 0 0 0 0 1 0 0 0 0 0' in sd:
#         n9_list.append(sd)
#     elif '0 0 0 0 0 0 0 0 0 1 0 0 0 0' in sd:
#         n10_list.append(sd)
#     elif '0 0 0 0 0 0 0 0 0 0 1 0 0 0' in sd:
#         n11_list.append(sd)
#     elif '0 0 0 0 0 0 0 0 0 0 0 1 0 0' in sd:
#         n12_list.append(sd)
#     elif '0 0 0 0 0 0 0 0 0 0 0 0 1 0' in sd:
#         n13_list.append(sd)
#     elif '0 0 0 0 0 0 0 0 0 0 0 0 0 1' in sd:
#         n14_list.append(sd)
#     else:
#         n15_list.append(sd)
#
# for ii in n15_list:
#     print(ii)
#
# print(len(n15_list))

import random

# with open('./dataset/openi_train.txt','r') as fs:
#     str_list=fs.read().split('\n')
#
#
# for si in str_list:
#     if len(si.split())!=16:
#         print(si)

def openi_12():

    d12_list=['normal','Opacity','Cardiomegaly','Pulmonary Atelectasis','Calcinosis','Lung/hypoinflation',
              'Calcified Granuloma ','Thoracic Vertebrae/degenerative','Lung/hyperdistention','Spine/degenerative',
              'Aorta/tortuous','Pleural Effusion','Atherosclerosis','Airspace Disease','Granulomatous Disease',
              'Nodule','Scoliosis']
    temp_list=[]
    with open('./stat/openi.mesh.top','r') as fs:
        mesh_list=fs.read().split('\n')
    for ds in d12_list:
        for line in mesh_list:
            if ds  in line:
                temp_list.append(line)
                # line_list=line.split('|')
    for new_line in set(temp_list):
        print(new_line)
    print(len(temp_list))
    print(len(set(temp_list)))

import math
def diseases_14_train_test():
    train_list=[]
    test_list=[]
    with open('./stat/diseases_14plus/Mass.txt','r') as f_mass:
        mass_list=f_mass.read().split('\n')[:-1]
        mass_list=list(set(mass_list))
        train_index=math.ceil(len(mass_list)*0.85)
        for tr in mass_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in mass_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)

    with open('./stat/diseases_14plus/Pneumothorax.txt','r') as f_Pneumothorax:
        Pneumothorax_list=f_Pneumothorax.read().split('\n')[:-1]
        Pneumothorax_list = list(set(Pneumothorax_list))
        train_index=math.ceil(len(Pneumothorax_list)*0.85)
        for tr in Pneumothorax_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Pneumothorax_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)


    with open('./stat/diseases_14plus/Fibrosis.txt','r') as f_Fibrosis:
        Fibrosis_list=f_Fibrosis.read().split('\n')[:-1]
        Fibrosis_list = list(set(Fibrosis_list))
        train_index=math.ceil(len(Fibrosis_list)*0.85)
        for tr in Fibrosis_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Fibrosis_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)


    with open('./stat/diseases_14plus/Pneumonia.txt','r') as f_Pneumonia:
        Pneumonia_list=f_Pneumonia.read().split('\n')[:-1]
        Pneumonia_list = list(set(Pneumonia_list))
        train_index=math.ceil(len(Pneumonia_list)*0.85)
        for tr in Pneumonia_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Pneumonia_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)


    with open('./stat/diseases_14plus/Hernia.txt', 'r') as f_Hernia:
        Hernia_list = f_Hernia.read().split('\n')[:-1]
        Hernia_list = list(set(Hernia_list))
        train_index = math.ceil(len(Hernia_list) * 0.85)
        for tr in Hernia_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Hernia_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    with open('./stat/diseases_14plus/Consolidation.txt', 'r') as f_Consolidation:
        Consolidation_list = f_Consolidation.read().split('\n')[:-1]
        Consolidation_list = list(set(Consolidation_list))
        train_index = math.ceil(len(Consolidation_list) * 0.85)
        for tr in Consolidation_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Consolidation_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    with open('./stat/diseases_14plus/Edema.txt', 'r') as f_Edema:
        Edema_list = f_Edema.read().split('\n')[:-1]
        Edema_list = list(set(Edema_list))
        train_index = math.ceil(len(Edema_list) * 0.85)
        for tr in Edema_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Edema_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    with open('./stat/diseases_14plus/Pleural_Thickening.txt', 'r') as f_Pleural_Thickening:
        Pleural_Thickening_list = f_Pleural_Thickening.read().split('\n')[:-1]
        Pleural_Thickening_list = list(set(Pleural_Thickening_list))
        train_index = math.ceil(len(Pleural_Thickening_list) * 0.85)
        for tr in Pleural_Thickening_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Pleural_Thickening_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)

    with open('./stat/diseases_14plus/Infiltration.txt', 'r') as f_Infiltration:
        Infiltration_list = f_Infiltration.read().split('\n')[:-1]
        Infiltration_list = list(set(Infiltration_list))
        train_index = math.ceil(len(Infiltration_list) * 0.85)
        for tr in Infiltration_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Infiltration_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    with open('./stat/diseases_14plus/Nodule.txt', 'r') as f_Nodule:
        Nodule_list = f_Nodule.read().split('\n')[:-1]
        Nodule_list = list(set(Nodule_list))
        train_index = math.ceil(len(Nodule_list) * 0.85)
        for tr in Nodule_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Nodule_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    with open('./stat/diseases_14plus/Effusion.txt', 'r') as f_Effusion:
        Effusion_list = f_Effusion.read().split('\n')[:-1]
        Effusion_list = list(set(Effusion_list))
        train_index = math.ceil(len(Effusion_list) * 0.85)
        for tr in Effusion_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Effusion_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    with open('./stat/diseases_14plus/Emphysema.txt', 'r') as f_Emphysema:
        Emphysema_list = f_Emphysema.read().split('\n')[:-1]
        Emphysema_list = list(set(Emphysema_list))
        train_index = math.ceil(len(Emphysema_list) * 0.85)
        for tr in Emphysema_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Emphysema_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    with open('./stat/diseases_14plus/Cardiomegaly.txt', 'r') as f_Cardiomegaly:
        Cardiomegaly_list = f_Cardiomegaly.read().split('\n')[:-1]
        Cardiomegaly_list = list(set(Cardiomegaly_list))
        train_index = math.ceil(len(Cardiomegaly_list) * 0.85)
        for tr in Cardiomegaly_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Cardiomegaly_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    with open('./stat/diseases_14plus/Atelectasis.txt', 'r') as f_Atelectasis:
        Atelectasis_list = f_Atelectasis.read().split('\n')[:-1]
        Atelectasis_list = list(set(Atelectasis_list))
        train_index = math.ceil(len(Atelectasis_list) * 0.85)
        for tr in Atelectasis_list[:train_index]:
            if tr not in train_list:
                if tr not in test_list:
                    train_list.append(tr)
        for tr in Atelectasis_list[train_index:]:
            if tr not in test_list:
                if tr not in train_list:
                    test_list.append(tr)
    return train_list,test_list

#
# with open('./stat/tag_16_diseases.txt', 'r') as f_plus:
#     f_list = f_plus.read().split('\n')[:-1]

# with open('./dataset/diseases_14_plus.txt', 'r') as f_plus:
#     f_list = f_plus.read().split('\n')[:-1]
# #
# img_list=[]
#
# for l in f_list:
#     img=l.split()[0].split('-')[:-1]
#     img='-'.join(img)
#     img_list.append(img)
#
# print(len(img_list))
# img_list_1=[]
#
# pp_set=set(img_list)
# for se in pp_set:
#     if img_list.count(se)==1:
#         img_list_1.append(se)
#         # print(se, img_list.count(se))
#
# print(len(img_list_1))
#
# for c1 in img_list_1:
#     if c1 in img_list:
#         img_list.remove(c1)
#
# print(len(img_list))
#
# for se in pp_set:
#     if img_list.count(se)>2:
#         img_list_1.append(se)
#         print(se, img_list.count(se))

#三张正面无侧面
# 'CXR2280_IM-0867-1001'
# 'CXR1976_IM-0635-1001'


# side_tree=os.walk('/home/huangxin/14plus/14plus_s')
# positive_tree=os.walk('/home/huangxin/14plus/14plus_p')
#
# side_list=[]
# positive_list=[]
#
# for root,dirs,files in side_tree:
#     for name in files:
#         # side_img=os.path.join(root,name)
#         # print(name)
#         side_list.append(name)
#
# for root,dirs,files in positive_tree:
#     for name in files:
#         # side_img=os.path.join(root,name)
#         # print(name)
#         positive_list.append(name)
#
# print(len(positive_list))
# print(len(side_list))
# dul_list=[]
# for p in positive_list:
#     p1='-'.join(p.split()[0].split('-')[:-1])
#     for s in side_list:
#         s1 = '-'.join(s.split()[0].split('-')[:-1])
#         if s1 == p1:
#             dul_list.append(p+' '+s)
# print(len(dul_list))
#
# dul_lable=[]
# for du in dul_list:
#     for line in f_list:
#         if du.split()[0] in line:
#             label=line.split()[1:]
#             label=' '.join(label)
#             print(du+' '+label)
#             dul_lable.append(du+' '+label)
# print(len(dul_lable))
#
# CLASS_NAMES = ['Atelectasis', 'Cardiomegaly', 'Effusion', 'Infiltration', 'Mass', 'Nodule', 'Pneumonia',
#                    'Pneumothorax', 'Consolidation', 'Edema', 'Emphysema', 'Fibrosis', 'Pleural_Thickening', 'Hernia']
#
# with open('./dataset/sick_double.txt', 'r') as f_plus:
#     f_list = f_plus.read().split('\n')
#
# Atelectasis,Cardiomegaly,Effusion=[],[],[]
# Infiltration,Mass,Nodule,Pneumonia=[],[],[],[]
# Pneumothorax,Consolidation,Edema=[],[],[]
# Emphysema,Fibrosis,Pleural_Thickening,Hernia=[],[],[],[]
# for du in f_list:
#     label=du.split()[2:]
#     if int(label[0])==1:
#         Atelectasis.append(du)
#     if int(label[1])==1:
#         Cardiomegaly.append(du)
#     if int(label[2])==1:
#         Effusion.append(du)
#     if int(label[3])==1:
#         Infiltration.append(du)
#     if int(label[4])==1:
#         Mass.append(du)
#     if int(label[5])==1:
#         Nodule.append(du)
#     if int(label[6])==1:
#         Pneumonia.append(du)
#     if int(label[7])==1:
#         Pneumothorax.append(du)
#     if int(label[8])==1:
#         Consolidation.append(du)
#     if int(label[9])==1:
#         Edema.append(du)
#     if int(label[10])==1:
#         Emphysema.append(du)
#     if int(label[11])==1:
#         Fibrosis.append(du)
#     if int(label[12])==1:
#         Pleural_Thickening.append(du)
#     if int(label[13])==1:
#         Hernia.append(du)
#
#
#
# print('Atelectasis: '+str(len(Atelectasis)))
# print('Cardiomegaly: '+str(len(Cardiomegaly)))
# print('Effusion: '+str(len(Effusion)))
# print(len(Infiltration))
# print(len(Mass))
# print(len(Nodule))
# print(len(Pneumonia))
# print(len(Pneumothorax))
# print(len(Consolidation))
# print(len(Edema))
# print(len(Emphysema))
# print(len(Fibrosis))
# print(len(Pleural_Thickening))
# print(len(Hernia))
#
# print('-------')
#
# train_list=[]
# test_list=[]
#
# train_index=math.ceil(len(Mass)*0.6)
# for tr in Mass[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Mass[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Fibrosis) * 0.6)
# for tr in Fibrosis[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Fibrosis[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Pneumothorax) * 0.6)
# for tr in Pneumothorax[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Pneumothorax[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Consolidation) * 0.6)
# for tr in Consolidation[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Consolidation[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Pneumonia) * 0.6)
# for tr in Pneumonia[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Pneumonia[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Hernia) * 0.6)
# for tr in Hernia[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Hernia[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Pleural_Thickening) * 0.5)
# for tr in Pleural_Thickening[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Pleural_Thickening[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Edema) * 0.85)
# for tr in Edema[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Edema[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Infiltration) * 0.85)
# for tr in Infiltration[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Infiltration[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
#
# train_index = math.ceil(len(Nodule) * 0.85)
# for tr in Nodule[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Nodule[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Effusion) * 0.6)
# for tr in Effusion[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Effusion[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Emphysema) * 0.8)
# for tr in Emphysema[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Emphysema[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Cardiomegaly) * 0.9)
# for tr in Cardiomegaly[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Cardiomegaly[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# train_index = math.ceil(len(Atelectasis) * 0.9)
# for tr in Atelectasis[:train_index]:
#     if tr not in train_list:
#         if tr not in test_list:
#             train_list.append(tr)
# for tr in Atelectasis[train_index:]:
#     if tr not in test_list:
#         if tr not in train_list:
#             test_list.append(tr)
#
# print(len(train_list))
# print(len(test_list))
#
# for te in test_list:
#     print(te)
def sort16():
    with open('./dataset/dul_16_disease.txt','r') as fd:
        dul16=fd.read().split('\n')
    for i in range(16):
        for n,dul in enumerate(dul16):
            label=dul.split()[2:]
            if label[i]=='1':
                print(dul)
                dul16.remove(dul16[n])

    print('------------')
    for d in dul16:
        print(d)
    # print(dul16)




def single16():
    with open('./dataset/dul_16_tr.txt','r') as fd:
        dul16_tr=fd.read().split('\n')

    with open('./dataset/dul_16_ts_expand.txt','r') as fd:
        dul16_ts=fd.read().split('\n')

    for tr in dul16_ts:
        p=tr.split()[0]
        s = tr.split()[1]
        l = ' '.join(tr.split()[2:])
        print(p+' '+l)
        print(s + ' ' + l)


with open('./dataset/dul_16_ts_expand.txt', 'r') as fd:
    dul16_tr = fd.read().split('\n')
    for tr in dul16_tr:
        img=tr.split()[0]
        new_img=img.split('/')[-1]
        other = ' '.join(tr.split()[1:])
        print(new_img+' '+other)