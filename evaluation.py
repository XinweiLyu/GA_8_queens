"""
My collection of fitness evaluation methods

"""

#imports


def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    

    #fitness = 0
    # student code begin
    M=28
    l = len(individual)
    check = 0

    # 计算冲突个数
    for i in range(l): # 遍历每个皇后
        for j in range(i + 1, l): # 遍历每个皇后之后的皇后
            # 检查是否在同一对角线
            if abs(individual[i] - individual[j]) == abs(i - j):
                check += 1

    # student code end
    
    return M- check # return the fitness value of the individual

# 测试代码
if __name__ == "__main__":
    individual1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(fitness_8queen(individual1))
    individual2 = [1, 8, 6, 4, 3, 7, 2, 5]
    print(fitness_8queen(individual2))
