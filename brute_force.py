# Algorithm 01: Brute Force Searching
# Capacity: W(kgs); Number for class: m
# Dataset: n items, each have value v_i, a class c_i, and weight w_i: item[(v_i1, c_i1, w_i1),...]
import csv
import argparse

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

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

def get_items(n,weight,value,label):
    items = []
    for i in range(0,n):
        items.append(Item(label[i],weight[i],value[i]))
    return items

def brute_force(item, m, Capacity):
    BValue = 0
    ClassCheck = set()
    Bestset = []

    # Create Subsets
    Combination = [[]]
    for i in item:
        newsubsets = [subset + [i] for subset in Combination]
        Combination.extend(newsubsets)
    Combination.pop(0)

    # Check optimal element in combination
    for listElement in Combination:
        Val_sum = 0
        Weight_sum = 0
        
        for j in listElement:
            Val_sum = Val_sum + j[0]
            Weight_sum = Weight_sum + j[1]
            ClassCheck.add(j[2])
        
        if Weight_sum <= Capacity and Val_sum > BValue and len(ClassCheck) >= m:
            BValue = Val_sum
            Bestset = listElement

    resultset = []
    for i in item:
        for j in Bestset:
            if i[0] == j[0] and i[1] == j[1] and i[2] == j[2]:
                resultset.append("1")
                break
        resultset.append("0")
    return BValue, resultset

#item = [(85, 79, 1),(26, 32, 1),(48, 47, 2),(21, 18, 1),(22, 26, 2),(95, 85, 1),(43, 33, 1),(45, 40, 2),(55, 45, 2),(52, 59, 2)]
#m = 2
#Capacity = 101
#brute_force(item, m, Capacity)
parser = argparse.ArgumentParser()
parser.add_argument("size", type=str, help="the size")
parser.add_argument("index", type=int, help="the index of INPUT file")
args = parser.parse_args()

if __name__ == '__main__':
    n,capacity,num_class,weight,value,label = read_txt(size=args.size,i=args.index)
    ITEMS =get_items(n[0],weight,value,label)
    brute_force(ITEMS,num_class,capacity)