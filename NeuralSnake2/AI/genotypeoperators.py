from random import *
from numpy import *
from constants import *

class GenotypeOperators(object):
    @staticmethod
    def breed(left_genotype, right_genotype):
        genotype = []
        for i in range(len(left_genotype)):
            max_value = pow(2, Constants.GENE_RESOLUTION - 1) - 1

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