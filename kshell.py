import networkx as nx
import numpy

def core_investigate(G):
    '''This will output an array of shell numbers of the input graph G'''
    c=nx.core_number(G) 
    d=c.values()
    d.sort()
    s=list(set(d))
    return len(s)#returns the number of shells

def experiment(n,k):
    '''This runs the experiment k times. We consider different erdos renyi graphs and compute the average number'''
    '''of shells per probability value'''
    averaged=[]
    for i in range(100):
        shells=[]
        for j in range(k):
            G=nx.erdos_renyi_graph(n,i*0.01)
            #print nx.is_connected(G)
            c=core_investigate(G)
            shells.append(c)
        averaged.append(numpy.average(shells))
        print i
    return averaged









