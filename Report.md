Report of Group's Project 01
============================
## Individual's detailed Information:
1. Nguyễn Hà Ngọc Linh - 20125061
2. Phạm Thanh Tú - 20125121
3. Phan Huỳnh Tấn Phát -
4. Phạm Quốc Thiệu - 
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

## Self-assessment for completion level for each requirement:
### 1. Brute-force algorithm:
Completed works:
- Implementation
- Showing videos of process
- Writing reports about the algorithms

Incompleted works:
- Running Test cases: Since brute-force cannot optimize time for the problem, it takes one test case with only 10 items up to 1 hour to complete generating output file. Hence we cannot generate all test cases.

Completion level: 7.5/10
### 2. Generic algorithm:
Completed works:
- Implementation
- Running Test cases
- Showing videos of process
- Writing reports about the algorithms

Incompleted works: None recorded

Completion level: 10/10
### 3. Branch and bound algorithm:
Completed works:
- Implementation

Incompleted works:

### 4. Local Beam search algorithm:
Completed works:
- Implementation

## Individual's report:
### 1. Brute force algorithm:
#### **Description:**
Brute-force algorithm is the easiest algorithm to solve many search problem in general and the Knapsack's problem itself. The idea of brute-force algorithm applied in this problem is to create all possible combinations created from the list of items, then run through every combinations to find the best match for the dataset.
#### **Pseudo code:**
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
#### **Evaluation:**
Working out all possible subsets takes $2^{N}$.

Calculating sum of each subset from 1 to N => Take N x $2^{N}$.

=> Time of Complexity: O (N x $2^{N}$)

Brute force algorithm is easier to implement. However it is not as efficient as the other algorithms and it cannot optimize this project's problem.
#### **Test case:**
We use the same test case "data" which has been divided into two sub-folder "small" datasets and "large" datasets for all of the algorithms in our project. The small datasets involve less than 50 items per case. The large dataset include over 50 items per case.

However brute force can only generate small datasets, we run the test case of 10 items at most.
