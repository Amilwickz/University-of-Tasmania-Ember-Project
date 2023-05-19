import csv

filename = 'prt5_output.txt' # giving the file name
output_filename_1 = 'stationary_particles.csv'


with open(filename, 'r') as file:
    reader = csv.reader (file)
    headers = next(reader) # read the header row
    header_mapping = {'X': 0,'Y': 1, 'Z': 2, 'Time': 3, 'ID': 4}

    #Dictionary to store last observed values for each ID
    last_values ={}

    stationary_particles =[]#list to store the filtered rows
  

    #Read and sort the data based on the ID column
    #data = sorted(reader, key=lambda row: int(row[header_mapping['ID']]))

    for row in reader:
        col1 = row[header_mapping['X']]
        col2 = row[header_mapping['Y']]
        col3 = row[header_mapping['Z']]
        col4 = row[header_mapping['Time']]
        col5 = row[header_mapping['ID']]

        #check if the ID's X, Y, and Z values have changed
        if col5 in last_values and col1 == last_values[col5]['X'] and col2 ==last_values[col5]['Y'] and col3 == last_values[col5]['Z']:
            continue #skip this row

        #process the columns as needed
        stationary_particles.append([col1, col2, col3, col4, col5])


        #update last observed values for the ID
        last_values[col5] = {'X': col1, 'Y': col2, 'Z':col3}
with open(output_filename_1, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers) #write the header row
    writer.writerows(stationary_particles)



