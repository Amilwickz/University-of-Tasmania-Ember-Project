import pandas as pd

#Read the tab seperated text file into a Data Frame
df = pd.read_csv('Cann_river_house_and_forest_coordinates.txt', sep=' ')

#store the data in a CSV file
df.to_csv('Cann_river_house_and_forest_coordinates_downsized_p293278.csv',  sep=',', index=False)

#read the first three columns of the stored CSV file
af = pd.read_csv('Cann_river_house_and_forest_coordinates_downsized_p293278.csv', usecols=[0, 1, 2])

#Store the values extracted from the above CSV file into an excel file with the headers of X, Y, Z in the first three columns
headers =['X','Y','Z']
af.columns = headers
af.to_excel('Cann_river_house_and_forest_coordinates_downsized_p293278XYZ.xlsx', index=False)

#Read the created excel file of 'CanRiverCompleteLowerPointsASCIIXYZ.xlsx'
kf = pd.read_excel('Cann_river_house_and_forest_coordinates_downsized_p293278XYZ.xlsx')
#find the maximum and minimum values of each column: This is to make the FDS script more simple
max_val_X = kf.iloc[:, 0].max()
min_val_X = kf.iloc[:, 0].min()

max_val_Y = kf.iloc[:, 1].max()
min_val_Y = kf.iloc[:, 1].min()

max_val_Z = kf.iloc[:, 2].max()
min_val_Z = kf.iloc[:, 2].min()

dif_X = max_val_X - min_val_X
dif_Y = max_val_Y - min_val_Y
dif_Z = max_val_Z - min_val_Z

print(f"Maximum value of X: {max_val_X}")
print(f"Minimum value of X: {min_val_X}")
print(f"Difference of X: {dif_X}", '\n')

print(f"Maximum value of Y: {max_val_Y}")
print(f"Minimum value of Y: {min_val_Y}")
print(f"Difference of Y: {dif_Y}", '\n')

print(f"Maximum value of Z: {max_val_Z}")
print(f"Minimum value of Z: {min_val_Z}")
print(f"Difference of Z: {dif_Z}", '\n')


#substracting the minimum value of each data point in each X, Y, Z column. By doing this we can simplify the FDS script
kf.iloc[:,0] = kf.iloc[:,0] - min_val_X
kf.iloc[:,1] = kf.iloc[:,1] - min_val_Y
kf.iloc[:,2] = kf.iloc[:,2] - min_val_Z - 25

#Write again the simplified excel file including the simplified X, Y, Z coordinates.
kf.to_excel('Cann_river_house_and_forest_coordinates_downsized_p293278XYZ_clear.xlsx', index=False)

lf = pd.read_excel('Cann_river_house_and_forest_coordinates_downsized_p293278XYZ_clear.xlsx')
nf_subset = lf.iloc[:, :3]

nf_new = pd.DataFrame()
nf_new['col1'] = 'aaa'  #add the necessary parts in the FDS script
nf_new['col2'] = 'bbb'  #add the necessary parts in the FDS script
nf_new['col3'] = 'ccc'  #add the necessary parts in the FDS script
nf_new['col4'] = nf_subset.iloc[:, 0]
nf_new['col5'] = nf_subset.iloc[:, 1]
nf_new['col6'] = nf_subset.iloc[:, 2]
nf_new['col7'] = 'N_PARTICLES=1/'

nf_new.to_csv('Cann_river_house_and_forest_coordinates_downsized_p293278XYZ_New_subset.txt', sep=',', index=False)

#arranging the data in ascending order according to X coordinates: The idea is to seperate forest and community to colour differently
qf = pd.read_excel('Cann_river_house_and_forest_coordinates_downsized_p293278XYZ_clear.xlsx', usecols=[0, 1, 2])
qf = qf.sort_values(by=qf.columns[0])

qf.to_excel('Sorted_Cann_river_house_and_forest_coordinates_downsized_p293278XYZ_clear.xlsx', index=False)

#write in seperate text files: Community WUI

#write coordinates in a seperate text file for the forest region (please enter the suitable X cordinate insted of value 435 upto the end of the forest region in the domain)
rf = pd.read_excel('Sorted_Cann_river_house_and_forest_coordinates_downsized_p293278XYZ_clear.xlsx', usecols=[0, 1, 2])
selected_data_1 = rf.loc[rf[rf.columns[0]] <= 440]

selected_data_forest = pd.DataFrame()
selected_data_forest['col1'] = 'aaa'  #add the necessary parts in the FDS script
selected_data_forest['col2'] = 'bbb'  #add the necessary parts in the FDS script
selected_data_forest['col3'] = 'ccc'  #add the necessary parts in the FDS script
selected_data_forest['col4'] = selected_data_1.iloc[:, 0]
selected_data_forest['col5'] = selected_data_1.iloc[:, 1]
selected_data_forest['col6'] = selected_data_1.iloc[:, 2]
selected_data_forest['col7'] = 'N_PARTICLES=1/'

selected_data_forest.to_csv('final_Sorted_forest_only_Cann_river_house_and_forest_coordinates_downsized_p293278XYZ_New_subset.txt', sep=',', index=False)

#write coordinates in a seperate text file for the forest region (please enter the suitable X cordinate insted of value 435 upto the end of the forest region in the domain)
selected_data_2 = rf.loc[(rf[rf.columns[0]] >= 440) & (rf[rf.columns[0]] <=700)]

selected_data_community = pd.DataFrame()
selected_data_community['col1'] = 'aaa'  #add the necessary parts in the FDS script
selected_data_community['col2'] = 'bbb'  #add the necessary parts in the FDS script
selected_data_community['col3'] = 'ccc'  #add the necessary parts in the FDS script
selected_data_community['col4'] = selected_data_2.iloc[:, 0]
selected_data_community['col5'] = selected_data_2.iloc[:, 1]
selected_data_community['col6'] = selected_data_2.iloc[:, 2]
selected_data_community['col7'] = 'N_PARTICLES=1/'

selected_data_community.to_csv('final_Sorted_community_only_Cann_river_house_and_forest_coordinates_downsized_p293278XYZ_New_subset.txt', sep=',', index=False)



