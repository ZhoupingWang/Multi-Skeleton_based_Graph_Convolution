import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

right_sam_filename = './work_dir/ntu/xsub/msg3d_joint_val/right-samples.txt'
#wrong_sam_filename = './work_dir/ntu/xsub/msg3d_joint_val/wrong-samples.txt'

categories = ['reading', 'writing', 'tear up paper', 'put on jacket', 'take off jacket', 'put on a shoe', 'take off a shoe', 'put on glasses', 'take off glasses', 'put on a hat/cap']
conf_mp = np.zeros([10,10])
f=open(right_sam_filename)
line = f.readline()
while len(line)>1:
    coor_gt = int(line[0])
    coor_pd = int(line[2])
    #print('%d,%d'%(coor_gt,coor_pd))
    conf_mp[coor_gt,coor_pd] = conf_mp[coor_gt,coor_pd]+1
    line = f.readline()
f.close()

label_gt = []
label_pd = []
label_acc = []
for k in range(10):
    class_num=0
    for l in range(10):
        class_num = class_num + conf_mp[k,l]
    for l in range(10):
        conf_mp[k,l] = conf_mp[k,l]/class_num
        label_gt.append(categories[k])
        label_pd.append(categories[l])
        label_acc.append(conf_mp[k,l])
conf_arr = {}
conf_arr["label_gt"] = label_gt
conf_arr["label_pd"] = label_pd
conf_arr["label_acc"] = label_acc
conf_arr_pd = pd.DataFrame(data=conf_arr)
conf_arr_mtx =conf_arr_pd.pivot("label_gt","label_pd","label_acc")

fig_dim = (12,12)
fig,ax = plt.subplots(figsize=fig_dim)
sns.heatmap(conf_arr_mtx,ax=ax,annot=True,fmt='.2%',cmap='Blues')
plt.show()
