import numpy as np
from Algorithm.NSGAII.Non_Dominated_Sort import nonDominatedSort
from scipy.spatial.distance import pdist

def UpdateDA(DA, New, MaxSize, p):
    
    ## find the non-dominated solution

  
    DA = DA+New
    N = len(DA)


    F, pop_combine_non,_= nonDominatedSort(len(DA), DA)
    DA = [DA[i] for i in F[1]]

    N = len(DA)
    if N <= MaxSize:
        return DA
    
    ## select the extreme solution first

    Choose = np.zeros(N,dtype = bool)
    Extreme1 = np.argmin([s.obj for s in DA], axis = 0)
    Extreme2 = np.argmax([s.obj for s in DA], axis = 0)
    
    Choose[Extreme1] = True
    Choose[Extreme2] = True

    if np.sum(Choose) > MaxSize:
        Choosed = np.where(Choose)[0]
        k = np.random.choice(Choosed, size = np.sum(Choose) - MaxSize, replace = False)
        Choose[k] = False
    elif np.sum(Choose) < MaxSize:
        Distance = np.full((N,N),np.inf)
        Distance1 = np.full((N,N),np.inf)
        for i in range(N-1):
            for j in range(i+1,N):
                Distance[i,j] = pdist([DA[i].obj, DA[j].obj], 'minkowski', p = p)[0]
                # Distance[i,j] = np.linalg.norm(np.vstack(DA[i].obj) - np.vstack(DA[j].obj),ord = 1)
                Distance[j,i] = Distance[i,j]
        while np.sum(Choose) < MaxSize:
            Remain = np.where(~Choose)[0]
            x = np.argmax(np.min(Distance[~Choose][:,Choose],axis =1))
            Choose[Remain[x]] = True
    DA = [DA[i] for i in range(N) if Choose[i]]

    return DA



