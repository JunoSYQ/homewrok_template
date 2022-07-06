def Radom(list,n):
    A = 2
    B = 5
    seed = random.randint(0, 10)
    M = 101
    list[0] = (A*seed+B) % M
    for i in range(n-1):
        list[i+1] = (A*list[i]+B) % M
