import csv
import time
import SortList


def Optimistic(values, weights, length):
    optimistic_weight = weights[2]
    capacity = weights[0]
    while capacity > weights[1][length - 1] and length > 0:
        optimistic_weight += values[length - 1]
        capacity -= weights[1][length - 1]
        length -= 1
    if length != 0:
        optimistic_weight += int(values[length - 1] * (capacity / weights[1][length - 1]))
    return optimistic_weight


def Resolve(capacity, values, Bag, length, result=[], queue=[]):
    def fourth(e):
        return e[0][3]

    if length == 0:
        return Bag[2], result
    temp = Bag.copy()
    temp[0] -= Bag[1][length - 1]
    temp[2] += values[length - 1]
    temp[3] = Optimistic(values, Bag, length)
    Bag[3] = Optimistic(values, Bag, length - 1)
    if temp[0] >= 0:
        queue += [[Bag, length - 1, result], [temp, length - 1, result + [length]]]
    else:
        queue += [[Bag, length - 1, result]]
    queue = sorted(queue, key=fourth, reverse=True)
    best = queue.pop(0)
    return Resolve(capacity, values, best[0], best[1], best[2], queue)


def PreProccess(length, capacity, num_class, weight_list, value_list, label_list):
    Result, length, Objects = SortList.Sort(length, num_class, weight_list, value_list, label_list)
    capacity -= Result[1][0]
    init_Bag = [capacity, Objects[0], 0, 0]
    total_value, final_Bag = Resolve(capacity, Objects[1], init_Bag, length)
    for item in final_Bag:
        Result[0].append(Objects[2][item - 1])
    return total_value + Result[1][1], Result[0]


def init_data(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        List = [item for item in csv_reader]
        capacity = List[0]
        capacity = int(capacity[0])
        num_class = List[1]
        num_class = int(num_class[0])
        weight_list = [int(item) for item in List[2]]
        value_list = [int(item) for item in List[3]]
        label_list = [int(item) for item in List[4]]
        length = len(weight_list)
    csv_file.close()
    return length, capacity, num_class, weight_list, value_list, label_list


def saveResult(data_path, output_path):
    x = time.time()
    length, capacity, num_class, weight_list, value_list, label_list = init_data(data_path)
    Result = PreProccess(length, capacity, num_class, weight_list, value_list, label_list)
    w = time.time()
    list = [0 for i in range(length)]
    for i in Result[1]:
        list[i] = 1
    with open(output_path, 'w') as f:
        f.write(str(Result[0]) + "\n")
        for i in range(length):
            if i == length - 1:
                f.write(str(list[i]) + "\n")
            else:
                f.write(str(list[i]) + ",")
    f.close()
    with open('./experiments/experiment.txt', 'a') as ex:
        ex.write(str(length) + "," + str(w - x) + '\n')
    f.close()


if __name__ == '__main__':
    type = 'large'
    i = 4
    data_path = './data/' + type + '/INPUT_' + str(i) + '.txt'
    output_path = './output/' + type + '/OUTPUT_' + str(i) + '.txt'
    saveResult(data_path, output_path)
