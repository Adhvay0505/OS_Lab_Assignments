## mft
parts=list(map(int,input("Enter partition sizes: ").split()))
procs=list(map(int,input("Enter process sizes: ").split()))
used=[0]*len(parts)
for i,p in enumerate(procs):
    idx=None
    for j in range(len(parts)):
        if not used[j] and parts[j]>=p:
            idx=j; used[j]=1; break
    if idx is not None:
        print(f"P{i+1}({p}) → Partition{idx+1} (Internal Frag={parts[idx]-p})")
    else:
        print(f"P{i+1}({p}) → Not Allocated")

##mvt
mem=int(input("Enter total memory size: "))
free=[(0,mem)]
allocs={}
while True:
    cmd=input("cmd (alloc/free/state/exit): ").split()
    if not cmd: continue
    if cmd[0]=='alloc':
        name,sz=cmd[1],int(cmd[2])
        for i,(s,l) in enumerate(free):
            if l>=sz:
                allocs[name]=(s,sz)
                del free[i]
                if l>sz: free.insert(i,(s+sz,l-sz))
                print(f"{name} allocated at {s}")
                break
        else: print("Not enough space")
    elif cmd[0]=='free':
        if cmd[1] in allocs:
            s,sz=allocs.pop(cmd[1])
            free.append((s,sz))
            free=sorted(free,key=lambda x:x[0])
            merged=[]
            for a,b in free:
                if not merged: merged.append((a,b))
                else:
                    pa,pb=merged[-1]
                    if pa+pb==a: merged[-1]=(pa,pb+b)
                    else: merged.append((a,b))
            free=merged
            print(f"{cmd[1]} freed")
        else: print("Process not found")
    elif cmd[0]=='state':
        print("Allocated:",allocs)
        print("Free:",free)
    elif cmd[0]=='exit': break
