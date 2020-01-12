import random
import time
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("field_size", help = "input size of game field")
parser.add_argument("iterations", help = "input amount of game iterations")
args = parser.parse_args()

N = int(args.field_size) 

Cnt = int(args.iterations)



#поле для игры
# 1 - это клетка с креветкой
# 2 - это клетка с рыбкой
# 3 - это клетка со скалой
# 0 - это пустая клетка



nbrs = [[1,1], [1,-1], [-1,1], [-1,-1], [1, 0], [0, 1], [-1, 0], [0, -1]]


def make_field(n):
    clist = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(random.choice([0, 1, 2, 3]))
        clist.append(a)
    return clist

def new_field(clist, n, nbrs):
    new_list = []
    for i in range(n):
        x = []        
        for j in range(n):
            fish_cnt = 0
            shrimp_cnt = 0
            for k in range(8): # посмотрим на каждого из соседей текущей ячейки
                s1 = i + nbrs[k][0]
                s2 = j + nbrs[k][1]                   
                if (s1 < n and s1 >= 0 and s2 < n and s2 >= 0):                    
                    if clist[s1][s2] == 2: #посчитаем количество соседей рыбок
                        fish_cnt+=1
                    if clist[s1][s2] == 1: #посчитаем количество соседей креветок                        
                        shrimp_cnt+=1
            if clist[i][j] == 2 and (fish_cnt == 2 or fish_cnt == 3): # рыбка выживает
                x.append(2)
            elif clist[i][j] == 2 and (fish_cnt < 2 or fish_cnt > 3): # рыбка умирает
                x.append(0)
            if clist[i][j] == 1 and (shrimp_cnt == 2 or shrimp_cnt == 3): # креветка выживает
                x.append(1)
            elif clist[i][j] == 1 and (shrimp_cnt < 2 or shrimp_cnt > 3): # креветка умирает
                x.append(0)
            if clist[i][j] == 0 and fish_cnt == 3: # рождается рыбка
                x.append(2)
            elif clist[i][j] == 0 and shrimp_cnt == 3: # рождается креветка
                x.append(1)
            elif clist[i][j] == 0 and shrimp_cnt != 3 and fish_cnt != 3:
                x.append(0)
            if clist[i][j] == 3: # скала остается неизменной
                x.append(3)
        new_list.append(x)
    clist = new_list
    return clist    

cell_list = make_field(N)

a = '___' #пустота
b =  '###' #скала
c = '<o>' #креветка
d = '>=o' # рыбка

def PrintCellList(clist, n):
    for i in range(n):
        for j in range(n):            
            if clist[i][j] == 0:
                print("\033[30m\033[47m{}\033[0m" .format(a), end ="")   
            if clist[i][j] == 3:
                print("\033[30m\033[47m{}\033[0m" .format(b), end ="")
            if clist[i][j] == 2:
                print("\033[30m\033[47m{}\033[0m" .format(d), end ="")
            if clist[i][j] == 1:
                print("\033[30m\033[47m{}\033[0m" .format(c), end ="")
        print(end="\n")
        


while Cnt:
    cell_list = new_field(cell_list, N, nbrs)
    PrintCellList(cell_list, N)
    time.sleep(0.7)
    os.system('clear')
    Cnt-=1
    
    

  

            
    
