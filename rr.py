# Round Robin CPU Scheduling
n = int(input("Enter number of processes :"))
p = []
for i in range(n):
    at = int(input(f"Enter arrival time for P{i+1}:"))
    bt = int(input(f"Enter burst time for P{i+1}:"))
    p.append([f"P{i+1}", at, bt, bt])
tq = int(input("Enter TimeQuant:"))
t = 0
q = []
done = 0
rq = [False] * n
ct = [0] * n
tat = [0] * n
wt = [0] * n

p.sort(key=lambda x: x[1])
q.append(0)
rq[0] = True
t = p[0][1]
while done < n:
    if q:
        i = q.pop(0)
        if p[i][3] > tq:
            t += tq
            p[i][3] -= tq
        else:
            t += p[i][3]
            p[i][3] = 0
            ct[i] = t
            tat[i] = ct[i] - p[i][1]
            wt[i] = tat[i] - p[i][2]
            done += 1
        for j in range(n):
            if not rq[j] and p[j][1] <= t:
                q.append(j)
                rq[j] = True
        if p[i][3] > 0:
            q.append(i)
    else:
        for j in range(n):
            if not rq[j]:
                q.append(j)
                rq[j] = True
                t = p[j][1]
                break
print("\nProcess\tArrival\tBurst\tCompletion\tTurnaround\tWait")
tw = 0
for i in range(n):
    print(f"{p[i][0]}\t{p[i][1]}\t{p[i][2]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
    tw += wt[i]
print(f"\nAverage Wait Time: {tw/n}")
