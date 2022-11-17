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
