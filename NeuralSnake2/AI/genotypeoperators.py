from random import *
from numpy import *
from constants import *

class GenotypeOperators(object):
    @staticmethod
    def breed(left_genotype, right_genotype):
        genotype = []
        max_value = pow(2, Constants.GENE_RESOLUTION - 1) - 1

        for i in range(len(left_genotype)):
            gene = 0
            left_gene  = int((left_genotype[i] + 1) * max_value)
            right_gene = int((right_genotype[i] + 1) * max_value)

            for bit in range(Constants.GENE_RESOLUTION):
                if randint(0, 1) == 0:
                    gene |= left_gene & pow(2, bit)
                else:
                    gene |= right_gene & pow(2, bit)

            genotype.append(gene / max_value - 1)
        return genotype

    @staticmethod
    def mutate(genotype):
        mutated_genotype = []
        max_value = pow(2, Constants.GENE_RESOLUTION - 1) - 1

        for i in range(len(genotype)):
            gene = genotype[i]
            if(randint(0, 100) < Constants.MUTATION_RATIO):
                gene_to_mutate  = int((genotype[i] + 1) * max_value)
                bit_index = randint(0, Constants.GENE_RESOLUTION - 1)
                gene = gene_to_mutate ^ (1 << bit_index)
                gene = gene / max_value - 1

            mutated_genotype.append(gene)
        return mutated_genotype