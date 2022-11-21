Report
=========================================================================
I. Algorithm 01: Brute-force Algorithm
-------------------------------------------------------------------------
### 1. Algorithm's description:
Brute-force algorithm is the easiest algorithm to solve many search problem in general and the Knapsack's problem itself. The idea of brute-force algorithm applied in this problem is to create all possible combinations created from the list of items, then run through every combinations to find the best match for the dataset.
### 2. Pseudo code:
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
### 3. Evaluation:
Working out all possible subsets takes $2^{N}$.

Calculating sum of each subset from 1 to N => Take N x $2^{N}$.

=> Time of Complexity: O (N x $2^{N}$)
### 4. Test case:
We use the same test case "data" which has been divided into two sub-folder "small" datasets and "large" datasets for all of the algorithms in our project. The small datasets involve less than 50 items per case. The large dataset include over 50 items per case.
### 5 Evaluation:
Brute force algorithm is easier to implement. However it is not as efficient as the other algorithms and it cannot optimize this project's problem.
### 6. Discussion:
This algorithm can help solving Knapsack problem with small datasets. However when facing with bigger datasets, the time to execute this algorithm will be much longer compared to other algorithms.
### 7. References:
https://gist.github.com/YJDave/c9ad61598bbe6d059ef0396b77bbd612
