Report of Group's Project 01
============================
# Individual's detailed Information:
1. Nguyễn Hà Ngọc Linh - 20125061
2. Phạm Thanh Tú - 20125121
3. Phan Huỳnh Tấn Phát - 20125047
4. Phạm Quốc Thiệu - 20125114
## Assignment plan:
Each individual will hold one algorithm to solve the problem. The whole work for one algorithm includes:
- Implementation
- Running Test cases
- Showing videos of the whole process
- Writing own report about the algorithm

The algorithms have been assigned in the following plan:
- Nguyễn Hà Ngọc Linh: "Brute force algorithm"
- Phạm Thanh Tú: "Genetic algorithm"
- Phan Huỳnh Tấn Phát: "Branch and Bound algorithm"
- Phạm Quốc Thiệu: "Local Beam search algorithm"

# Self-assessment for completion level for each requirement:
## 1. Brute-force algorithm:
Completed works:
- Implementation
- Showing videos of process
- Writing reports about the algorithms
- Running Test cases: Since brute-force cannot optimize time for the problem, it takes one test case with only 35 items up to 1 hour to complete generating output file. Hence we cannot generate all test cases.

Incompleted works: None recorded

Completion level: 9.5/10
## 2. Genetic algorithm:
Completed works:
- Implementation
- Running Test cases
- Showing videos of process
- Writing reports about the algorithms

Incompleted works: None recorded

Completion level: 10/10
## 3. Branch and bound algorithm:
Completed works:
- Implementation
- Running Test cases
- Showing videos of process
- Writing reports about the algorithms

Incompleted works: None recorded

Completion level: 10/10
## 4. Local Beam search algorithm:
Completed works:
- Implementation

Completion level: /10
# Algorithm 1: Brute force algorithm:
## 1.1. Description:
Brute-force algorithm is the easiest algorithm to solve many search problem in general and the Knapsack's problem itself. The idea of brute-force algorithm applied in this problem is to create all possible combinations created from the list of items, then run through every combinations to find the best match for the dataset.
## 1.2. Pseudo code:
The following Codeblock quickly go through the procedure of Brute-force algorithm.
```python
# item represents the set of all items in the data set, each have value vi, class ci, and weight wi
# Create subsets from all posible combinations
for i in item:
  newsubsets = [subset + [i] for subset in Combination]
  Combination.extend(newsubsets)
  
# Find the optimal solution, which satisfied the highest value that can be reached but not excced the capacity of the Knapsack
for each_element in the_list_of_all_combinations:
  Sum_of_value in element
  Sum_of_weight in element
  check_all_class_appears_at_least_once
        
  if Sum_of_weight <= Capacity and Sum_of_value > Best_value_recorded and all_class_appears_at_least_once:
    Best_value_recorded = Sum_of_value
```
## 1.3. Evaluation:
Working out all possible subsets takes $2^{N}$.

Calculating sum of each subset from 1 to N => Take N x $2^{N}$.

=> Time of Complexity: O (N x $2^{N}$)

Brute force algorithm is easier to implement. However it is not as efficient as the other algorithms and it cannot optimize this project's problem.
## 1.4. Test case:
We use the same test case "data" which has been divided into two sub-folder "small" datasets and "large" datasets for all of the algorithms in our project. The small datasets involve less than 50 items per case. The large dataset include over 50 items per case.

However brute force can only generate small datasets, we run the test case of 13 items at most.

Input file
```
13
298
2
88,54,73,13,40,65,16,76,90,46,11,11,11
1,78,10,64,5,12,66,21,82,31,23,2,32
2,2,1,1,2,2,1,1,2,2,1,1,1
```
Output file
```
383
0,1,0,1,1,0,1,0,1,1,1,1,1
```
## 1.5. Discussion & Comments:
This algorithm can help solving Knapsack problem with small datasets. However when facing with bigger datasets, the time to execute this algorithm will be much longer compared to other algorithms.
## 1.6. Conclusion:
Brute force algorithm is about combining and generating all posible powersets, then run from 1 to N powersets in order to find the best powerset. This algorithm cannot be used in large datasets to avoid wasting time.
## 1.7. References:
- https://gist.github.com/YJDave/c9ad61598bbe6d059ef0396b77bbd612
- https://github.com/AndrewGEvans95/Knapsack/blob/master/solutions/BruteForce.py
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
# Algorithm 4: Generic algorithm:
## 4.1. Description:
- Genetic Algorithm is about natural selection that is studied in Biology subject.
- Any elements that can adapt to the changes will continue to go further and reproduce to go to next generation.
- We need to model it to undergo evolution through natural operations like Mutation, Crossover, Reproduction, and Selection.
### General Process of Generic Algorithm:
- We radomly generate the population of indiviuals, which are the intial population - zeroth population and ready to generate new population.
- This new population are individuals that evolved from the zeroth population - expected to be better than their parents
- Based on narutal selection, the individuals who are fittest reproduce to create offspring
    - The offspring are either copies of the parent or undergo crossover where they get a fragment from each parent or an abrupt mutation.
- We consistently generate new population until it meets a termonation condition.
### Individual Representation:
- An Individual in the Genetic Algorithm is a potential solution.
- We represented Individuals as the binary strings.
### Picking Individuals:
- We generate a random set of Individuals that form our initial population.
- For example:
```
    0 0 0 1
    1 0 0 1
    1 1 0 1
    1 0 1 0
```
### Fitness Coefficient:
- We calculate the fitness of each individual of the population
### Selection:
- We will select some individuals for the next generations.
#### Tournament selection:
- We shuffle the population and then randomly pick 4 individuals. We randomly pick 2 from 4 picked individuals and run a tournament between them. We repeat the same procedure and get the second parent for the next step.
### Crossover:
- Crossover is an evolutionary operation between two individuals, and it generates children having some parts from each parent.
### Mutation:
- The mutation is a way of changing unexpectedly the struture of individual, which randomly mutates an individual. It randomly changes a bit in an individual based on the probibility of mutation.

### Reproduction:
- Reproduction is a way of keeping the structure of individual for the next generation without being affected by mutation or crossover. We pass the genes with the high fitness score to the next generations to reach the optimal solution.
### Creating Generations:
- From the initial generations - zeroth population, we continues to creat the next generation that is first population. This process is done by repeating the process of Selection, Reproduction, Crossover, and Mutation till we get the same number of children as the initial population.
### Termination Condition:
- We cannot create generations infinitely as human population or living things in nature. We should set it up a condition as the process of looping about 500 cycles of creating new generation.
## 4.2 Pseudo code:
```python
def solve_genetic_knapsack():
    population = creat_initial_generation()

    for i in range(500):

        score = compute_avarage_fitness_score(population)

        # in this process, we implement the selection, muation, crossover, reproduction.
        population = next_generations(population)

    # sort the solution by the score
    solution = sort(population,population.fitness())

    # get the optimal solution - the individual with the high fitness score
    return solution[0]
```
## 4.3 Explanation:
- This algorithm is all about natural randomness. First, it randomly generate the initial population - zeroth population. Second we compute the avarage fitness score of whole populaion. We create the new generation and repeat this process 500 times. In the process of creating generations, we implement selection, crossover, muation, and reproduction.
## 4.4 Visualization:
![](image/process.png?raw=true "Process of Genetic Algorithm")
## 4.5 Test cases:
Input file
```
39
508
3
92,62,6,14,45,77,17,5,46,75,67,11,2,52,12,42,49,71,29,86,38,1,82,41,17,90,41,98,5,3,96,77,51,6,52,41,54,89,50
43,51,34,65,78,27,57,38,30,81,79,26,42,67,51,31,84,3,23,87,95,75,25,57,82,8,76,34,53,38,74,48,15,3,95,94,88,4,22
3,2,3,2,3,2,1,2,2,1,1,2,1,2,3,3,2,3,2,1,1,3,1,2,1,1,3,1,1,1,1,3,1,1,1,1,3,2,3
```

Output file 
```
649
0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0
```
## 4.6 Evaluation:
![](image/experiment_small.png?raw=true "Process of Genetic Algorithm")
- The time is proportional to the number of given items. When we increae it to a large number, then it takes more time to generate the solution. 
- The size of population increase the time computing as well. We need to choose the right population to avoid the redundancy or inadequacy. 
## 4.7 Discussion & Comments:
- Genetic Algorithm helps generate solutions to optimize problems, like Knapsack, but it does not guarantee an optimal solution. With the large population of individuals, we have more chance to approach the optimal solutions, but the tradeoff is the time computing.
- If we compute on large item datasets - over 100 items - with the small initial population like less than 10 individuals, we hardly get the optimal result and then it retuns value 0 - none of solutions are fit.
## 4.8 Conclusion:
- Genetic algorithm is all about randomness, we set all parametes to the random numbers. The good genetic model really depends on these random numbers like size of population, the iteration of generations, muatation rate, crossover rate, reproduction rate.
- When you want to get the optimal solution, you need to set the size of population to a large number. It gives us the high chance to get the fittest solution, but the tradeoff is time computing.
## 4.9 References:
- https://www.geeksforgeeks.org/genetic-algorithms/
- https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
- https://github.com/MohammadAsadolahi/knapsack-problem-solved-with-evolutionary-strategy-Genetic-algorithm-in-python/blob/main/knapsack%20with%20GA.py
- https://arpitbhayani.me/blogs/genetic-knapsack
- https://github.com/mohilpatel25/0-1-knapsack-using-genetic-algorithm

# Group workspace:
- Github repository: https://github.com/FuyuLinh/KnapsackProblem
- Video demo process (Link Google Drive): https://drive.google.com/drive/folders/1RyPIzK3kiCHfyBXLixnJJDor9oZmkT-G?usp=sharing

We have commit codes of each algorithm in the <SID>.zip file along with this report. In case it may occur any bugs or errors, we wish to send you the codes throught github repository for alternative method. Thank you very much for considering our project.
