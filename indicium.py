def solve(n, k):
    flg = False
    mrx = []
    flg_check = [[],[],[2,4],[3,6,9],[4,6,7,8,9,10,11,12,13,14,16],[5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25]]
    if(n == 2):
        if(k == 2):
            flg = True
            mrx = [[1, 2], [2, 1]]
        elif(k == 4):
            flg = True
            mrx = [[2, 1], [1, 2]]
    elif(n == 3):
        if (k == 3):
            flg = True
            mrx = [[1, 3, 2], [2, 1, 3], [3, 2, 1]]
        elif (k == 6):
            flg = True
            mrx = [[2, 1, 3], [3, 2, 1], [1, 3, 2]]
        elif (k == 9):
            flg = True
            mrx = [[3, 2, 1], [1, 3, 2], [2, 1, 3]]

    elif(n == 4):
        if (k == 4):
            flg = True
            mrx = [[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]]
        elif (k == 8):
            flg = True
            mrx = [[2, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
        elif (k == 12):
            flg = True
            mrx = [[3, 4, 1, 2], [2, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 3]]
        elif (k == 16):
            flg = True
            mrx = [[4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1], [1, 2, 3, 4]]
        elif (k == 7):
            flg = True
            mrx = [[1, 2, 3, 4], [3, 1, 4, 2], [4, 3, 2, 1], [2, 4, 1, 3]]
        elif (k == 9):
            flg = True
            mrx = [[2, 4, 1, 3], [1, 2, 3, 4], [3, 1, 4, 2], [4, 3, 2, 1]]
        elif (k == 11):
            flg = True
            mrx = [[3, 1, 4, 2], [4, 3, 2, 1], [2, 4, 1, 3], [1, 2, 3, 4]]
        elif (k == 13):
            flg = True
            mrx = [[4, 3, 2, 1], [2, 4, 1, 3], [1, 2, 3, 4], [3, 1, 4, 2]]
        elif (k == 6):
            flg = True
            mrx = [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 2, 1], [4, 3, 1, 2]]
        elif (k == 10):
            flg = True
            mrx = [[2, 3, 4, 1], [3, 2, 1, 4], [4, 1, 3, 2], [1, 4, 2, 3]]
        elif (k == 14):
            flg = True
            mrx = [[3, 4, 1, 2], [4, 3, 2, 1], [1, 2, 4, 3], [2, 1, 3, 4]]

    elif(n == 5):
        if(k % 5 == 0):
            pp = [1, 2, 3, 4, 5]
            for m in [1, 2, 3, 4, 5]:
                if(k == 5*m):
                    flg = True
                    pp.pop(m-1)
                    mrx = [[m,pp[0],pp[1],pp[2],pp[3]],[pp[3],m,pp[0],pp[1],pp[2]],[pp[2],pp[3],m,pp[0],pp[1]],[pp[1],pp[2],pp[3],m,pp[0]],[pp[0],pp[1],pp[2],pp[3],m]]
        elif(k in flg_check[5]):
            pp = [1, 2, 3, 4, 5]
           # print("pp is", pp)
            for m in [1, 2, 3, 4, 5]:
                for n in [1, 2, 3, 4, 5]:
                    if(k == 3*m+2*n and flg == False):
                        flg = True
                        if(m < n):
                            pp.pop(n-1)
                            pp.pop(m-1)
                        elif(m > n):
                            pp.pop(m-1)
                            pp.pop(n-1)
                        mrx = [[m,n,pp[0],pp[1],pp[2]],[pp[2],m,n,pp[0],pp[1]],[n,pp[1],m,pp[2],pp[0]],[pp[0],pp[2],pp[1],n,m],[pp[1],pp[0],pp[2],m,n]]

    if(flg == True):
        flag = "POSSIBLE"
    elif(flg == False):
        flag = "IMPOSSIBLE"
    return flag, mrx

# after test, replace all to f.readline()
f = open("./555.txt")
T = int(f.readline().strip())
for t in range(T):
    st = list(map(int, f.readline().strip().split()))
    n = st[0]
    k = st[1]
    flag,mrx = solve(n, k)
    print('Case #{}: {}'.format(t+1,flag))
    for i in range(len(mrx)):  # 세로 크기
        for j in range(len(mrx[i])):  # 가로 크기
            print(mrx[i][j], end=' ')
        print()