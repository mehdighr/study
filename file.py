import csv
with open("myfile.csv","w") as my_file:
    writer = csv.writer(my_file)
    writer.writerow(["name", "last name", "age"])
    
with open("myfile.csv","a+") as my_file:
    writer = csv.writer(my_file)
    read = csv.DictReader(my_file) 
    writer.writerow(["mehdi", "ghatrani", "18"])
    my_file.seek(0)
    for i in read:
        print(i)
    