## ALGO Exercises

graph=[[5,8],[0],[],[9],[0,7],[4],[0,3],[4],[2,7],[1,5,3]]


# Ex 3,b
def DFSall(G):
    """
    DFS traversal
    Parameters
    ----------
    G : Graph
        Adjacency List.

    Returns
    List of connected graphs
    """

    def DFS(v):
        """
        Depth First Search 
    
        Parameters
        ----------
        v : Vertex
        """
        seen[v]=True
        nonlocal clock,pre,post
        clock+=1
        pre[v]=clock
        temp=sorted(graph[v].copy())
        while len(temp)>1:
            w=temp[1]
            temp.pop(1)
            if not seen[w]:
                parent[w]=v
                DFS(w)
        if len(temp)==1:
            w=temp[0]
            if not seen[w]:
                parent[w]=v
                DFS(w)
        clock+=1
        post[v]=clock
    
    clock=0
    seen=dict()
    pre=dict()
    post=dict()
    parent=dict()
    n=len(G)
    vertices=list(range(n))
    for i in range(n):
        seen[i]=False
        parent[i]=None
    
    for i in vertices:
        if not seen[i]:
            DFS(i)
    
    return seen,parent,pre,post

seen,parent,pre,post=DFSall(graph)



def path(G,vertex1,vertex2):
    """
    To check if there is any path from vertex1 to vertex2
    ----------
    G : Graph
        Adjacency List.
    vertex1 : Vertex 1
    vertex2 : Vertex 2

    Returns
    True/False
    """
    if G[vertex1]==[]:
        return False
    elif vertex2 in G[vertex1]:
        return True
    else:
        for i in G[vertex1]:
            return path(G,i,vertex2)

def dag_check(G):
    """
    Check if any digraph is acyclic

    Parameters
    ----------
    G : List
        Adjacency List.

    Returns
     True if exists else False
    """
    cycle=False
    vertices=list(range(10))
    for i in vertices:
        cycle=path(G,i,i)
        if cycle:
            return "Not A directed Acyclic Graph"
    return "A directed Acyclic Graph"
            

digraph=[[1,2],[2],[],[0,4,9,8],[0],[0,6],[],[5,8,9],[0,1,2,4,9],[4,6]]
dag_check(digraph)
    
    
# Exercise 11:      Incomplete
def check_arc_type(G):
    """
    Categorising Arc type into tree,forward,back and cross

    Parameters
    ----------
    G : Adjacency List
        Graph.
    fixed : Fixed arc (u--->v)

    Returns
    Dictionary of arcs categorised
    """
    n=len(G)
    vertices=list(range(n))
    
    tree=dict() # When DFS(u) is invoked, v is new and dfs(u) calls dfs(v),then u ---> v is called tree edge
    forward=dict() # When DFS(u) is invoked, v is new and dfs(u) doesn't call dfs(v),then u ---> v is called forward edge
    back=dict() # v is active when DFS(u) is invoked, then u ---> v is called back edge
    cross=dict() # v is finished when DFS(u) is invoked, then u---> v is called cross edge
    
    for i in range(n):
        seen[i]=False
        
    for i in vertices:
        if not seen[i]:
            DFS(i)
    
    
    



































