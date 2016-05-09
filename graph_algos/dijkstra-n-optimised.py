import random
def rndmat(n,d):
    #generates random connection matrix with integer entries in range d and dimension n
    M=[]
    for p in range(n):
        row=[]
        for i in range(n):
            row.append(random.randrange(d))
        M.append(row)
    for i in range(n):
        for j in range(i+1):
            M[j][i]=M[i][j]
            if i==j:
                M[i][j]=0
                
    return M                
    
#M=[[0,100000,2,0,0,0],[100000,0,0,2,0,0.0000000001],[2,0,0,0,0,3],[0,2,0,0,2,0],[0,0,0,2,0,3],[0,0.0000000001,3,0,3,0]]
#M is connection matrix with entries= distances b/w adjacent vertices
#M=rndmat(20,50)

INF=9999999999
UNDEF=len(M) +1
n=len(M)

def dist(m,n): return M[m][n]
#dist b/w adj vertices

def mpl(s,M):
    #min path length from source to all vertices
    
    V=[] #list of vertices
    for i in range(n):
        V.append(['white',INF,UNDEF])
    #white= unvisited, red = visited.
    #2nd arg is current known shortest dist from start. initializes to infinity
    #3rd arg is previous vertex in shortest path

    V[s]=['white',0,s] #dist from s to s =0

    while True:
        cont=0#decides whether to continue search
        for i in range(n):
            if V[i][0]=='white': 
                cont=1 # continue only if there are white/unexplored vertices
                break

        if cont==0: #exit while loop if there are no white vertices
            break


        mindist=INF # dist of closest white vert from s. initialize to inf
        u=s #current vertex. initialize to source
        for i in range(n): # closest vertex
                if (V[i][0]=='white') & (V[i][1]<mindist):
                    mindist=V[i][1]
                    u=i #make current vertex the closest unexplored vertex
        #print 'mindist', mindist
        #print 'u',u
        
        V[u][0]='red' #set current vertex to red

        for j in range(0,n): #going through unexplored neighbours of current vert ie u
            #print "j", j
            #print "M[u][j]", M[u][j]
            if (M[u][j]!=0) & (V[j][0]=='white'):           
                    alt= V[u][1] + dist(u,j)
                    if alt< V[j][1]:
                        V[j][1] = alt
                        V[j][2] = u

    return(V)


def mplmatrix(M):
    D=[]
    for i in range(len(M)):
        D.append(mpl(i,M))
    return D


def shortest_path(start,end,matrix):
    #returns shortest path from start to end using connection matrix
    mpls=mpl(start,matrix)
    curr=end#current vertex
    path=[]#shortest path
    while curr != start:
        print 'a'
        path.insert(0,curr)
        curr=mpls[curr][2]
        print 'b'
    path.insert(0,start)
    return path
    
    
    
