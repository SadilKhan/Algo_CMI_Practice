## ALGO Exercises

graph=[[5,8],[0],[],[9],[0,7],[4],[0,3],[4],[2,7],[1,5,3]]


# Ex 3,b
def DFSall(G,types):
    """
    DFS traversal
    Parameters
    ----------
    G : Graph
        Adjacency List.
    types: 0 if smallest element is to be chosen
            1 if second smallest element is to be chosen

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
        temp=sorted(G[v].copy())
        while len(temp)>1:
            w=temp[types]
            temp.pop(types)
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
    print(vertices)
    for i in range(n):
        seen[i]=False
        parent[i]=None
    
    for i in vertices:
        if not seen[i]:
            DFS(i)
    
    return seen,parent,pre,post

seen,parent,pre,post=DFSall(graph,1)



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
def check_arc_type(G,types):
    """
    Categorising Arc type into tree,forward,back and cross for DFS Type 1

    Parameters
    ----------
        Graph.
    types: 0 if smallest el
    G : Adjacency Listement is to be chosen
            1 if second smallest element is to be chosen
    Returns
    Dictionary of arcs categorised
    """
    n=len(G)
    vertices=list(range(n))
    
    tree=[] # When DFS(u) is invoked, v is new and dfs(u) calls dfs(v),then u ---> v is called tree edge
    forward=[] # When DFS(u) is invoked, v is new and dfs(u) doesn't call dfs(v),then u ---> v is called forward edge
    back=[] # v is active when DFS(u) is invoked, then u ---> v is called back edge
    cross=[] # v is finished when DFS(u) is invoked, then u---> v is called cross edge
    seen=dict()
    _,_,pre,post=DFSall(G,types)
    
    for i in vertices:
        for j in vertices:
            if i!=j:
                if post[i]<pre[j]:
                    if i in G[j]:
                        cross.append((j,i))
                if pre[i]+1<pre[j] and post[i]>post[j]:
                    back.append((i,j))
    
    
    def DFS_modified(vertex):
        """
        Standard DFS Traversal with a slight 
        modification of adding edges to lists.
        
        Parameters
        ----------
        vertex : An integer
            Vertex of a Graph

        Returns
       List of reachable vertors
       """
        seen[vertex]=True
        for i in G[vertex]:
            if not seen[i]:
                tree.append((vertex,i))
                if vertex in G[i]:
                    back.append((i,vertex))
    
    for i in range(n):
        seen[i]=False
        
    for i in vertices:
        if not seen[i]:
            DFS_modified(i)
    
    return tree,back,cross,back
    
    
digraph=[[1,2],[2],[],[0,4,9,8],[0],[0,6],[],[5,8,9],[0,1,2,4,9],[4,6]]
di=[[1,2],[0],[1]]
check_arc_type(di,0)



























