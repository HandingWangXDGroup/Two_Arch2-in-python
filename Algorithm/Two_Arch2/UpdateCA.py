import numpy as np


def UpdateCA(CA,New,MaxSize):

    CA = CA+New
    N = len(CA)
    if N <= MaxSize:
        return CA
    temp = []
    kappa =0.05
 

    for i in range(len(CA)):
        temp.append(CA[i].obj)
    popObj = np.vstack(temp)

    minObj = np.min(popObj,0)
    minObj = np.tile(minObj,(N,1))
    maxObj = np.max(popObj,0)
    maxObj = np.tile(maxObj,(N,1))

     #Normalization
    popObj = (popObj-minObj)/(maxObj-minObj)
    I = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            I[i][j] = np.max(popObj[i,:]-popObj[j,:])

    C = np.max(np.abs(I))
    C = np.tile(C,(N,N))
    fitness = np.exp(-I/C/kappa)
    F= np.sum(np.exp(-I/C/kappa),0)+1

    
    Choose = list(range(N))

    while len(Choose) > MaxSize:
        x = np.argmin(F[Choose])
        F = F + np.exp(-I[Choose[x],:]/ C[Choose[x]]/kappa)
        Choose.pop(x)
        
    CA = [CA[i] for i in Choose]

    return CA