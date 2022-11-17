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
for each element in the list of all combinations:
  Sum of all value in the element
  Sum of the weight in the element
  check to satisfy all class appears at least once
        
  if Sum of weight <= Capacity and Sum of value > Best value recorded and all class appeared at least once:
    Best Value recorded = Sum of value
```
