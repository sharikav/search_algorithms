'''
Function tri_Traversal - performs DFS, UCS and A* traversals and returns the path for each of these traversals 

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]

NOTE : you MUST have three additional functions DFS_Traversal, UCS_Traversal and A_star_Traversal for each of the above mentioned traversals (DO NOT change the names of these individual functions).
'''

def tri_Traversal(cost, heuristic, start_point, goals):
    l = []
    t3=[]
    t2=[]
    t1=[]
    t1=DFS_Traversal(cost, heuristic, start_point, goals)
    t2=UCS_Traversal(cost, heuristic, start_point, goals)
    t3=A_star_Traversal(cost, heuristic, start_point, goals)
    
    # t1 <= DFS_Traversal
    # t2 <= UCS_Traversal
    # t3 <= A_star_Traversal

    l.append(t1)
    l.append(t2)
    l.append(t3)
    return l



        
def DFS_Traversal(cost,heuristic,start_point,goals):
    stack = []
    traverse = []
    came_from = {start_point:start_point}
    stack.append(start_point)
   
    vis = [0 for i in range(len(cost))]
    while len(stack)>0:
        curr = stack.pop()
        vis[curr] = 1
        
        traverse.append(curr)
        if curr in goals:
            break
                 
        
        for j in range(len(cost)-1,0,-1):
            if(vis[j]==0 and cost[curr][j] >0 ):
                stack.append(j)
                came_from[j] = curr
                  

    j1 = curr
    path=[]
    while(j1!=came_from[j1]):
            
            path.append(j1)
            if j1 not in came_from.keys():
                break
            j1 = came_from[j1]
            
    path.append(start_point)        
        
    path.reverse()
       
    return path


def UCS_Traversal(cost, heuristic, start_point, goals):
    b={}
    for i in goals:
        if UCS_Traversal1(cost, heuristic, start_point, i) is not None:
            (a,c)=UCS_Traversal1(cost, heuristic, start_point, i)
            b[c]=a
        else :
            return None
    t=min(b.keys())
    if len(b)==0:
        return None
    return b[t]
def get_neighbors(n,cost):
    a={}
    for i in range(len(cost[0])):
       
        if cost[n][i] > 0:
            a[i]=cost[n][i]
    
        
    return a        
def A_star_Traversal(cost, heuristic, start_point, goals):
    b={}
    for i in goals:
        if A_star_Traversal1(cost, heuristic, start_point,i) is not None:
            (a,c)=(A_star_Traversal1(cost, heuristic, start_point,i))
            b[c]=a
        
    t=min(b)
    
    return b[t]

def A_star_Traversal1(cost, heuristic, start_point,d):
   
    frontier=set()
    
    
    frontier.add(start_point)
    
    explored= set()
    dist={}
    
    parents={}
    dist[start_point]=0
    parents[start_point]=start_point
   
    while len(frontier) >0:
        
        n= None
        for v in frontier:
            #print(dist[v])
            if n == None or dist[v] + heuristic[v] < dist[n] + heuristic[n]:
                n=v
                
        if n==d:
            
            pass
        else:
            
            
            for (m, weight) in get_neighbors(n,cost).items():
                if len(get_neighbors(n,cost))==0:
                    break
                if m not in frontier and m not in explored:
                    frontier.add(m)
                    parents[m]=n
                    dist[m]=dist[n]+weight
                else:
                    if dist[m] > dist[n]+ weight:
                        dist[m]=dist[n]+weight
                        parents[m]=n
                        if m in explored:
                            explored.remove(m)
                            frontier.add(m)
                            
        if n == None:
            return None
        
            
            
        if n==d:
            
            p=dist[n]
            path=[]
            while parents[n] !=n:
                path.append(n)
                n=parents[n]
            path.append(start_point)
            path.reverse()
            
            
            return (path,p)
            
        frontier.remove(n)
        
        explored.add(n)
    return None
def UCS_Traversal1(cost, heuristic, start_point, d):
   
    frontier=set()
    
    
    frontier.add(start_point)
    
    explored= set()
    dist={}
    
    parents={}
    dist[start_point]=0
    parents[start_point]=start_point
   
    while len(frontier) >0:
        
        n= None
        for v in frontier:
            
            if n == None or dist[v] < dist[n]:
                n=v
                
        if n==d:
            pass
        else:
            
            
            for (m, weight) in get_neighbors(n,cost).items():
                if len(get_neighbors(n,cost))==0:
                    break
                if m not in frontier and m not in explored:
                    frontier.add(m)
                    parents[m]=n
                    dist[m]=dist[n]+weight
                else:
                    if dist[m] > dist[n]+ weight:
                        dist[m]=dist[n]+weight
                        parents[m]=n
                        if m in explored:
                            explored.remove(m)
                            frontier.add(m)
                            
        if n == None:
            return None
        
            
            
        if n==d:
            
            p=dist[n]
            path=[]
            while parents[n] !=n:
                path.append(n)
                n=parents[n]
            path.append(start_point)
            path.reverse()
            
            
            return (path,p)
            
        frontier.remove(n)
        
        explored.add(n)
    return None
                    
                
                
                    
                
                    
                
                
                    
                
