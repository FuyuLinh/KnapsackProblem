import csv
import numpy as np

#--------------------------------import data from input files---------------------------------

def generate_tree_search(size, i):
  path = '../data/' + size + '/INPUT_' + str(i) + '.txt'
  with open(path, mode='r') as f:
    weight = int(f.readline())
    num_of_class = int(f.readline())
    reader = csv.reader(f)

    List = [row for row in reader]
    f.close()

    weight_list = List[0]
    value_list = List[1]
    class_list = List[2]
    heuristic_list = []
    quantity = len(value_list)

    for j in range(0, quantity):
      weight_list[j] = int(weight_list[j])
      value_list[j] = int(value_list[j])
      class_list[j] = int(class_list[j])
      heuristic_list.append(value_list[j]/weight_list[j])

  return quantity, weight, num_of_class, weight_list, value_list, class_list,heuristic_list

#---------------------------write data into output files-----------------------------------------

def output(total_value, _list, size, file):
  total_value = [total_value]
  path = '../output/'+ size + f'/OUTPUT_{file}.txt'
  with open(path, mode='w') as filehandle:
    file = csv.writer(filehandle, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file.writerow(total_value)
    file.writerow(map(lambda x: x, _list))
    filehandle.close()

#-------------------------find max heuristic classify by class----------------------------------------------

def find_max_heuristic(weight_list, value_list, class_list, heuristic_list, active_list, class_index, max_weight, total_weight, check_list, total_value):
  temp_heuristic = []
  temp_position = []
  _max = 0
  position = 0

  for i in range(0, len(class_list)):
    if class_list[i] == class_index and active_list[i] != True and total_weight + weight_list[i] <= max_weight:
      temp_heuristic.append(heuristic_list[i])
      temp_position.append(i)
  
  if(len(temp_heuristic) == 0):
    for i in range(0, len(class_list)):
      if class_list[i] == class_index and total_weight + weight_list[i] <= max_weight:
        temp_heuristic.append(heuristic_list[i])
        temp_position.append(i)

  for i in range(0, len(temp_heuristic)):
    if temp_heuristic[i] == max(temp_heuristic):
      _max = temp_heuristic[i]
      position = temp_position[i]
      total_weight += weight_list[position]
      total_value += value_list[position]
      break
  if len(temp_heuristic) == 0:
    check_list = False
  return total_weight, position, check_list, total_value

#------------------------------------------find max heuristic not clasify by class--------------------------------

def find_max_heuristic_not_by_class(weight_list, value_list, class_list, heuristic_list, active_list, max_weight, total_weight, total_value):
  temp_heuristic = []
  temp_position = []
  _max = 0
  position = 0
  check_full = False

  for i in range(0, len(class_list)):
    if active_list[i] != True and total_weight + weight_list[i] <= max_weight:
      temp_heuristic.append(heuristic_list[i])
      temp_position.append(i)

  for i in range(0, len(temp_heuristic)):
    if temp_heuristic[i] == max(temp_heuristic):
      _max = temp_heuristic[i]
      position = temp_position[i]
      total_weight += weight_list[position]
      total_value += value_list[position]
      break
  if len(temp_heuristic) == 0:
    check_full = True
  return total_weight, position, check_full, total_value

#--------------------------find the most optimal path of input file---------------------------------------

def local_beam_search(size, file):
  quantity, weight, num_of_class, weight_list, value_list, class_list,heuristic_list = generate_tree_search(size, file)
  k = 2

  list_position = []
  for i in range(0,k):
    list_position.append([])

  total_weight = [0]*k
  total_value = [0]*k
  check_list = [True]*k

  active_list = [False]*quantity #use when find at least 1 from every class

  #find max heuristic in every class and add 
  for i in range(1, num_of_class+1):
    for j in range(0, k):
      total_weight[j], position, check_list[j], total_value[j] = find_max_heuristic(weight_list, value_list, class_list, heuristic_list, active_list, i, weight, total_weight[j],check_list[j], total_value[j])
      active_list[position] = True
      list_position[j].append(position)

  active_list = []
  for i in range(0,k):
    active_list.append([False]*quantity)
    for j in list_position[i]:
      active_list[i][j] = True

  #find max heuristic in remain values and add to beams
  check_full = [False]*k
  while False in check_full:
    for i in range(0, k):
      total_weight[i], position, check_full[i], total_value[i] = find_max_heuristic_not_by_class(weight_list, value_list, class_list, heuristic_list, active_list[i], weight, total_weight[i], total_value[i])
      if check_full[i] == False:
        active_list[i][position] = True
        list_position[i].append(position)

  for i in range(0, k):
    if check_list[i] == False:
      total_weight.pop(i)
      total_value.pop(i)
      list_position.pop(i)

  for i in range(0, len(total_weight)):
    if total_value[i] == max(total_value):
      print_list = [0]*quantity
      total_value = 0
      for j in list_position[i]:
        print_list[j] = 1
        total_value += value_list[j]
      output(total_value, print_list, size, file)
      break

#------------------------main fuction to run through all input files-----------------------------------

def main():
  size = ['large', 'small']
  i = [1,2,3,4,5]
  for j in size:
    for z in i:
      local_beam_search(j,z)
      
main()