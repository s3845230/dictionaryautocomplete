
SIZE_OF_DATA_FILE=100

data_filename = "./data/sampleData200k.txt"
data_file = open(data_filename, 'r')

export_filename = "./data/datagen" + str(SIZE_OF_DATA_FILE) + ".txt"
export_file = open(export_filename, 'w')

count = 0

for line in data_file:
    export_file.write(line)
    count+=1
    if count >=SIZE_OF_DATA_FILE:
        break

export_file.close()
data_file.close()