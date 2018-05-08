from enum import Enum
import random

class Adyacencia(Enum):
    NINGUNA=0
    IZQUIERDA_O_ARRIBA= 1
    IZQUIERDA_Y_ARRIBA=2


#CONSTANTES
Y = 3840 #tamaño lineal de la red de sitios en la dirección right (numeros columnas)
X = 3840 #tamaño lineal de la red de sitios en la dirección down (numeros filas)
L = X
M = X*Y #Numeros de sitios
MAX_NUM_CLUSTERS = int((M + 1)/2)
promedios = 50000
k = 6
Np = 46 #numeros de puntos
grabadatosRD = "L640_k6.dat"

MA = [[0 for x in range(X)] for y in range(Y)] #matriz de sitios para   detectar perclacón down
cubrimiento = [0 for x in range(Np)] #matriz para llevar el cubrimiento para cada promedio
rotulo =[0 for x in range(MAX_NUM_CLUSTERS + 1)] #matriz para llevar el rotulo de cada cluster en cada
# pasada en la direccion down
tamanocluster = [0 for x in range(MAX_NUM_CLUSTERS + 1)] #matriz para llevar el tamaño de cluster en cada
#pasada junto con la matriz cuentacluster[] en la direccion down
cubri_real= [0.0 for x in range(Np)]
mas= [0 for x in range(L)]
menos= [0 for x in range(L)]
perco_D= [0.0 for x in range(Np)] #matriz para llevar la detección de la percolación down
perco_R= [0.0 for x in range(Np)] #*matriz para llevar la detección de la percolación right
perco_U= [0.0 for x in range(Np)] #*matriz para llevar la percolación bajo el criterio U
perco_I= [0.0 for x in range(Np)] #*matriz para llevar la percolación bajo el criterio I
perco_A= [0.0 for x in range(Np)] #*matriz para llevar la percolación bajo el criterio A
perco_D_auxiliar= [[0 for x in range(Np)] for y in range(promedios)] #matriz auxiliares para llevar la detección de los criterios de percolación U
perco_R_auxiliar= [[0 for x in range(Np)] for y in range(promedios)] #matriz auxiliares para llevar la detección de los criterios de percolación I
P= [0 for x in range(Np)]#matriz para llevar los cluster de mayor tamaño para cada cubrimento en la dirección
P2= [0 for x in range(Np)]#matriz para llevar los cluster de mayor tamaño al cuadrado para cada cubrimento en la dirección n
P4= [0 for x in range(Np)]#matriz para llevar los cluster del mayor tamaño a la cuarta para cada cubrimento en la dirección
U= [0 for x in range(Np)]#matriz para llevar el cumulante de Binder en la dirección
Ji= [0 for x in range(Np)]#matriz para llevar la susceptibilidad

dt=0.0 #tiempo que demora el programa
np, aux, cubri, o, xi, yj = 0,0,0,0,0,0
bandera, banderaR, ta = 0,0,0

seed=[]
r=0
irr=0
t_i, t_f=0,0

def inicializar(seed):
    i, j, irr=0,0,1
    random.seed()
    seed = [random.randrange(1) for i in range(256)]
    r = seed[0]
    # for i in range(100000):
    #     seed[irr] += seed[r]
    #     r= seed[irr]
    #     irr +=1

def condiciones_periodicas():
    global mas, menos
    #Se llena el vector vecinos
    for  index, elemento in enumerate(mas):
        elemento = index+1
    for index, elemento in enumerate(menos):
        elemento = index-1
    mas[L-1] = 0
    menos[0] = L - 1

if __name__== '__main__':
    inicializar(seed)
    condiciones_periodicas()
    for index, (elem_cubrimiento, elem_cubri_real, elem_perco_d, elem_perco_r) \
            in enumerate(zip(cubrimiento, cubri_real, perco_D, perco_R)):
        # ,\
        # elem_perco_u, elem_perco_a, elem_perco_i, elem_p, elem_p2, elem_p4,\
        # elem_u, elem_ji
        # in zip(cubrimiento, cubri_real, perco_D, perco_R, perco_U, perco_A, perco_I, P, P2, P4, U, Ji):

        elem_cubrimiento = 1043768 + 500 * index
        print(elem_cubrimiento)
        elem_cubri_real = 0.0
        elem_perco_D = 0
        elem_perco_R = 0
        elem_perco_U = 0
        elem_perco_A = 0
        elem_perco_I = 0
        elem_P = 0.0
        elem_P2 = 0.0
        elem_P4 = 0.0
        elem_U = 0.0
        elem_Ji = 0.0

    for perco_D, perco_R in zip(perco_D_auxiliar, perco_R_auxiliar):
        for elem_D, elem_R in zip(perco_D,perco_R):
            elem_D = 0
            elem_R = 0

    for ele in cubrimiento:
        print(ele)

    print("Hsdasoal")
#
# int main()
# {
#     t_i = time(NULL)
# int
# FPV
# inicializar()
# Condiciones_Periodicas()
# int
# i, j, a, x, y, f
# int
# num_rotulo
# for (np=0np < Npnp++)
# {
#     cubrimiento[np] = 1043768 + 500 * np
# cubri_real[np] = 0.0
# perco_D[np] = 0
# perco_R[np] = 0
# perco_U[np] = 0
# perco_A[np] = 0
# perco_I[np] = 0
# P[np] = 0.0
# P2[np] = 0.0
# P4[np] = 0.0
# U[np] = 0.0
# Ji[np] = 0.0
# }
# // for para promedios
# for (FPV=1FPV < promediosFPV++)
# {// printf("promedios=%d\n", FPV)
# // if (FPV % 10 == 0){printf("h=%d\n", FPV)}
# for (np=0np < Npnp++){perco_D_auxiliar[np][FPV]=0perco_R_auxiliar[np][FPV]=0}
#
# for (aux=0aux < Npaux++)
# {
# cubri=cubrimiento[aux]
# // printf("cubri=%d\n", cubri)
# for (i=0i < Xi++){for (j=0j < Yj++){MA[i][j]=1}}
# for (o=0o < (MAX_NUM_CLUSTERS+1)o++){rotulo[o]=0tamanocluster[o]=0}
# // lleno matriz
# int cont=0int intentos=0bool vacioint flag=0
# do
# {
# r=seed[irr++] += seed[r >> 24]f=r % 2
# intentos++
# switch(f)
# {
# case 0:{ // horizontal
# r = seed[irr + +] += seed[r >> 24]
# x = r % L
# r = seed[irr + +] += seed[r >> 24]
# y = r % L
# vacio = true
# for (j=0j <= k-1j++)
# {
#     vacio = ((MA[ind(x + j)][y] == 1) & & vacio)
# }
# if (vacio){for (j=0j <= k-1j++){MA[ind(x+j)][y]=0}cont++vacio=false}
# }
# break // case
# 4
# case
# 1: { // horizontal
# r = seed[irr + +] += seed[r >> 24]
# x = r % L
# r = seed[irr + +] += seed[r >> 24]
# y = r % L
# vacio = true
# for (j=0j <= k-1j++)
# {
#     vacio = ((MA[x][ind(y + j)] == 1) & & vacio)
# }
# if (vacio){for (j=0j <= k-1j++){MA[x][ind(y+j)]=0}cont++vacio=false}
# }break // case 5
# } // cierro
# switch
# if (cont == cubri)
# {flag = 1}
# // for (i=0i < Li++){printf("\n") for (j=0j < Lj++){printf("\t%d", MA[i][j])}}
# // getchar()
# // printf("cont=%d intentos=%d\n", cont, intentos)
# }
# while (flag != 1 & & intentos != M)
#
# for (i=0i < Yi++)
#     {
#     for (j=0j < Yj++)
#     {
#     if (MA[i][j] != 0){cubri_real[aux] += 1.0}
#     }
#     }
# // MA[3][0] = 1
# MA[6][0] = 1
# MA[8][0] = 1
# MA[9][0] = 0
# MA[0][0] = 1
# MA[8][0] = 1
# / * for (i = 0 i < X i++)
# {
# for (j = 0 j < Y j++)
# if (MA[i][j] != 0)
# printf("%3d", MA[i][j])
# else
# printf("   ")
# putchar('\n')
# }
# printf("-----------------H-K-----------------\n")
# getchar() * /
# / *aplico
# H - K * /
# num_rotulo = 0
#
# for (i=0i < Xi++)
#     {
#     for (j=0j < Yj++)
#     {
#     // int etiqueta[MAX_NUM_CLUSTERS + 1]
#     // printf("1\n")
#     // printf("ah....\n")getchar()
#     // int i, j
#     int p, q, a
#
#     / *
#     ** Procesamiento de cada una de las celdas de la matriz, las
#     ** celdas "vacias" (indicado por el valor cero) se ignoran.
#     * /
#     // num_rotulo = 0
#     // for (i = 0 i < NUM_FILAS i++){
#     // for (j = 0 j < NUM_COLS j++){
#     if (!MA[i][j])
#     continue
#
#     / *
#     ** Las
#     variables
#     "p"
#     y
#     "q"
#     indican
#     si
#     existe
#     un
#     objeto
#     adyacente
#     ** en
#     la
#     fila
#     previa
#     y / o
#     columna
#     previa, respectivamente.
#     * /
#     // printf("2\n")
#     p = i & & MA[i - 1][j]
#     // printf("i=%d j=%d matriz=%d\n", i, j, matriz[i - 1][j])
#     q = j & & MA[i][j - 1]
#     // printf("p=%d\n", p)
#     getchar()
#     switch(p + q)
#     { / * Adyacencia? * /
#     case
#     NINGUNA: \
#         MA[i][j] = ++num_rotulo
#     rotulo[MA[i][j]] = 1
#     break
#     case
#     IZQUIERDA_O_ARRIBA:
#     / *
#     ** Ahora
#     la
#     variable
#     "p"
#     se
#     utiliza
#     para
#     almacenar
#     el
#     "puntero"
#     ** dado
#     por
#     la
#     etiqueta
#     de
#     la
#     fila(o
#     columna) previa
#     y
#     obtener
#     ** en
#     base
#     a
#     esta
#     su
#     etiqueta
#     "padre".
#     * /
#     // printf("a_p=%d\n", p)
#     getchar()
#     a = MA[i][j] = MA[i - p][j - q]
#     // printf("d_p=%d\n", p)
#     getchar()
#     while (rotulo[a] < 0)
#         a = -rotulo[a]
#     rotulo[a] + +
#     break
#     case
#     IZQUIERDA_Y_ARRIBA:
#     / *
#     ** Ahora
#     la
#     variables
#     "p"
#     y
#     "q"
#     se
#     utilizan
#     para
#     almacenar
#     los
#     ** "punteros"
#     dados
#     por
#     las
#     etiquetas
#     de
#     la
#     fila
#     y
#     columna
#     ** previas
#     y
#     obtener
#     en
#     base
#     a
#     estas
#     las
#     etiquetas
#     "padres".
#     * /
#     p = MA[i - 1][j]
#     q = MA[i][j - 1]
#     MA[i][j] = p < q ? p: q
#
#     while (rotulo[p] < 0)
#         p = -rotulo[p]
#     while (rotulo[q] < 0)
#         q = -rotulo[q]
#
#     / *
#     ** Si
#     las
#     etiquetas
#     indicadas
#     por
#     "p"
#     y
#     "q"
#     son
#     diferentes
#     la
#     ** etiqueta
#     mayor
#     se
#     reasigna
#     como
#     un
#     elemento
#     "hijo"
#     de
#     la
#     ** etiqueta
#     menor.
#     * /
#     if (p < q){
#     rotulo[p] += rotulo[q] + 1
#     rotulo[q] = -p / * "q" se reasigna como "hijo" de "p" * /
#     } else if (p == q){
#     rotulo[p]++
#     } else / * p > q * / {
#     rotulo[q] += rotulo[p] + 1
#     rotulo[p] = -q / * "p" se reasigna como "hijo" de "q" * /
#     }
#     break
#     }
#     } // cierro
#     for en j
#     } // cierro for en i
#
#     / *
#     ** Con este proceso se copia el numero de objetos por cluster a su
#     ** ubicacion final (el array cluster[]) y se calcula el numero total
#     ** de clusters almacenandose este valor en cluster[0].
#     **
#     ** Tambien se copian las etiquetas "padre" a cada uno de sus "hijos",
#     ** con esto se asegura que todos los objetos de un cluster utilizaran
#     ** una sola etiqueta una vez re-etiquetados.
#     * /
#     rotulo[0] = tamanocluster[0] = 0
#     for (i = 1 i <= num_rotulo i++)
#     if (rotulo[i] > 0){
#     tamanocluster[++tamanocluster[0]] = rotulo[i]
#     rotulo[i] = tamanocluster[0]
#     } else
#     rotulo[i] = rotulo[-rotulo[i]]
#
#     / * Etiquetado final de todos los objetos de la matriz * /
#     for (i = 0 i < X i++)
#     for (j = 0 j < Y j++)
#     MA[i][j] = rotulo[MA[i][j]]
#     // ver matirz
#     / *
#     for (i = 0 i < X i++){
#     for (j = 0 j < Y j++)
#     if (MA[i][j] != 0)
#     printf("%3d", MA[i][j])
#     else
#     printf("   ")
#
#     putchar('\n')
#     }
#     getchar() * /
#     // Determino el cluster de mayor tamaño con metodo diferente al de la burbuja que es mas rapido
#     int mayor_cluster=0double mayor=0
#     for (ta=1ta <= tamanocluster[0]ta++)
#     {
#     if (tamanocluster[ta] > mayor_cluster)
#     {
#     mayor_cluster=tamanocluster[ta]
#     }
#     }
#     // Mido todos los momentos y demás
#     // printf("mayor_cluster=%d\n", mayor_cluster)getchar()
#     mayor=mayor_cluster / (double (M))
#     // printf("mayor=%f\n", mayor)getchar()
#     P[aux] += 1.0 * mayor
#     P2[aux] += pow(1.0 * mayor, 2)
#     P4[aux] += pow(1.0 * mayor, 4)
#     U[aux]=1.0-((P4[aux] / (double)FPV) / (3 * (pow((P2[aux] / (double)FPV), 2))))
#     Ji[aux]=((P2[aux] / (double)FPV)-(P[aux] / (double)FPV) * (P[aux] / (double)FPV))
#
#     / * for (i = 1 i <= tamanocluster[0] i++)
#     printf("cluster[%02d] == %2d\n", i, tamanocluster[i])
#     getchar() * /
#     / * termino H-K * /
#     / * cubri real * /
#     bandera=0  perco_D_auxiliar[aux][FPV]=0
#     // ____detecto percolación down____ //
#     bandera=0  perco_D_auxiliar[aux][FPV]=0
#     for (i=0i < Yi++)
#     {for (j=0j < Yj++)
#     {if (bandera == 0)
#     {if (MA[0][i] != 0 & & MA[X-1][j] != 0)
#     { if (MA[0][i] == MA[X - 1][j])
#     {
#         perco_D[aux] += 1
#     perco_D_auxiliar[aux][FPV] = 1
#     bandera = 1 // printf("Percolo_2 FPV=%d\n", FPV)
#     getchar()
#     }
#     }
#     }
#     }
#     }
#     // ____termina
#     detecto
#     percolación
#     down____ //
#
#     // ____detecto
#     percolación
#     right____ // \
#  \
#     banderaR = 0
#     perco_R_auxiliar[aux][FPV] = 0
#     for (j=0j < Xj++)
#     {for (i=0i < Xi++)
#     {if (banderaR == 0)
#     {if (MA[i][0] != 0 & & MA[j][Y-1] != 0)
#     { if (MA[i][0] == MA[j][Y - 1])
#     {
#         perco_R[aux] += 1
#     perco_R_auxiliar[aux][FPV] = 1
#     banderaR = 1
#     }
#     }
#     }
#     }
#     }
#
#     // ____termina
#     detecto
#     percolación
#     right____ //
#
#     / * ____Calculo
#     la
#     RU
#     y
#     RI____ * /
#     if (perco_D_auxiliar[aux][FPV] == 1 | | perco_R_auxiliar[aux][FPV] == 1)
#     {perco_U[aux] += 1}
#     if (perco_D_auxiliar[aux][FPV] == 1 & & perco_R_auxiliar[aux][FPV] == 1){perco_I[aux] += 1}
#     / * ____termina Calculo la RU y RI____ * /
#
#     / * ____Calculo la RA____ * /
#     perco_A[aux]=(perco_U[aux]+ perco_I[aux]) * ((double )0.5)
#     / * ____termina Calculo la RA____ * /
#
#     } // cierro for de aux, lleva el cubrimiento
#
#
#
#     t_f=time(NULL)
#     dt=difftime(t_f, t_i)
#     // printf("dt=%f \n", dt)
#     // getchar()
#     int uj
#     if ((archivo=fopen(grabadatosRD, "w")) == NULL){printf("error al abrir el archivo\n")getchar()exit(0)}
#     fprintf(archivo, "cubri_real\t  cubrimiento\t    RD\t   RR\t   U\t    A\t    I\t P\t P2\t P4\t Ji\t U\t tiempo\t  promedios\n")
#     for (uj=0uj < Npuj++)
#     {
#     fprintf(archivo, "%.4f\t %.4f\t  %f\t %f\t %f\t %f\t %f\t %f\t %f\t %f\t %f\t %f\t %f\t %d\n", cubri_real[uj] / ((double)M * FPV), 1.0-((k * cubrimiento[uj]) / ((double)M)), perco_D[uj] / ((double)(FPV)), perco_R[uj] / ((double)(FPV)), perco_U[uj] / ((double)(FPV)), perco_A[uj] / ((double)(FPV)), perco_I[uj] / ((double)(FPV)), P[uj] / ((double)(FPV)), P2[uj] / ((double)(FPV)), (P4[uj] / ((double)(FPV))), (Ji[uj] * X * Y), U[uj], dt, FPV)
#     }
#     fclose(archivo)
#
#     } // cierra for sobre promedios FPV
#
#     } // main
#
#
#     int ind(int i){
#     // Devuleve un número entre 0 y N-1.
#     // Sirve para hacer condiciones circulares de contorno.
#     // Supone que N es el tamaño lineal del sistema.
#     if (i >= 0){
#     return (i % L)
#     } else {
#     return (ind(L + i))
#     }
#     }