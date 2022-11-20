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

def read_experiment(size):
    path = 'experiment/experiment_'+size+'.txt'
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        List = [item for item in csv_reader]
        n=[]
        time_computing =[]
        for num_size,time in List:
            n.append(int(num_size))
            time_computing.append(float(time))
        n, time_computing = (list(t) for t in zip(*sorted(zip(n, time_computing))))
    return n, time_computing