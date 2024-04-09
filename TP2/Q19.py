import numpy as np

matrice = np.array([[None,1,None,5,2], [None, 8, 1, 1, None]])
index_ele_notnull = np.argwhere(matrice!=None)

print(matrice)
print("")
print(index_ele_notnull)