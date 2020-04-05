def solve(n):

    return k, r, c

# after test, replace all to input()
#f = open("./111.txt")
T = int(input().strip())
for t in range(T):
    n = int(input().strip())
    k,r,c = solve(n)
    print('Case #{}: {} {} {}'.format(t+1,k,r,c))