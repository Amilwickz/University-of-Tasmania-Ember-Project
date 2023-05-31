#Particle trajectory creating on XY plane
#@Amil-UTAS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read the CSV file
df = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/trajectory_plotting_Ember_3.csv', skiprows=1)

#Extract the X, Y data of each ember from relevant Columns
column_0 = df.iloc[:, 0]#1st column (index 0)
column_1 = df.iloc[:, 1]#2nd column (index 1)

column_9 = df.iloc[:, 9]#10th column (index 9)
column_10 = df.iloc[:, 10]#11th column (index 10)

column_18 = df.iloc[:, 18]#19th column (index 18)
column_19 = df.iloc[:, 19]#20th column (index 19)

column_27 = df.iloc[:, 27]#28th column (index 27)
column_28 = df.iloc[:, 28]#29th column (index 29)

column_36 = df.iloc[:, 36]#37th column (index 36)
column_37 = df.iloc[:, 37]#38th column (index 38)

column_45 = df.iloc[:, 45]#46th column (index 45)
column_46 = df.iloc[:, 46]#47th column (index 47)

column_54 = df.iloc[:, 54]#55th column (index 54)
column_55 = df.iloc[:, 55]#56th column (index 56)

column_63 = df.iloc[:, 63]#64th column (index 63)
column_64 = df.iloc[:, 64]#65th column (index 65)


#Create a new DataFrame to store the filtered data
filtered_data_1 ={'Column_0':[], 'Column_1':[]}
filtered_data_2 ={'Column_9':[], 'Column_10':[]}
filtered_data_3 ={'Column_18':[], 'Column_19':[]}
filtered_data_4 ={'Column_27':[], 'Column_28':[]}
filtered_data_5 ={'Column_36':[], 'Column_37':[]}
filtered_data_6 ={'Column_45':[], 'Column_46':[]}
filtered_data_7 ={'Column_54':[], 'Column_55':[]}
filtered_data_8 ={'Column_63':[], 'Column_64':[]}


#Itereate over the rows and apply the filtering condition
previous_value_1 = float('-inf') #iterate with negative infinity
for value_0, value_2 in zip(column_0, column_1):
    if value_0 > previous_value_1:
        filtered_data_1['Column_0'].append(value_0)
        filtered_data_1['Column_1'].append(value_2)
        previous_value_1 = value_0

#Itereate over the rows and apply the filtering condition
previous_value_2 = float('-inf') #iterate with negative infinity
for value_9, value_11 in zip(column_9, column_10):
    if value_9 > previous_value_2:
        filtered_data_2['Column_9'].append(value_9)
        filtered_data_2['Column_10'].append(value_11)
        previous_value_2 = value_9

#Itereate over the rows and apply the filtering condition
previous_value_3 = float('-inf') #iterate with negative infinity
for value_18, value_20 in zip(column_18, column_19):
    if value_18 > previous_value_3:
        filtered_data_3['Column_18'].append(value_18)
        filtered_data_3['Column_19'].append(value_20)
        previous_value_3 = value_18

#Itereate over the rows and apply the filtering condition
previous_value_4 = float('-inf') #iterate with negative infinity
for value_27, value_29 in zip(column_27, column_28):
    if value_27 > previous_value_4:
        filtered_data_4['Column_27'].append(value_27)
        filtered_data_4['Column_28'].append(value_29)
        previous_value_4 = value_27

#Itereate over the rows and apply the filtering condition
previous_value_5 = float('-inf') #iterate with negative infinity
for value_36, value_38 in zip(column_36, column_37):
    if value_36 > previous_value_5:
        filtered_data_5['Column_36'].append(value_36)
        filtered_data_5['Column_37'].append(value_38)
        previous_value_5 = value_36

#Itereate over the rows and apply the filtering condition
previous_value_6 = float('-inf') #iterate with negative infinity
for value_45, value_47 in zip(column_45, column_46):
    if value_45 > previous_value_6:
        filtered_data_6['Column_45'].append(value_45)
        filtered_data_6['Column_46'].append(value_47)
        previous_value_6 = value_45

#Itereate over the rows and apply the filtering condition
previous_value_7 = float('-inf') #iterate with negative infinity
for value_54, value_56 in zip(column_54, column_55):
    if value_54 > previous_value_7:
        filtered_data_7['Column_54'].append(value_54)
        filtered_data_7['Column_55'].append(value_56)
        previous_value_7 = value_54


#Itereate over the rows and apply the filtering condition
previous_value_8 = float('-inf') #iterate with negative infinity
for value_63, value_65 in zip(column_63, column_64):
    if value_63 > previous_value_8:
        filtered_data_8['Column_63'].append(value_63)
        filtered_data_8['Column_64'].append(value_65)
        previous_value_8 = value_63

#Create a new DataFrame with the filtered data
new_df_1 = pd.DataFrame(filtered_data_1)
new_df_2 = pd.DataFrame(filtered_data_2)
new_df_3 = pd.DataFrame(filtered_data_3)
new_df_4 = pd.DataFrame(filtered_data_4)
new_df_5 = pd.DataFrame(filtered_data_5)
new_df_6 = pd.DataFrame(filtered_data_6)
new_df_7 = pd.DataFrame(filtered_data_7)
new_df_8 = pd.DataFrame(filtered_data_8)

#write the data to a new CSV file called "plot"
new_df_1.to_csv('plotXY_Cube_Ember1_small_distance.csv', index=False)
new_df_2.to_csv('plotXY_Cube_Ember2_small_distance.csv', index=False)
new_df_3.to_csv('plotXY_Cube_Ember3_medium_distance.csv', index=False)
new_df_4.to_csv('plotXY_Cube_Ember4_medium_distance.csv', index=False)
new_df_5.to_csv('plotXY_Cube_Ember5_medium_distance.csv', index=False)
new_df_6.to_csv('plotXY_Cube_Ember6_long_distance.csv', index=False)
new_df_7.to_csv('plotXY_Cube_Ember7_long_distance.csv', index=False)
new_df_8.to_csv('plotXY_Cube_Ember8_long_distance.csv', index=False)

plt.plot(new_df_1['Column_0'],new_df_1['Column_1'], color= "dimgrey", label = "Ember ID_457282 (small distance)")
plt.plot(new_df_2['Column_9'],new_df_2['Column_10'], color= "black", label = "Ember ID_330694 (small distance)")
plt.plot(new_df_3['Column_18'],new_df_3['Column_19'],color= "darkorange", label = "Ember ID_325459 (medium distance)")
plt.plot(new_df_4['Column_27'],new_df_4['Column_28'], color= "seagreen", label = "Ember ID_414414 (medium distance)")
plt.plot(new_df_5['Column_36'],new_df_5['Column_37'], color= "orchid", label = "Ember ID_338535 (medium distance)")
plt.plot(new_df_6['Column_45'],new_df_6['Column_46'], color= "darkblue", label = "Ember ID_366618 (long distance)")
plt.plot(new_df_7['Column_54'],new_df_7['Column_55'], color= "teal", label = "Ember ID_399574 (long distance)")
plt.plot(new_df_8['Column_63'],new_df_8['Column_64'],color= "red", label = "Ember ID_351359 (long distance)")

plt.title("Cube Embers' Trajectories")
plt.xlabel("X (m)")
plt.ylabel("Z (m)")
plt.xlim(300, 700)
plt.ylim(0,210)
plt.legend()
plt.grid()
plt.show()

