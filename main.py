hiaracy = {'A':['B','C'],'B':['D','E'],'C':['F','G']}
value = {'A':3,'B':5,'C':4,'D':2,'E':6,'F':3,'G':7}
objective = 7

def locate(route):
    locating = 'A'
    for i in route:
        locating = hiaracy[locating][i]
    return locating

def depth_first():
    route = []
    now = 'A'
    print("탐색 : A")
    
    while True:
        if value[now] >= objective:
            return now
            break
        else:
            if now in hiaracy:
                route.append(0)
                now = locate(route)
                print("탐색 :",now)
            else:
                if route == []:
                    return "목표 상태 없음"
                    break
                a = route.pop()
                now = locate(route)
                while a + 1 >= len(hiaracy[now]):
                    a = route.pop()
                    now = locate(route)
                if a + 1 < len(hiaracy[now]):
                    route.append(a+1)
                    now = locate(route)
                    print("탐색 :",now)

def width_first():
    same_width = ['A']
    
    while True:
        before_width = []
        for i in same_width:
            print("탐색 :",i)
            if value[i] >= objective:
                return i
                break
            if i in hiaracy:
                before_width.append(i)
        same_width = []
        for i in before_width:
            same_width.extend(hiaracy[i])
    

def hill_climbing():
    now = 'A'
    print("탐색 : A")
    
    while now in hiaracy:
        maximum = hiaracy[now][0]
        for i in hiaracy[now]:
            if value[i] > value[maximum]:
                maximum = i
        if value[maximum] <= value[now]:
            break
        now = maximum
        print("탐색 :",now)
    return now

def maximum_first():
    checked = []
    accessible = ['A']
    
    while True:
        maximum = accessible[0]
        for i in accessible:
            if value[i] > value[maximum]:
                maximum = i
        print("탐색 :",maximum)
        if value[maximum] >= objective:
            return maximum
        if maximum in hiaracy:
            accessible.extend(hiaracy[maximum])
        checked.append(maximum)
        accessible.remove(maximum)

print("깊이 우선 탐색")
print("목표 상태 =",depth_first())
print("너비 우선 탐색")
print("목표 상태 =",width_first())
print("언덕 등반 탐색")
print("목표 상태 =",hill_climbing())
print("최상 우선 탐색")
print("목표 상태 =",maximum_first())
