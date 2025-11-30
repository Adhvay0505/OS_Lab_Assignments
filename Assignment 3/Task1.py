# priority scheduling (non - preemptive)
n=int(input("n: "))
bt,at,pr=[],[],[]
for i in range(n):
    b,a,p=map(int,input().split());bt+=[b];at+=[a];pr+=[p]
ct=[0]*n;done=[0]*n;t=0
for _ in range(n):
    r=[i for i in range(n) if not done[i]and at[i]<=t]
    if not r:t=min(at[i]for i in range(n)if not done[i]);continue
    i=min(r,key=lambda x:pr[x]);t+=bt[i];ct[i]=t;done[i]=1
tat=[ct[i]-at[i]for i in range(n)]
wt=[tat[i]-bt[i]for i in range(n)]
print("P\tCT\tTAT\tWT")
for i in range(n):print(f"{i+1}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
print("Avg TAT=",round(sum(tat)/n,2)," Avg WT=",round(sum(wt)/n,2))


# round robin scheduling
n=int(input("n: "))
bt,at=[],[]
for i in range(n):b,a=map(int,input().split());bt+=[b];at+=[a]
q=int(input("q: "))
r=bt[:];t=0;ct=[0]*n;Q=[]
while 1:
    for i in range(n):
        if at[i]<=t and r[i]>0 and i not in Q:Q+=[i]
    if not Q:
        if all(x==0 for x in r):break
        t+=1;continue
    i=Q.pop(0);x=min(q,r[i]);r[i]-=x;t+=x
    for j in range(n):
        if at[j]<=t and r[j]>0 and j not in Q:Q+=[j]
    if r[i]>0:Q+=[i]
    else:ct[i]=t
tat=[ct[i]-at[i]for i in range(n)]
wt=[tat[i]-bt[i]for i in range(n)]
print("P\tCT\tTAT\tWT")
for i in range(n):print(f"{i+1}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
print("Avg TAT=",round(sum(tat)/n,2)," Avg WT=",round(sum(wt)/n,2))
