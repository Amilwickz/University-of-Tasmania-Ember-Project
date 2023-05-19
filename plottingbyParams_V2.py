import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from PIL import Image

text_file = 'prt5_params.txt'
csv_file = 'plotdata.csv'

# Path to the image on the working folder
image_path = "C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V2/CanRiver_photo.png"

# Read the image using PIL
image = Image.open(image_path)

# Define the desired size of the image
desired_size = (5200, 1600)

# Resize the image
resized_image = image.resize(desired_size)

with open(text_file, 'r') as file:
   rows = file.readlines()

with open(csv_file, 'w', newline='') as file:
   writer = csv.writer(file)
   for row in rows:
       values = row.strip().split(',')
       writer.writerow(values)

x_values = []
y_values = []

with open(csv_file, 'r') as file:
   reader = csv.reader(file)
   for row in reader:
       x_values.append(float(row[0]))
       y_values.append(float(row[1]))

df = pd.read_csv(csv_file, header=None)
x1_values = df.iloc[:, 0]
y1_values = df.iloc[:, 1]

# Create a figure and subplots
fig, axs = plt.subplots(3, 2, figsize=(10, 10))

# Create a scatter plot
axs[0, 0].scatter(x_values, y_values, s=5, c='r', marker='o', cmap=None)
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('Y')
axs[0, 0].set_xlim(325, 700)
axs[0, 0].set_ylim(0, 210)

# Display the resized image on the subplot
axs[2, 1].imshow(resized_image)
axs[2, 1].axis('off')
axs[2, 1].set_xlim(0, 700)
axs[2, 1].set_ylim(0, 210)
axs[2, 1].set_xticks([])
axs[2, 1].set_yticks([])

plt.tight_layout()
plt.show()

