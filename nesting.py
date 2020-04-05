def solve_binary(s, num):
    ss = ""
    cnt = 0
    if(num == 1):
        return "("+s+")"
    p_notclosed = False
    for idx, char in enumerate(list(s)):
       # print(idx, char)
        if(char == '(' or char == ')'):
            ss = ss + char
        elif(int(char) >= 1):
            if(p_notclosed == False):
                if (cnt == num - 1):
                    ss= ss+'(' + char + ')'
                else:
                    ss= ss+'('+char
                    p_notclosed = True
                    cnt = cnt + 1

            elif(p_notclosed == True):
                if (cnt == num - 1):
                    ss= ss+char + ')'
                    p_notclosed = False
                else:
                    ss= ss+char
                    cnt = cnt + 1

        elif(int(char) == 0):
            if(p_notclosed == True):
                ss= ss+')'+char
                p_notclosed = False
            else:
                ss= ss+char
            cnt = cnt + 1
        else:
            print("what is this input?")

    return ss

def solve(s):
    tmp_ans = s
    si = [int(char) for char in s]
    n = max(si)
    #print("n is", n)
    if(n == 0):
        return solve_binary(s, len(s))

    for i in range(n):
        li = list(solve_binary(tmp_ans, len(s)))
        for idx, cr in enumerate(li):
            if(cr == '(' or cr == ')'):
                li[idx] = li[idx]
            elif(int(cr)>=1):
                li[idx] = int(cr)-1
     #   print("li is", li)
        tmp_ans = ''.join([str(j) for j in li])
     #   print("tmp_ans is ", tmp_ans)

    tmp_ans2 = list(tmp_ans)
    cnt_k = 0
    for idx,cr in enumerate(tmp_ans2):
        if (cr == '(' or cr == ')'):
             cnt_k = cnt_k
        elif (int(cr) >= 0):
             tmp_ans2[idx] = si[cnt_k]
             cnt_k = cnt_k+1
    return ''.join([str(j) for j in tmp_ans2])


# after test, replace all to open()
#f = open("./222.txt")
T = int(input().strip())
for t in range(T):
    s = input().strip()
    ps = solve(s)
    print('Case #{}: {}'.format(t+1,ps))