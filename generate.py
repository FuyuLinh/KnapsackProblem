import argparse
import numpy 
import csv

parser = argparse.ArgumentParser()
parser.add_argument("size", type=str, help="the size")
args = parser.parse_args()

num_file = 5



def generate(size,num_instances):
    path = 'data/'+ size + f'/INPUT_{i}.txt'
    n = num_instances
    capacity = [numpy.random.randint(100,1000)]
    num_class = [numpy.random.randint(2,4)] # 2-3 classes for small dataset
    weight = numpy.random.randint(1,100,size=n[0])
    value = numpy.random.randint(1,100,size=n[0])
    label = numpy.random.randint(1,num_class[0]+1,size=n[0])

    with open(path, mode='w') as filehandle:
        file = csv.writer(filehandle, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(n)
        file.writerow(capacity)
        file.writerow(num_class)
        file.writerow(weight)
        file.writerow(value)
        file.writerow(label)

def read():
    with open('data/large/INPUT_1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        List = [item for item in csv_reader]
        a = [int(item) for item in List[0]]
        for item in List:
            print(item)


if args.size == "small":
    print("Hello small")
    for i in range(1,num_file+1):
        n = [numpy.random.randint(10,40)]
        generate(args.size,n)

else:
    print("Hello large")
    for i in range(1,num_file+1):
        n = [numpy.random.randint(50,1000)]
        generate(args.size,n)


    