import csv
def read_txt(size,i):
    path = '../data/' + size + f'/INPUT_{i}.txt'
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        List = [item for item in csv_reader]
        n = [int(item) for item in List[0]]
        capacity = [int(item) for item in List[1]]
        num_class = [int(item) for item in List[2]]
        weight = [int(item) for item in List[3]]
        value = [int(item) for item in List[4]]
        label = [int(item) for item in List[5]]
    return n,capacity,num_class,weight,value,label
