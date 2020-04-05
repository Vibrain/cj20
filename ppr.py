def fastest(start_sch, done_sch) :
    ft = min(start_sch)
    indexes = [i for i, x in enumerate(start_sch) if x == min(start_sch)]
    for idx, start_sch in enumerate(start_schstart_sch):
        if(ft == start_sch)

return fastest_idx, start_time

def solve(n):

    schedule_per_minute = [0]*1440
    tot_sch = []
    tmp_ans = []*n
    start_sch = []
    done_sch = []
    tot_task = []
    min_time = min(start_sch)
    max_time = max(done_sch)

    for m in range(n):
        sch = list(map(int, f.readline().strip().split()))
        tot_sch.append(sch)
        tot_task.append(sch)
        start_sch.append(sch[0])
        done_sch.append(sch[1])
        for j in range(sch[0], sch[1]):
            schedule_per_minute[j] = schedule_per_minute[j]+1
            if(schedule_per_minute[j] > 2):
                return "IMPOSSIBLE"

    # greedy 하게 스타트 타임 중 가장 빠른 것의 인덱스에 씨를 할당하고, 그것의 엔드타임 이상의 것 중 가장 빠른 스타트 타임의 인덱에 씨를 할당하고
    for m in range(n):
        min_time

    ans = ""

    ans = ans + 'C'
    ans = ans + 'J'

    return ans

# after test, replace all to input()
f = open("./333.txt")
T = int(f.readline().strip())
for t in range(T):
    n = int(f.readline().strip())
    ppr = solve(n)
    print('Case #{}: {}'.format(t+1,ppr))