#MATRIX TOOL
#
#determinant, inverse, square, product of two matrices
#
#
#
print("=====MATRIX TOOL=====")

#demande des coordonnées de la matrice
print("Column count [a]?...")
a = int(input())
print("Lign count [b]?...")
b = int(input())

mat= [[1,2,3],[4,5,6],[7,8,9]]

for j in range(0,a) :
    sub_mat = []
    for i in range(0,b):
        sub_mat.append(i)
    mat.append(sub_mat)

if a == b :
    print("Calcul du déterminant")

    #initialisation du déterminant et du sous-déterminant
    det = 1
    sub_det = 1

    for j in range(0,b):
        for i in range(0,a) :
            sub_det = mat[j][i]

print(mat)