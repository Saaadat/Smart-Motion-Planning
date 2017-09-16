from trial import *
import numpy as np
import operator
import random

class robot:

    def __init__(self, x, y, route, status):
        self.x = x
        self.y = y
        self.route = route
        self.status = status

def route2coord(x1,y1,x2,y2,route):
    start = x1 + 10*y1
    end = x2 + 10*y2
    coord=[]
    coord.append(start)
    for i in range(len(route)-1):
        if route[i] == 0:
            coord.append(coord[i]+1)
        elif route[i] == 1:
            coord.append(coord[i]+10)
        elif route[i] == 2:
            coord.append(coord[i]-1)
        elif route[i] == 3:
            coord.append(coord[i]-10)
    coord.append(end)
    return coord

def str2int(route):
    route_ = []
    for i in range(len(route)):
        if route[i] == '0':
            route_.append(0)
        elif route[i] == '1':
            route_.append(1)
        elif route[i] == '2':
            route_.append(2)
        elif route[i] == '3':
            route_.append(3)
    return route_

x =[]
y = []
location = []
endPoint = [9,19,29,39,49,59,69,79,89,99]
freeBot=['mr1','mr2','mr3','mr4','mr5','mr6','mr7','mr8','mr9','mr10']
usedBot=[]

for i in range(10):
    num = random.randrange(0,9)
    x.append(num)

for i in range(10):
    num2 = random.randrange(0,9)
    y.append(num2)
    
#for i in range(5):
    #randx = random.randrange(0,9)
    #randy = random.randrange(0,9)
    #location.append((randx,randy))

location = [(9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)]

print(x,y)
    
mr1 = robot(x[0],y[0], [], False)
mr2 = robot(x[1],y[1], [], False)
mr3 = robot(x[2],y[2], [], False)
mr4 = robot(x[3],y[3], [], False)
mr5 = robot(x[4],y[4], [], False)
mr6 = robot(x[5],y[5], [], False)
mr7 = robot(x[6],y[6], [], False)
mr8 = robot(x[7],y[7], [], False)
mr9 = robot(x[8],y[8], [], False)
mr10 = robot(x[9],y[9], [], False)

all_route = []

ob     = [[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]

print(location)

route1 = pathFind(ob, n, m, dirs, dx, dy, mr1.x, mr1.y, location[0][0], int(location[0][1]))
route2 = pathFind(ob, n, m, dirs, dx, dy, mr2.x, mr2.y, location[0][0], int(location[0][1]))
route3 = pathFind(ob, n, m, dirs, dx, dy, mr3.x, mr3.y, location[0][0], int(location[0][1]))
route4 = pathFind(ob, n, m, dirs, dx, dy, mr4.x, mr4.y, location[0][0], int(location[0][1]))
route5 = pathFind(ob, n, m, dirs, dx, dy, mr5.x, mr5.y, location[0][0], int(location[0][1]))
route6 = pathFind(ob, n, m, dirs, dx, dy, mr6.x, mr6.y, location[0][0], int(location[0][1]))
route7 = pathFind(ob, n, m, dirs, dx, dy, mr7.x, mr7.y, location[0][0], int(location[0][1]))
route8 = pathFind(ob, n, m, dirs, dx, dy, mr8.x, mr8.y, location[0][0], int(location[0][1]))
route9 = pathFind(ob, n, m, dirs, dx, dy, mr9.x, mr9.y, location[0][0], int(location[0][1]))
route10 = pathFind(ob, n, m, dirs, dx, dy, mr10.x, mr10.y, location[0][0], int(location[0][1]))

if len(route1) <= len(route2) and len(route1) <= len(route3) and len(route1) <= len(route4) and len(route1) <= len(route5) and len(route1) <= len(route6) and len(route1) <= len(route7) and len(route1) <= len(route8) and len(route1) <= len(route9) and len(route1) <= len(route10):
    #freeBot.pop(0)
    usedBot.append('mr1')
    mr1.status = True
    route1 = str2int(route1)
    mr1.route = route2coord(mr1.x,mr1.y,location[0][0],location[0][1],route1)
    all_route.append(mr1.route)

elif len(route2) <= len(route1) and len(route2) <= len(route3) and len(route2) <= len(route4) and len(route2) <= len(route5) and len(route2) <= len(route6) and len(route2) <= len(route7) and len(route2) <= len(route8) and len(route2) <= len(route9) and len(route2) <= len(route10):
    #freeBot.pop(1)
    usedBot.append('mr2')
    mr2.status = True
    route2 = str2int(route2)
    mr2.route = route2coord(mr2.x,mr2.y,location[0][0],location[0][1],route2)
    all_route.append(mr2.route)
    
elif len(route3) <= len(route1) and len(route3) <= len(route2) and len(route3) <= len(route4) and len(route3) <= len(route5) and len(route3) <= len(route6) and len(route3) <= len(route7) and len(route3) <= len(route8) and len(route3) <= len(route9) and len(route3) <= len(route10):
    #freeBot.pop(2)
    usedBot.append('mr3')
    mr3.status = True
    route3 = str2int(route3)
    mr3.route = route2coord(mr3.x,mr3.y,location[0][0],location[0][1],route3)
    all_route.append(mr3.route)
    
elif len(route4) <= len(route1) and len(route4) <= len(route2) and len(route4) <= len(route3) and len(route4) <= len(route5) and len(route4) <= len(route6) and len(route4) <= len(route7) and len(route4) <= len(route8) and len(route4) <= len(route9) and len(route4) <= len(route10):
    #freeBot.pop(3)
    usedBot.append('mr4')
    mr4.status = True
    route4 = str2int(route4)
    mr4.route = route2coord(mr4.x,mr4.y,location[0][0],location[0][1],route4)
    all_route.append(mr4.route)
    
elif len(route5) <= len(route1) and len(route5) <= len(route2) and len(route5) <= len(route3) and len(route5) <= len(route4) and len(route5) <= len(route6) and len(route5) <= len(route7) and len(route5) <= len(route8) and len(route5) <= len(route9) and len(route5) <= len(route10):
    #freeBot.pop(4)
    usedBot.append('mr5')
    mr5.status = True
    route5 = str2int(route5)
    mr5.route = route2coord(mr5.x,mr5.y,location[0][0],location[0][1],route5)
    all_route.append(mr5.route)
###########################################################################################################################################
elif len(route6) <= len(route1):
    usedBot.append('mr6')
    mr6.status = True
    route6 = str2int(route6)
    mr6.route = route2coord(mr6.x,mr6.y,location[0][0],location[0][1],route6)
    all_route.append(mr6.route)

if 1 == 1:

    for i in range(1,5):
        if mr1.status == False:
            route1 = pathFind(ob, n, m, dirs, dx, dy, mr1.x, mr1.y, location[i][0], int(location[i][1]))
        else:
            route1 = [0]*20
        if mr2.status == False:
            route2 = pathFind(ob, n, m, dirs, dx, dy, mr2.x, mr2.y, location[i][0], int(location[i][1]))
        else:
            route2 = [0]*20
        if mr3.status == False:    
            route3 = pathFind(ob, n, m, dirs, dx, dy, mr3.x, mr3.y, location[i][0], int(location[i][1]))
        else:
            route3 = [0]*20
        if mr4.status == False:
            route4 = pathFind(ob, n, m, dirs, dx, dy, mr4.x, mr4.y, location[i][0], int(location[i][1]))
        else:
            route4 = [0]*20
        if mr5.status == False:
            route5 = pathFind(ob, n, m, dirs, dx, dy, mr5.x, mr5.y, location[i][0], int(location[i][1]))
        else:
            route5 = [0]*20

        if len(route1) <= len(route2) and len(route1) <= len(route3) and len(route1) <= len(route4) and len(route1) <= len(route5) and mr1.status == False:
            #freeBot.pop(0)
            list_1 = []
            for j in range(len(route1)):
                if route1[j] == route2[j] and mr2.status == True:
                    list_1.append(route1[j])
                elif route1[j] == route3[j] and mr3.status == True:
                    list_1.append(route1[j])
                elif route1[j] == route4[j] and mr4.status == True:
                    list_1.append(route1[j])
                elif route1[j] == route5[j] and mr5.status == True:
                    list_1.append(route1[j])

            if len(list_1) <=3 :
                usedBot.append('mr1')
                mr1.status = True
                route1 = str2int(route1)
                mr1.route = route2coord(mr1.x,mr1.y,location[i][0],location[i][1],route1)
                all_route.append(mr1.route)
            else:
                pass
        elif len(route2) <= len(route1) and len(route2) <= len(route3) and len(route2) <= len(route4) and len(route2) <= len(route5) and mr2.status == False:
            #freeBot.pop(1)
            list_2 = []
            for j in range(len(route2)):
                if route2[j] == route1[j] and mr1.status == True:
                    list_2.append(route2[j])
                elif route2[j] == route3[j] and mr3.status == True:
                    list_2.append(route2[j])
                elif route2[j] == route4[j] and mr4.status == True:
                    list_2.append(route2[j])
                elif route2[j] == route5[j] and mr5.status == True:
                    list_2.append(route2[j])
                
            if len(list_2) <= 3:
                usedBot.append('mr2')
                mr2.status = True
                route2 = str2int(route2)
                mr2.route = route2coord(mr2.x,mr2.y,location[i][0],location[i][1],route2)
                all_route.append(mr2.route)
            else:
                pass
            
        elif len(route3) <= len(route1) and len(route3) <= len(route2) and len(route3) <= len(route4) and len(route3) <= len(route5) and mr3.status == False:
            #freeBot.pop(2)
            list_3 = []
            for j in range(len(route3)):
                if route3[j] == route1[j] and mr1.status == True:
                    list_3.append(route3[j])
                elif route3[j] == route2[j] and mr2.status == True:
                    list_3.append(route3[j])
                elif route3[j] == route4[j] and mr4.status == True:
                    list_3.append(route3[j])
                elif route3[j] == route5[j] and mr5.status == True:
                    list_3.append(route3[j])
                    
            if len(list_3) <= 3:
                usedBot.append('mr3')
                mr3.status = True
                route3 = str2int(route3)
                mr3.route = route2coord(mr3.x,mr3.y,location[i][0],location[i][1],route3)
                all_route.append(mr3.route)
            else:
                pass
            
        elif len(route4) <= len(route1) and len(route4) <= len(route2) and len(route4) <= len(route3) and len(route4) <= len(route5) and mr4.status == False:
            #freeBot.pop(3)
            list_4 = []
            for j in range(len(route4)):
                if route4[j] == route1[j] and mr1.status == True:
                    list_4.append(route4[j])
                elif route4[j] == route2[j] and mr2.status == True:
                    list_4.append(route4[j])
                elif route4[j] == route3[j] and mr3.status == True:
                    list_4.append(route4[j])
                elif route4[j] == route5[j] and mr5.status == True:
                    list_4.append(route4[j])
                
            if len(list_4) <= 3:
                usedBot.append('mr4')
                mr4.status = True
                route4 = str2int(route4)
                mr4.route = route2coord(mr4.x,mr4.y,location[i][0],location[i][1],route4)
                all_route.append(mr4.route)
            else:
                pass
                
        elif len(route5) <= len(route1) and len(route5) <= len(route2) and len(route5) <= len(route3) and len(route5) <= len(route4) and mr5.status == False:
            #freeBot.pop(4)
            list_5 = []
            for j in range(len(route5)):
                if route5[j] == route1[j] and mr1.status == True:
                    list_5.append(route5[j])
                elif route5[j] == route2[j] and mr2.status == True:
                    list_5.append(route5[j])
                elif route5[j] == route3[j] and mr3.status == True:
                    list_5.append(route5[j])
                elif route5[j] == route4[j] and mr4.status == True:
                    list_5.append(route5[j])

            if len(list_5) <=3:
                usedBot.append('mr5')
                mr5.status = True
                route5 = str2int(route5)
                mr5.route = route2coord(mr5.x,mr5.y,location[i][0],location[i][1],route5)
                all_route.append(mr5.route)
            else:
                pass

        print(i)

print(mr1.route,mr2.route,mr3.route,mr4.route,mr5.route)

print(usedBot)
