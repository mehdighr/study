import json


with open("myfile.json","w+") as my_file:
    json.dump([1, 2, 3], my_file, indent= 4, separators= ("=", "="))
    my_file.seek(0)
    print(json.load(my_file))
