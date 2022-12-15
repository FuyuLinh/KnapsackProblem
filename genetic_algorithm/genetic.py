import random
from typing import List
from read import read_txt
import csv
import argparse
import time


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


class Individual:
    def __init__(self, bits: List[int]):
        self.bits = bits
    
    def __str__(self):
        return repr(self.bits)

    def __hash__(self):
        return hash(str(self.bits))
   
    def get_bits(self):
        return self.bits

    def fitness(self) -> int:
        total_value = sum([
            bit * item.value
            for item, bit in zip(ITEMS, self.bits)
        ])

        total_weight = sum([
            bit * item.weight
            for item, bit in zip(ITEMS, self.bits)
        ])

        if total_weight <= MAX_KNAPSACK_WEIGHT:

            return total_value
        
        return 0

CROSSOVER_RATE = 0.53
MUTATION_RATE = 0.013
REPRODUCTION_RATE = 0.15


def generate_initial_population(items,count=10) -> List[Individual]:
    population = set()

    while len(population) != count:
        bits = [
            random.choice([0, 1])
            for _ in items
        ]
        population.add(Individual(bits))
    return list(population)


def selection(population: List[Individual]) -> List[Individual]:
    parents = []
    
    random.shuffle(population)

    if population[0].fitness() > population[1].fitness():
        parents.append(population[0])
    else:
        parents.append(population[1])
    
    # tournament between third and fourth
    if population[2].fitness() > population[3].fitness():
        parents.append(population[2])
    else:
        parents.append(population[3])

    return parents


def crossover(parents: List[Individual],n) -> List[Individual]:
    N = n

    child1 = parents[0].bits[:N//2] + parents[1].bits[N//2:]
    child2 = parents[0].bits[N//2:] + parents[1].bits[:N//2]

    return [Individual(child1), Individual(child2)]


def mutate(individuals: List[Individual]) -> List[Individual]:
    for individual in individuals:
        for i in range(len(individual.bits)):
            if random.random() < MUTATION_RATE:
                # Flip the bit
                individual.bits[i] = ~individual.bits[i]


def next_generation(population: List[Individual],n) -> List[Individual]:
    next_gen = []
    while len(next_gen) < len(population):
        children = []

        parents = selection(population)

        # reproduction
        if random.random() < REPRODUCTION_RATE:
            children = parents
        else:
            # crossover
            if random.random() < CROSSOVER_RATE:
                children = crossover(parents,n)
            
            # mutation
            if random.random() < MUTATION_RATE:
                mutate(children)

        next_gen.extend(children)

    return next_gen[:len(population)]


def print_generation(population: List[Individual]):
    for individual in population:
        print(individual.bits, individual.fitness())
    print()
    print("Average fitness", sum([x.fitness() for x in population])/len(population))
    print("-" * 32)


def average_fitness(population: List[Individual]) -> float:
    return sum([i.fitness() for i in population]) / len(population)


def solve_knapsack(items,n) -> Individual:
    population = generate_initial_population(items)

    avg_fitnesses = []

    for _ in range(500):
        avg_fitnesses.append(average_fitness(population))
        population = next_generation(population,n)

    population = sorted(population, key=lambda i: i.fitness(), reverse=True)
    return population[0]


def solution(ITEMS,n):
    solution = solve_knapsack(items=ITEMS,n=n)
    return solution.bits,solution.fitness()

def get_items(n,weight,value,label):
    items = []
    for i in range(0,n):
        items.append(Item(label[i],weight[i],value[i]))
    return items

def save_solution(solution,score,size,i):
    path = '../genetic_algorithm/output_'+ size + f'/OUTPUT_{i}.txt'
    fitness =[score]
    found_solution = solution
    with open(path, mode='w') as filehandle:
        file = csv.writer(filehandle, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(fitness)
        file.writerow(found_solution)

def save_experiment(n,time_computing):
    # save n, save time-out
    path = '../genetic_algorithm/experiment.txt'
    row = [n,time_computing]
    with open(path, mode='a') as filehandle:
        file = csv.writer(filehandle, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(row)


    
parser = argparse.ArgumentParser()
parser.add_argument("size", type=str, help="the size")
parser.add_argument("index", type=int, help="the index of INPUT file")
args = parser.parse_args()

if __name__ == '__main__':
    n,capacity,num_class,weight,value,label = read_txt(size=args.size,i=args.index)
    MAX_KNAPSACK_WEIGHT = capacity[0]
    ITEMS =get_items(n[0],weight,value,label)
    #start_time = time.time()
    solution,score = solution(ITEMS,n[0])
    print(solution,score)
    save_solution(solution,score,args.size,args.index)
    #time_computing = time.time() - start_time
    #save_experiment(n[0],time_computing)
        
