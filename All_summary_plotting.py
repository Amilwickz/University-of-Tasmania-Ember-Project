import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from PIL import Image

file_paths = ["C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/plotdata_Ember_1.csv",
              "C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/plotdata_Ember_2.csv",
              "C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/plotdata_Ember_3.csv"]

data_frames =[]
for file_path in file_paths:
    df = pd.read_csv(file_path)
    data_frames.append(df.iloc[:, :2]) # select the first two columns

#concatanate the data frames along the columns axis (axis =1)
all_data = pd.concat(data_frames, axis =1)

#Define the column names for the resulting data frames
column_names = ['Column 1', 'Column 2', 'Column 4', 'Column 5', 'Column 7', 'Column 8']

#Rename the columns in the all_data data frames
all_data.columns = column_names

print(all_data)


#Ember 1: X, Y landing location data
x1_values = all_data.iloc[1:,0]
y1_values = all_data.iloc[1:,1]

##Ember 2: X, Y landing location data
x2_values = all_data.iloc[1:,2]
y2_values = all_data.iloc[1:,3]

#Ember 3: X, Y landing location data
x3_values = all_data.iloc[1:,4]
y3_values = all_data.iloc[1:,5]


#write the combined data frame to a new csv filenamed 'All.csv'
all_data.to_csv('All.csv', index=False)

#image plotting info
#Path to the image on the working folder
image_path ="C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/CanRiver_photo.png"

#Read the image using PIL
image =Image.open(image_path)


#define the desired size of the image
desired_size = (5200, 1600)

#resize the image
resized_image = image.resize(desired_size)



#create a scatter subplot at (3, 2, 1) location
plt.subplot(3,2,1)
plt.scatter(all_data['Column 1'], all_data['Column 2'],s=4, c='blue', marker='o', cmap=None)
plt.scatter(all_data['Column 4'], all_data['Column 5'],s=4, c='red', marker='o', cmap=None)
plt.scatter(all_data['Column 7'], all_data['Column 8'],s=4, c='green', marker='o', cmap=None)
plt.xlabel('X')
plt.ylabel('Y')
# set axes range
plt.xlim(325, 700)
plt.ylim(0, 210)
plt.legend(['cylinder', 'sphere', 'cube'], fontsize ='small')


#Plot with colour filled contours
plt.subplot(3, 2, 2)
sns.kdeplot(data=df, x=x1_values, y=y1_values, cmap="Blues", fill=True, bw_adjust=.75, cbar=False)
sns.kdeplot(data=df, x=x2_values, y=y2_values, cmap="Reds", fill=True, bw_adjust=.75, cbar=False)
sns.kdeplot(data=df, x=x3_values, y=y3_values, cmap="Greens", fill=True, bw_adjust=.75, cbar=False)
sns.set_style('whitegrid')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(325, 700)
plt.ylim(0, 210)
#plt.legend(['cylinder', 'sphere', 'cube'], fontsize ='small')
plt.title('Ember distribution')

#Probability density of X direction
plt.subplot(3, 2, 3)
sns.kdeplot(all_data['Column 1'], c='blue')
sns.kdeplot(all_data['Column 4'], c='red')
sns.kdeplot(all_data['Column 7'], c='green')
plt.xlabel('X')
plt.ylabel('Probability')
plt.xlim(325, 700)
#plt.title('Probability density')
plt.legend(['cylinder', 'sphere', 'cube'], fontsize ='small')


#plot with line contours
plt.subplot(3, 2, 4)
sns.kdeplot(data=df, x=x1_values, y=y1_values, color='blue')
sns.kdeplot(data=df, x=x2_values, y=y2_values, color='red' )
sns.kdeplot(data=df, x=x3_values, y=y3_values, color='green')
sns.set_style('whitegrid')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(325, 700)
plt.ylim(0, 210)
#plt.legend(['cylinder', 'sphere', 'cube'], fontsize ='small')


#Probability density of Y direction
plt.subplot(3, 2, 5)
sns.kdeplot(all_data['Column 2'], c='blue')
sns.kdeplot(all_data['Column 5'], c='red')
sns.kdeplot(all_data['Column 8'], c='green')
plt.xlabel('Y')
plt.ylabel('Probability')
plt.xlim(-10, 220)
#plt.title('Probability density')
plt.legend(['cylinder', 'sphere', 'cube'], fontsize ='small')


#Display the Cann River area image on the subplot
plt.subplot(3, 2, 6)
plt.imshow(resized_image, extent =[0, 700, 0, 210])
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,700)
plt.ylim(0,210)


#saving and displaying the final
plt.savefig('All_plot_summary.png')
plt.show()