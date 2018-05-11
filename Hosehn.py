labels = [];
n_labels = 0; # length of the labels array

# https://gist.github.com/tobin/909424


# uf_intitialize sets up the data structures needed by the union-find implementation.
def uf_initialize(max_labels):
    global  n_labels, labels
    n_labels = max_labels
    labels = [0 for x in range(0,max_labels)]

def uf_find(x):
    y = x
    while (labels[y] != y):
        y = labels[y]
    while (labels[x] != x):
        z = labels[x]
        labels[x] = y
        x = z
    return y

# uf_union joins two equivalence classes and returns the canonical label of the resulting class.
def uf_union( x,  y):
    labels[uf_find(x)] = uf_find(y)
    return labels[uf_find(x)]

# uf_make_set creates a new equivalence class and returns its label

def uf_make_set():
  labels[0] +=1
  labels[labels[0]] = labels[0]
  return labels[0]

# *  uf_done frees the memory used by the union-find data structures */
def uf_done(void):
    global n_labels, labels
    n_labels = 0
    labels = 0

# print_matrix prints out a matrix that is set up in the "pointer to pointers" scheme
# (aka, an array of arrays); this is incompatible with C's usual representation of 2D
# arrays, but allows for 2D arrays with dimensions determined at run-time */

def print_matrix(matrix, m, n):
    for lista in matrix:
        for elemento in lista:
          print("%3d ".format(elemento))
        print("\n")


#Label the clusters in "matrix".  Return the total number of clusters found.

def hoshen_kopelman(matrix, m, n):
    uf_initialize(m * n / 2)
    for index_x,lista in enumerate(matrix):
        for index_y,elemento in enumerate(lista):
            if elemento!=0: #if occupied ...
            	up = 0
            	if index_x!=0: #  look up
                    up = matrix[index_x-1][index_y]

            	left = 0
                if index_y == 0:#look left
                    left = matrix[index_x][index_y-1]
            if (up + left==0):
                elemento = uf_make_set()#a new cluster
                break
            if (up + left==1):
                elemento = max(up,left)
                break
            if 	(up + left==2):
                elemento = uf_union(up, left)
                break

#  /* apply the relabeling to the matrix */
# /* This is a little bit sneaky.. we create a mapping from the canonical labels
#    determined by union/find into a new set of canonical labels, which are
#    guaranteed to be sequential. */


    new_labels = [0 for x in range(0, n_labels)]#allocate array, initialized to zero
    for index_x,lista in enumerate(matrix):
        for index_y, elemento in enumerate(lista):
            if elemento!=0:
                x = uf_find(elemento)
	        if new_labels[index_x] == 0:
                    new_labels[0]+=1
                    new_labels[index_x] = new_labels[0]
            elemento = new_labels[index_x]
    total_clusters = new_labels[0]
    uf_done()
    return total_clusters


#This procedure checks to see that any occupied neighbors of an occupied site
#   have the same label. */

def check_labelling(matrix, m, n):
    N=0
    S=0
    E=0
    W=0
    for index_x, lista in enumerate(matrix):
        for index_y, elemento in enumerate(lista):
            if elemento!=0:
                if index_x!=0:
                    N = matrix[index_x-1][index_y]
                else:
                    N = 0
                if index_x == m-1:
                    S = matrix[index_x+1][index_y]
                else:
                    S= 0
                if index_y!=n-1:
                    E = matrix[index_x][index_y+1]
                else:
                    E = 0
                if index_y != 0:
                    W = matrix[index_x][index_y-1]
                else:
                    W=0
