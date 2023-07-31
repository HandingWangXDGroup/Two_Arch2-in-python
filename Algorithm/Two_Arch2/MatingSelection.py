import numpy as np

def MatingSelection(CA, DA, N):
    CAParent1 = np.random.randint(0, len(CA), size = int(np.ceil(N/2)))
    CAParent2 = np.random.randint(0, len(CA), size = int(np.ceil(N/2)))
    
    temp = []
    for i in range(len(CA)):
        temp.append(CA[i].obj)
    CAobj = np.vstack(temp)

    # CAobj1 = []
    # for i in CAParent1:
    #      CAobj1.append(CAobj[i,:])

    # CAobj2 = []
    # for i in CAParent2:
    #      CAobj2.append(CAobj[i,:])

    A1 = 0 + np.any(CAobj[CAParent1,:] < CAobj[CAParent2,:],axis =1)
    A2 = 0 + np.any(CAobj[CAParent1,:] > CAobj[CAParent2,:],axis =1)
    Dominate = A1 - A2


    # Dominate = np.any(CAobj[CAParent1,:] < CAobj[CAParent2,:]) - np.any(CAobj[CAParent1,:] > CAobj[CAParent2,:])
    ParentC = []
    for i in range(len(CAParent1)):
        if Dominate[i] == 1:
            ParentC.append(CA[CAParent1[i]])
        else:
            ParentC.append(CA[CAParent2[i]])
    ParentC += [DA[np.random.randint(0,len(DA))] for _ in range(int(np.ceil(N/2)))]
    ParentM = [CA[np.random.randint(0, len(CA))] for _ in range(N)]

    return ParentC, ParentM