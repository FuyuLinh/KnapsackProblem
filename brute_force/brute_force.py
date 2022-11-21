# Algorithm 01: Brute Force Searching
# Capacity: W(kgs); Number for class: m
# Dataset: n items, each have value v_i, a class c_i, and weight w_i: item[(v_i1, c_i1, w_i1),...]
from typing import List
# from read import read_txt
import csv
import argparse

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight
    def get_value(self):
        return self.value

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
            Val_sum = Val_sum + j.get_value()
            Weight_sum = Weight_sum + j.get_weight()
            ClassCheck.add(j.get_name())
        
        if Weight_sum <= Capacity and Val_sum > BValue and len(ClassCheck) >= m:
            BValue = Val_sum
            Bestset = listElement

    resultset = []
    for i in item:
        if i in Bestset:
            resultset.append("1")
        else:
            resultset.append("0")
    return BValue, resultset

def save_txt(resultset,BValue,size,i):
    path = "output_" + size + f'/OUTPUT_{i}.txt'
    totalvalue =[BValue]
    found_solution = resultset
    with open(path, mode='w') as filehandle:
        file = csv.writer(filehandle, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(totalvalue)
        file.writerow(found_solution)

parser = argparse.ArgumentParser()
parser.add_argument("size", type=str, help="the size")
parser.add_argument("index", type=int, help="the index of INPUT file")
args = parser.parse_args()

if __name__ == '__main__':
    n,capacity,num_class,weight,value,label = read_txt(size=args.size,i=args.index)
    ITEMS =get_items(n[0],weight,value,label)
    BValue,resultset = brute_force(ITEMS,num_class[0],capacity[0])
    save_txt(resultset,BValue,args.size,args.index)