# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:12:24 2022

@author: mkyng

"""


import csv
import matplotlib.pyplot as plt
#import matplotlib.tri as tri
import matplotlib as mpl
import seaborn as sns


z0_x=[]
z0_y=[]
z0_z=[]
z0_tag=[]
outcount=0
with open('prt5_params.txt', newline='') as csvfile:
    prt5reader = csv.reader(csvfile,delimiter=',')
    for row in prt5reader:
        #print(row)
        #print(len(row))
        if (float(row[2]) < 0.5) & (float(row[0]) >= 400): # row[0]=X, row[1]=y, row[2]=Z, row[3]=Time,row[4]=ID
            z0_x.append(float(row[0]))
            z0_y.append(float(row[1]))
            z0_z.append(float(row[2]))
            z0_tag.append(row[4])
        else:
            outcount=outcount+1

csvfile.close()

# with open('prt5_output_old.txt', newline='') as csvfile:
#     prt5reader = csv.reader(csvfile,delimiter=',')
#     for row in prt5reader:
#         if (float(row[2]) < 0.1) & (float(row[0]) > 400):
#             z0_x.append(float(row[0]))
#             z0_y.append(float(row[1]))


csvfile.close()


#plt.scatter(z0_x,z0_y)
#plt.hist2d(z0_x,z0_y,100)


#fig = plt.tricontourf(z0_x, z0_y, z0_z)

#fig = plt.hist2d(z0_x, z0_y, [100,200], norm=mpl.colors.LogNorm()) #[100,200]
plt.figure(dpi=1200)
fig=sns.kdeplot(x=z0_x,y=z0_y,thresh=0.001, cut=0, bw_adjust=0.75, fill=False, levels=10, cmap='copper',cbar=True) #levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.99,0.999]
#plt.Figure(dpi=1200)
plt.ylim(-200,200)
#plt.colorbar(fig[3])
