labels = [];
n_labels = 0; # length of the labels array


def uf_initialize(max_labels):
    global  n_labels, labels
    n_labels = max_labels
    labels = [0 for x in range(0,max_labels)]

def uf_find(x):
    y = x
    while (labels[y] != y):
        y = labels[y]
    while (labels[x] != x) {
int z = labels[x];
labels[x] = y;
x = z;
}
return y;
}