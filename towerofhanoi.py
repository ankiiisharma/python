def TowerOfHanoi(n, source, destionation, intermediate):
    if(n==1):
        print("Move 1 from",source, "to",destionation)
        return
    TowerOfHanoi(n-1,source,intermediate,destionation)
    print("Move ",n,"from",source, "to", destionation )
    TowerOfHanoi(n-1,intermediate,destionation,source)

n=3
TowerOfHanoi(n,'A','C','B')