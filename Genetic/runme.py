import random

random_chromosome = lambda size: [random.randint(1,size) for _ in range(size)]
random_chromosome.__doc__='making random chromosomes'

def fitness(chromosome,maxFitness=None):
    n = len(chromosome)
    if maxFitness==None:
        maxFitness=(n*(n-1))/2
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2

    left_diagonal=[0]*(2*n)
    right_diagonal=[0]*(2*n)
    for index,chrom in enumerate(chromosome):
        left_diagonal[index+chrom-1]+=1
        right_diagonal[n-index+chrom-2]+=1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i]  > 1: counter += left_diagonal[i]-1
        if right_diagonal[i] > 1: counter += right_diagonal[i]-1
        diagonal_collisions+= counter / (n-abs(i-n+1))

    return int(maxFitness-(horizontal_collisions + diagonal_collisions))

probability=lambda chromosome, fitness,maxFitness=1: fitness(chromosome)/maxFitness

def random_pick(population, probabilities):
    # tmp={tuple(i):j for i,j in zip(population, probabilities)}
    # return list(max(tmp,key=lambda x:tmp[x]))
    r = sum(probabilities)*random.random()
    upto = 0
    for c, w in zip(population, probabilities):
        upto+=w
        if upto>=r: return c
    raise RuntimeError("This is unreachable state :(")

def reproduce(x, y):
    assert len(x)==len(y)
    '''doing cross_over between two chromosomes'''
    c = random.randint(0,len(x)-1)
    return x[:c]+y[c:]

def mutate(x):
    '''randomly changing the value of a random index of a chromosome'''
    n = len(x)
    x[random.randint(0,n-1)]=random.randint(1,n)
    return x

def genetic_queen(population, fitness,maxFitness,mutationProbability = 0.03):
    new_population = []
    probabilities = [probability(n, fitness,maxFitness) for n in population]
    probabilities = [probability(n, fitness,maxFitness) for n in population]
    for _ in population:
        x = random_pick(population, probabilities) #best chromosome 1
        y = random_pick(population, probabilities) #best chromosome 2
        child = reproduce(x, y) #creating two new chromosomes from the best 2 chromosomes
        if random.random() < mutationProbability:
            child = mutate(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
    return new_population

def main(nq,initialPopulation=100):
    maxFitness = (nq*(nq-1))/2
    population = [random_chromosome(nq) for _ in range(initialPopulation)]
    generationCount = 1
    while not maxFitness in [fitness(chrom) for chrom in population]:
        # new generation starts
        population = genetic_queen(population, fitness,maxFitness)
        generationCount += 1
    generationCount-=1
    for chrom in population:
        if fitness(chrom) == maxFitness:
            return "\n".join('0 '*(i-1)+'1 '+'0 '*(nq-i) for i in chrom),generationCount

if __name__ == "__main__":
    TABLE_SIZE=5
    print("{}\n\nsolution found after {} generations".format(*main(TABLE_SIZE)))
