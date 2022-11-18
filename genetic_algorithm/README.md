# Algorithm 4: Generic algorithm for KNAPSACK 
## 4.1. Description
- Genetic Algorithm is about natural selection that is studied in Biology subject.
- Any elements that can adapt to the changes will continue to go further and reproduce to go to next generation.
- We need to model it to undergo evolution through natural operations like Mutation, Crossover, Reproduction, and Selection.
### General Process of Generic Algorithm
- We radomly generate the population of indiviuals, which are the intial population - zeroth population and ready to generate new population.
- This new population are individuals that evolved from the zeroth population - expected to be better than their parents
- Based on narutal selection, the individuals who are fittest reproduce to create offspring
    - The offspring are either copies of the parent or undergo crossover where they get a fragment from each parent or an abrupt mutation.
- We consistently generate new population until it meets a termonation condition.
### Individual Representation
- An Individual in the Genetic Algorithm is a potential solution.
- We represented Individuals as the binary strings.
### Picking Individuals
- we generate a random set of Individuals that form our initial population.
- For example:
```
    0 0 0 1
    1 0 0 1
    1 1 0 1
    1 0 1 0
```
### Fitness Coefficient
- We calculate the fitness of each individual of the population
### Selection
- We will select some individuals for the next generations.
#### Tournament selection
- We shuffle the population and then randomly pick 4 individuals. We randomly pick 2 from 4 picked individuals and run a tournament between them. We repeat the same procedure and get the second parent for the next step.
### Crossover
- Crossover is an evolutionary operation between two individuals, and it generates children having some parts from each parent.
### Mutation
- The mutation is an evolutionary operation that randomly mutates an individual

### Reproduction

### Creating Generations
### Termination Condition
## 4.2 Pseudo code
## 4.3 Explanation
## 4.4 Visualization
    * picture
## 4.5 Test cases
## 4.6 Evaluation
### Run-time Complexity
## 4.7 Discusion
Genetic Algorithm helps generate solutions to optimize problems, like Knapsack, but it does not guarantee an optimal solution.
## 4.8 Conclusion

## 4.9 References