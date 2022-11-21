# Algorithm 2: Branch and bound algorithm for KNAPSACK 
## 2.1. Description
- The goal of the branching and limiting algorithm is to find a maximum value of x such that the weight in the bag does not exceed a given limit.
- A B&B algorithm maintains track of boundaries on the minimum it is attempting to discover and utilizes these limitations to "prune" the search space by removing potential solutions that it can demonstrate won't include an ideal answer.
## 2.2 Pseudo code
#### PreProcess 
```python
def PreProccess ((length, capacity, num_class, weight_list, value_list, label_list):
    Result, length, Objects = Sort(length, num_class, weight_list, value_list, label_list)
    # Result is best in each class.
    # length, Objects after get best in each class.
    capacity -= Result[1][0] # weight of list Result
    # create init bag
    init_Bag = [capacity, Objects[0], 0, 0]
    # get items to bags
    total_value, final_Bag = Resolve(capacity, value_list, init_Bag, length)
    # add item to list item
    for item in final_Bag:
        Result[0].append(Objects[2][item-1])
    return total_value + Result[1][1], Result[0]
```
#### Process
```python
def Resolve(capacity, values, Bag, length, result=[], queue=[]):
    if length == 0:
        return Bag[2], result
    temp = Bag.copy()
    temp[0] -= Bag[1][length - 1]
    temp[2] += values[length - 1]
    temp[3] = optimistic(values, Bag, length)
    Bag[3] = optimistic(values, Bag, length - 1)
    if temp[0] >= 0:
        queue += [[Bag, length - 1, result], [temp, length - 1, result + [length]]]
    else:
        queue += [[Bag, length - 1, result]]
    queue = sorted(queue, key=fourth, reverse=True)
    best = queue.pop(0)
    return resolve(capacity, values, best[0], best[1], best[2], queue)
```
#### Auxiliary function
1. Calculate optimistic weight of the bag:
```python
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
```
2. Sort the initial list item by ascending:
```python
def Sort(length, num_class, weight_list, value_list, label_list):
    def ratio(e):
        return e[1] / e[0]

    X = [[weight_list[x], value_list[x], label_list[x], x] for x in range(length)]
    Y = sorted(X, key=ratio) # ration is (value/ weight)
    weights = [Y[x][0] for x in range(length)]
    values = [Y[x][1] for x in range(length)]
    labels = [Y[x][2] for x in range(length)]
    keys = [Y[x][3] for x in range(length)] # the initial index of item
    return getBestInClass(length, num_class, weights, values, labels, keys)
```
3. Get initial the best item in each class
```python 
def getBestInClass(length, num_class, weights, values, labels, keys):
    contained = [0, 0] 
    class_uncomplete = []
    res = []
    for i in range(num_class):
        class_uncomplete.append(1)
    x = length - 1
    while x > 0:
        if len(res) != num_class:
            if class_uncomplete[labels[x] - 1] == 1:
                # push key to inital index to res
                res.append(keys[x]) 
                # increase value in contained
                contained[0] += weights[x]
                contained[1] += values[x]
                # remove item from list
                del weights[x]
                del values[x]
                del keys[x]
                class_uncomplete[labels[x] - 1] = 0
                del labels[x]
            x = x - 1
        else:
            break
    return [res,contained], length - num_class, [weights, values, keys]
```
## 2.3 Explanation
- In preprocess section, we call the sort function to find the best item in each class and sort the list item after remove the best item by key = (value / weight).
- In process section, we recursively split the search space into smaller spaces, calculate the optimistic weight of the bag then choose a good case until you can't put any more items in the bag.
## 2.4 Test case
Input file
```
37
759
2
12,88,99,62,47,22,3,64,31,2,32,68,28,19,40,36,50,15,54,5,75,58,88,80,13,86,67,63,55,37,83,52,24,86,53,19,5
7,39,92,77,63,39,12,13,25,77,7,2,42,9,67,3,52,1,45,34,40,60,67,12,55,42,75,94,63,99,51,61,85,4,69,82,22
2,1,1,1,2,1,2,1,2,1,1,1,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,1,1,2,2
```
Output file
```
1273
0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,1,1
```
Time run: 0.6289482116699219 ms 
## 2.5 Conclusion
- Branch and bound algorithm performs a top-down recursive search through the tree of instances formed by the branch operation.
- If we compute on a large item dataset the amount of recursion will exceed the capacity of the resource that can execute. Example in large dataset 2 and 5. By sorting this list before process so the complexity will reduce.
## 2.6 Reference
- https://github.com/AndreaRubbi/Knapsack-implementation-Python/blob/master/Branch%26Bound.py
- https://iq.opengenus.org/0-1-knapsack-using-branch-and-bound/
- https://en.wikipedia.org/wiki/Branch_and_bound