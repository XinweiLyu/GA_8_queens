"""
My collection of initialization methods for different representations

"""

#imports
import numpy


def permutation (pop_size, chrom_length):
    """initialize a population of permutation
        :return retuan a list(pop size number) of permutation
    """

    population = []
    # student code begin
    for i in range(pop_size):
        # 生成一个随机排列，表示棋盘上的皇后位置
        population.append(numpy.random.permutation(chrom_length))
    #student code end
    
    return population                     

if __name__ == "__main__":
    print(permutation(10, 8))