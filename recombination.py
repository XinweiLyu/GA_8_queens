"""
My collection of recombination methods

"""

#imports
import random

def permutation_cut_and_crossfill_v2 (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    
    # student code begin
    # 随机选择交叉点
    xover_point = random.randint(1, len(parent1) - 2)

    # 子代的前半部分从对应父代直接复制
    offspring1.extend(parent1[:xover_point])
    offspring2.extend(parent2[:xover_point])

    # 子代的后半部分从另一个父代按顺序填充（跳过已经存在的基因）
    for gene in parent2:
        if gene not in offspring1:
            offspring1.append(gene)

    for gene in parent1:
        if gene not in offspring2:
            offspring2.append(gene)
                
    # student code end
    
    return offspring1, offspring2

def permutation_cut_and_crossfill(parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    l = len(parent1)  # 长度（基因数）

    # student code begin

    twice1 = []  # 用于记录 parent1 的基因序列
    twice2 = []  # 用于记录 parent2 的基因序列

    # 将 parent1 和 parent2 的基因存入 twice1 和 twice2
    for i in range(0, l):
        twice1.append(parent1[i])
        twice2.append(parent2[i])
    # print("twice1:", twice1)
    # print("twice2:", twice2)


    # 随机选择交叉点
    xover_point = random.randint(1, l - 2)
    # print("crossover point:", xover_point)

    # 复制前半部分
    for i in range(0, xover_point):
        offspring1.append(parent1[i])
        offspring2.append(parent2[i])
    # print("offspring1:", offspring1)
    # print("offspring2:", offspring2)

    # 填充剩余部分，避免重复基因
    j = xover_point
    print("j:", j)
    while len(offspring1) < l:
        if twice2[j % l] in offspring1:  # 检查基因是否已存在
            j = j + 1
        else:
            offspring1.append(twice2[j % l])
            j = j + 1

    j = xover_point  # 重置 j+
    while len(offspring2) < l:
        if twice1[j % l] in offspring2:  # 检查基因是否已存在
            j = j + 1
        else:
            offspring2.append(twice1[j % l])
            j = j + 1

    # student code end

    return offspring1, offspring2


# 测试代码
if __name__ == "__main__":
    parent1 = [1, 3, 5, 7, 2, 4, 6, 8]
    parent2 = [8, 6, 4, 2, 7, 5, 3, 1]
    off1, off2 = permutation_cut_and_crossfill(parent1, parent2)
    print("Parent 1:", parent1)
    print("Parent 2:", parent2)
    print("Offspring 1:", off1)
    print("Offspring 2:", off2)