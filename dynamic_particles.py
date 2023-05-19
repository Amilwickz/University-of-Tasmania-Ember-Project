import csv

filename = 'prt5_output.txt'  # giving the file name


with open(filename, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # read the header row
    header_mapping = {'X': 0, 'Y': 1, 'Z': 2, 'Time': 3, 'ID': 4}

    # Dictionary to store last observed values for each ID
    last_values = {}

    stationary_particles = []  # list to store the filtered rows

    # Read and sort the data based on the ID column
    # data = sorted(reader, key=lambda row: int(row[header_mapping['ID']]))

    for row in reader:
        col1 = row[header_mapping['X']]
        col2 = row[header_mapping['Y']]
        col3 = row[header_mapping['Z']]
        col4 = row[header_mapping['Time']]
        col5 = row[header_mapping['ID']]

        # check if the ID's X, Y, and Z values have changed
        if col5 not in last_values:
            last_values[col5] =col1
        else:
            if float(col1) - float(last_values[col5]) > 0:
                stationary_particles.append(row)
            last_values[col5] = col1

output_filename = "dynamicParicles.csv"

with open(output_filename, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(headers)
    writer.writerows(stationary_particles)






