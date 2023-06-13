def TowerOfHanoi(n,source,destination,intermediate):
    if(n==1):
        print("Move disk 1 from pole ",source, " to " ,destination)
        return
    
    TowerOfHanoi(n-1, source,intermediate,destination)
    print("Move disk ",n, "from pole ", source, " to ", destination)
    TowerOfHanoi(n-1,intermediate,destination,source)


n=3
TowerOfHanoi(n,'A','C','B')