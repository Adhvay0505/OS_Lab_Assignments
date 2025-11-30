def allocate(blocks, procs, strat):
    b_used=[False]*len(blocks)
    for i,p in enumerate(procs):
        idx=None
        if strat=='first':
            for j,b in enumerate(blocks):
                if not b_used[j] and b>=p: idx=j; break
        elif strat=='best':
            idx=min((j for j in range(len(blocks)) if not b_used[j] and blocks[j]>=p),key=lambda j:blocks[j],default=None)
        else:
            idx=max((j for j in range(len(blocks)) if not b_used[j] and blocks[j]>=p),key=lambda j:blocks[j],default=None)
        if idx is not None:
            b_used[idx]=True
            print(f"P{i+1}({p}) → Block{idx+1} ({blocks[idx]-p} internal frag)")
        else:
            print(f"P{i+1}({p}) → Not Allocated")

blocks=list(map(int,input("Enter memory block sizes: ").split()))

procs=list(map(int,input("Enter process sizes: ").split()))

s=input("Strategy (first/best/worst): ").lower()

allocate(blocks,procs,s)
