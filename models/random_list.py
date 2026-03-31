import random

RANDOM_LIST = [random.randrange(1,1000) for i in range(1000)]

with open("list.txt","w")  as unsorted_file:
    unsorted_file.writelines(str(RANDOM_LIST))
    unsorted_file.close()

print(RANDOM_LIST)