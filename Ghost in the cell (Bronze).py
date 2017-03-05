import sys
import math
import random

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
D = []
for i in range(link_count):
    D.append([int(j) for j in input().split()])
#print(D)
Bomb = 2
# game loop
while True:
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    E = []
    My_base = []
    Neutral = []
    Evil = []
    for i in range(entity_count):
        E.append([j for j in input().split()])
        E[i][0] = int(E[i][0]) # base id
        E[i][2] = int(E[i][2]) # 1 - my, -1 - enemy, 0 - neutral
        E[i][3] = int(E[i][3]) # number of cyborgs in the factory
        E[i][4] = int(E[i][4]) # factory production (between 0 and 3)
        E[i][5] = int(E[i][5]) # unused
        E[i][6] = int(E[i][6]) # unused
        
        if E[i][1] == "FACTORY" and E[i][2] == 1:
            My_base.append(E[i][0])


    prints = []
    for j in range(len(My_base)):
        
        if E[My_base[j]][4] == 0 and E[My_base[j]][5] == 0 and E[My_base[j]][3] >= 20:
            prints.append("INC " + str(E[My_base[j]][0]))
            
        elif len(My_base) % 2 == 1:
            for i in range(factory_count):
            
                if E[i][2] == 0 and E[i][3] >= 10 and E[i][0] != My_base[j] and D[My_base[j]][2] <= 7:
                    prints.append("MOVE " + str(My_base[j]) + " " + str(E[i][0]) + " " + str(E[i][4] + 2))
            
                elif E[i][2] == 0 and 4 < E[i][3] < 10 and E[i][0] != My_base[j] and D[My_base[j]][2] <= 7:
                    prints.append("MOVE " + str(My_base[j]) + " " + str(E[i][0]) + " " + str(E[i][4] + 2))
                
                elif E[i][2] == 0 and E[i][3] <= 4 and E[i][0] != My_base[j] and D[My_base[j]][2] <= 7:
                    prints.append("MOVE " + str(My_base[j]) + " " + str(E[i][0]) + " " + str(E[i][4] + 2))
            
        else:
            for i in range(factory_count):
                
                if E[i][2] == -1 and 15 > E[i][3] >= 5 and E[i][0] != My_base[j] and D[My_base[j]][2] <= 7:
                    prints.append("MOVE " + str(random.choice(My_base)) + " " + str(E[i][0]) + " " + str(E[i][3] + 2))
            
                elif E[i][2] == -1 and E[i][3] >= 15 and E[i][0] != My_base[j] and D[My_base[j]][2] <= 7:
                    prints.append("BOMB " + str(random.choice(My_base)) + " " + str(E[i][0]))
                    Bomb -= 1
                    if Bomb <= 0:
                        prints.append("MOVE " + str(random.choice(My_base)) + " " + str(E[i][0]) + " " + str(E[i][3] + 2))
            
                elif E[i][2] == -1 and E[i][3] <= 4 and E[i][0] != My_base[j] and D[My_base[j]][2] <= 6:
                    prints.append("MOVE " + str(random.choice(My_base)) + " " + str(E[i][0]) + " " + str(E[i][3] + 2))
            
            
                elif E[i][2] == 1 and E[i][3] >= 5 and E[i][0] != My_base[j] and D[My_base[j]][2] <= 6:
                    prints.append("MOVE " + str(My_base[j]) + " " + str(E[i][0]) + " " + str(E[i][3]//2 + 2))
            
                elif E[i][2] == 1 and E[i][3] < 5 and E[i][0] != My_base[j] and D[My_base[j]][2] <= 6:
                    prints.append("MOVE " + str(My_base[j]) + " " + str(E[i][0]) + " " + str(E[i][3] + 2))
            #    print("WAIT")
    print(";".join(prints))
    
    E.clear()
    My_base.clear()
    Neutral.clear()
    Evil.clear()
