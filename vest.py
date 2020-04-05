def solve(N):
    M = []
    k, r, c = 0, 0, 0
    for i in range(N):
        M.append(list(map(int, input().split())))
        k = k + M[i][i]
    for i in range(N):
        for j1 in range(N):
            loop_flag = True
            for j2 in range(N):
                if (j1 < j2):
                    if (M[i][j1] == M[i][j2]):
                        r = r + 1
                        loop_flag = False
                        break
            if (loop_flag == False):
                break

    for i in range(N):
        for j1 in range(N):
            loop_flag = True
            for j2 in range(N):
                if (j1 < j2) :
                    if(M[j1][i] == M[j2][i]) :
                        c = c + 1
                        loop_flag = False
                        break
            if (loop_flag == False):
                break

    return k, r, c

# after test, replace all to input()
#f = open("./111.txt")
T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    k,r,c = solve(N)
    print('Case #{}: {} {} {}'.format(t+1,k,r,c))