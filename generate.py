import argparse
import numpy 
import csv

parser = argparse.ArgumentParser()
parser.add_argument("size", type=str, help="the size")
args = parser.parse_args()

num_file = 5



def generate(size,num_instances,num_class,capacity):
    path = 'data/'+ size + f'/INPUT_{i}.txt'
    n = num_instances
    c = capacity
    num_classes = num_class 
    weight = numpy.random.randint(1,100,size=n[0])
    value = numpy.random.randint(1,100,size=n[0])
    label = numpy.random.randint(1,num_class[0]+1,size=n[0])

    with open(path, mode='w') as filehandle:
        file = csv.writer(filehandle, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(n)
        file.writerow(c)
        file.writerow(num_classes)
        file.writerow(weight)
        file.writerow(value)
        file.writerow(label)


if args.size == "small":
    print("Hello small")
    for i in range(1,num_file+1):
        n = [numpy.random.randint(10,40)]
        num_class = [numpy.random.randint(2,5)]
        capacity = [numpy.random.randint(100,1000)]
        generate(args.size,n,num_class,capacity)

else:
    print("Hello large")
    for i in range(1,num_file+1):
        n = [numpy.random.randint(50,1000)]
        num_class = [numpy.random.randint(5,11)]
        capacity = [numpy.random.randint(2000,25000)]
        generate(args.size,n,num_class,capacity)


    