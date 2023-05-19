import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from PIL import Image

text_file = 'prt5_params_All.txt'
csv_file = 'plotdata_All.csv'

#Path to the image on the working folder
image_path ="C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/CanRiver_photo.png"

#Read the image using PIL
image =Image.open(image_path)


#define the desired size of the image
desired_size = (5200, 1600)

#resize the image
resized_image = image.resize(desired_size)

with open(text_file, 'r') as file:
    rows = file.readlines()

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        values = row.strip().split(',')
        writer.writerow(values)

x_values =[]
y_values =[]

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x_values.append(float(row[0]))
        y_values.append(float(row[1]))

df = pd.read_csv(csv_file, header=None)
x1_values = df.iloc[:,0]
y1_values = df.iloc[:,1]




#create a scatter plot
plt.subplot(3, 2, 1)
plt.scatter(x_values, y_values, s=5, c='r', marker='o', cmap=None)
plt.xlabel('X')
plt.ylabel('Y')
# set axes range
plt.xlim(325, 700)
plt.ylim(0, 210)


plt.subplot(3, 2, 2)
sns.kdeplot(x_values, c='b')
plt.xlabel('X')
plt.ylabel('Probability')
plt.xlim(325, 700)

plt.subplot(3, 2, 3)
sns.kdeplot(y_values, c='g')
plt.xlabel('Y')
plt.ylabel('Probability')
plt.xlim(-10, 220)

plt.subplot(3, 2, 4)
sns.kdeplot(data=df, x=x1_values, y=y1_values, cmap="Reds", fill=True, bw_adjust=.75, cbar=True)
sns.set_style('whitegrid')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(325, 700)
plt.ylim(0, 210)


#Display the Cann River area image on the subplot
plt.subplot(3, 2, 5)
plt.imshow(resized_image)
plt.axis('on')
#plt.xlim(0, 700)
#plt.ylim(0, 210)
#plt.xticks(np.arange(0, 701, 100))
#plt.yticks(np.arange(0, 211, 50))



plt.subplot(3, 2, 6)
sns.kdeplot(data=df, x=x1_values, y=y1_values)
sns.set_style('whitegrid')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(325, 700)
plt.ylim(0, 210)

plt.tight_layout()
plt.show()

