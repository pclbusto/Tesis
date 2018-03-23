#CONSTANTES
Y = 3840 #tamaño lineal de la red de sitios en la dirección right (numeros columnas)
X = 3840 #tamaño lineal de la red de sitios en la dirección down (numeros filas)
M = X*Y #Numeros de sitios*/
MAX_NUM_CLUSTERS = ((M + 1)/2)
promedios = 50000
k = 6
Np = 46 #/*numeros de puntos*/
grabadatosRD = "L640_k6.dat"

int MA[X][Y] #matriz de sitios para   detectar perclacón down
int cubrimiento[Np] #matriz para llevar el cubrimiento para cada promedio
int rotulo[MAX_NUM_CLUSTERS + 1]; #matriz para llevar el rotulo de cada cluster en cada
# pasada en la direccion down
int tamanocluster[MAX_NUM_CLUSTERS + 1] #matriz para llevar el tamaño de cluster en cada
#pasada junto con la matriz cuentacluster[] en la direccion down
double cubri_real[Np];
int mas[L], menos[L];
double perco_D[Np]; / *matriz
para llevar
la detección
de la
percolación
down * /
double
perco_R[Np]; / *matriz
para
llevar
la
detección
de
la
percolación
right * /
double
perco_U[Np]; / *matriz
para
llevar
la
percolación
bajo
el
criterio
U * /
double
perco_I[Np]; / *matriz
para
llevar
la
percolación
bajo
el
criterio
I * /
double
perco_A[Np]; / *matriz
para
llevar
la
percolación
bajo
el
criterio
A * /
int
perco_D_auxiliar[Np][promedios]; / *matriz
auxiliares
para
llevar
la
detección
de
los
criterios
de
percolación
U * /
int
perco_R_auxiliar[Np][promedios]; / *matriz
auxiliares
para
llevar
la
detección
de
los
criterios
de
percolación
I * /

double
P[Np]; / *matriz
para
llevar
los
cluster
de
mayor
tamaño
para
cada
cubrimento
en
la
dirección * /
double
P2[Np]; / *matriz
para
llevar
los
cluster
de
mayor
tamaño
al
cuadrado
para
cada
cubrimento
en
la
dirección
n * /
double
P4[Np]; / *matriz
para
llevar
los
cluster
del mayor
tamaño
a
la
cuarta
para
cada
cubrimento
en
la
dirección * /
double
U[Np]; / *matriz
para
llevar
el
cumulante
de
Binder
en
la
dirección * /
double
Ji[Np]; / *matriz
para
llevar
la
susceptibilidad * /
enum
e_adyacencia
{NINGUNA, IZQUIERDA_O_ARRIBA, IZQUIERDA_Y_ARRIBA};
double
dt; / *tiempo
que
demora
el
programa * /
int
np, aux, cubri, o, xi, yj;
int
bandera, banderaR, ta;
/ *:::::::::::::::::::::::::::::::::::::::::::::::::::: * /
void
Condiciones_Periodicas(void);
void
inicializar(void);
int
ind(int
i);
/ *::::::::::::::::::::::::::::::::::::::::::::::::::::: * /
/ *generador
numeros
al
azar * /
const
double
NMAX = 4294967296.0; / *numero
del random * /
unsigned
int
seed[256], r;
unsigned
char
irr;
time_t
t_i, t_f;
struct
tm * time_block;
void
inicializar(void)
{
    int
i, j;
/ *::::::::::::: Se
randomiza:::::::::::::::::::::::::::::::::::: * /
srand((unsigned)
time( & t_i));irr = 1;
for (j=0;j < 256;j++)
{seed[j] = rand();}r = seed[0];
for (i=0;i < 100000;i++)
r = seed[irr + +] += seed[r >> 24];
/ *::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: * /
}
int
main()
{
    t_i = time(NULL);
int
FPV;
inicializar();
Condiciones_Periodicas();
int
i, j, a, x, y, f;
int
num_rotulo;
for (np=0;np < Np;np++)
{
    cubrimiento[np] = 1043768 + 500 * np;
cubri_real[np] = 0.0;
perco_D[np] = 0;
perco_R[np] = 0;
perco_U[np] = 0;
perco_A[np] = 0;
perco_I[np] = 0;
P[np] = 0.0;
P2[np] = 0.0;
P4[np] = 0.0;
U[np] = 0.0;
Ji[np] = 0.0;
}
// for para promedios
for (FPV=1;FPV < promedios;FPV++)
{// printf("promedios=%d\n", FPV);
// if (FPV % 10 == 0){printf("h=%d\n", FPV);}
for (np=0;np < Np;np++){perco_D_auxiliar[np][FPV]=0;perco_R_auxiliar[np][FPV]=0;}

for (aux=0;aux < Np;aux++)
{
cubri=cubrimiento[aux];
// printf("cubri=%d\n", cubri);
for (i=0;i < X;i++){for (j=0;j < Y;j++){MA[i][j]=1;}}
for (o=0;o < (MAX_NUM_CLUSTERS+1);o++){rotulo[o]=0;tamanocluster[o]=0;}
// lleno matriz
int cont=0;int intentos=0;bool vacio;int flag=0;
do
{
r=seed[irr++] += seed[r >> 24];f=r % 2;
intentos++;
switch(f)
{
case 0:{ // horizontal
r = seed[irr + +] += seed[r >> 24];
x = r % L;
r = seed[irr + +] += seed[r >> 24];
y = r % L;
vacio = true;
for (j=0;j <= k-1;j++)
{
    vacio = ((MA[ind(x + j)][y] == 1) & & vacio);
}
if (vacio){for (j=0;j <= k-1;j++){MA[ind(x+j)][y]=0;}cont++;vacio=false;}
};
break; // case
4
case
1: { // horizontal
r = seed[irr + +] += seed[r >> 24];
x = r % L;
r = seed[irr + +] += seed[r >> 24];
y = r % L;
vacio = true;
for (j=0;j <= k-1;j++)
{
    vacio = ((MA[x][ind(y + j)] == 1) & & vacio);
}
if (vacio){for (j=0;j <= k-1;j++){MA[x][ind(y+j)]=0;}cont++;vacio=false;}
};break; // case 5
} // cierro
switch
if (cont == cubri)
{flag = 1;}
// for (i=0;i < L;i++){printf("\n"); for (j=0;j < L;j++){printf("\t%d", MA[i][j]);}}
// getchar();
// printf("cont=%d intentos=%d\n", cont, intentos);
}
while (flag != 1 & & intentos != M);

for (i=0;i < Y;i++)
    {
    for (j=0;j < Y;j++)
    {
    if (MA[i][j] != 0){cubri_real[aux] += 1.0;}
    }
    }
// MA[3][0] = 1;
MA[6][0] = 1;
MA[8][0] = 1;
MA[9][0] = 0;
MA[0][0] = 1;
MA[8][0] = 1;
/ * for (i = 0; i < X; i++)
{
for (j = 0; j < Y; j++)
if (MA[i][j] != 0)
printf("%3d", MA[i][j]);
else
printf("   ");
putchar('\n');
}
printf("-----------------H-K-----------------\n");
getchar(); * /
/ *aplico
H - K * /
num_rotulo = 0;

for (i=0;i < X;i++)
    {
    for (j=0;j < Y;j++)
    {
    // int etiqueta[MAX_NUM_CLUSTERS + 1];
    // printf("1\n");
    // printf("ah....\n");getchar();
    // int i, j;
    int p, q, a;

    / *
    ** Procesamiento de cada una de las celdas de la matriz, las
    ** celdas "vacias" (indicado por el valor cero) se ignoran.
    * /
    // num_rotulo = 0;
    // for (i = 0; i < NUM_FILAS; i++){
    // for (j = 0; j < NUM_COLS; j++){
    if (!MA[i][j])
    continue;

    / *
    ** Las
    variables
    "p"
    y
    "q"
    indican
    si
    existe
    un
    objeto
    adyacente
    ** en
    la
    fila
    previa
    y / o
    columna
    previa, respectivamente.
    * /
    // printf("2\n");
    p = i & & MA[i - 1][j];
    // printf("i=%d j=%d matriz=%d\n", i, j, matriz[i - 1][j]);
    q = j & & MA[i][j - 1];
    // printf("p=%d\n", p);
    getchar();
    switch(p + q)
    { / * Adyacencia? * /
    case
    NINGUNA: \
        MA[i][j] = ++num_rotulo;
    rotulo[MA[i][j]] = 1;
    break;
    case
    IZQUIERDA_O_ARRIBA:
    / *
    ** Ahora
    la
    variable
    "p"
    se
    utiliza
    para
    almacenar
    el
    "puntero"
    ** dado
    por
    la
    etiqueta
    de
    la
    fila(o
    columna) previa
    y
    obtener
    ** en
    base
    a
    esta
    su
    etiqueta
    "padre".
    * /
    // printf("a_p=%d\n", p);
    getchar();
    a = MA[i][j] = MA[i - p][j - q];
    // printf("d_p=%d\n", p);
    getchar();
    while (rotulo[a] < 0)
        a = -rotulo[a];
    rotulo[a] + +;
    break;
    case
    IZQUIERDA_Y_ARRIBA:
    / *
    ** Ahora
    la
    variables
    "p"
    y
    "q"
    se
    utilizan
    para
    almacenar
    los
    ** "punteros"
    dados
    por
    las
    etiquetas
    de
    la
    fila
    y
    columna
    ** previas
    y
    obtener
    en
    base
    a
    estas
    las
    etiquetas
    "padres".
    * /
    p = MA[i - 1][j];
    q = MA[i][j - 1];
    MA[i][j] = p < q ? p: q;

    while (rotulo[p] < 0)
        p = -rotulo[p];
    while (rotulo[q] < 0)
        q = -rotulo[q];

    / *
    ** Si
    las
    etiquetas
    indicadas
    por
    "p"
    y
    "q"
    son
    diferentes
    la
    ** etiqueta
    mayor
    se
    reasigna
    como
    un
    elemento
    "hijo"
    de
    la
    ** etiqueta
    menor.
    * /
    if (p < q){
    rotulo[p] += rotulo[q] + 1;
    rotulo[q] = -p; / * "q" se reasigna como "hijo" de "p" * /
    } else if (p == q){
    rotulo[p]++;
    } else / * p > q * / {
    rotulo[q] += rotulo[p] + 1;
    rotulo[p] = -q; / * "p" se reasigna como "hijo" de "q" * /
    }
    break;
    }
    } // cierro
    for en j
    } // cierro for en i

    / *
    ** Con este proceso se copia el numero de objetos por cluster a su
    ** ubicacion final (el array cluster[]) y se calcula el numero total
    ** de clusters almacenandose este valor en cluster[0].
    **
    ** Tambien se copian las etiquetas "padre" a cada uno de sus "hijos",
    ** con esto se asegura que todos los objetos de un cluster utilizaran
    ** una sola etiqueta una vez re-etiquetados.
    * /
    rotulo[0] = tamanocluster[0] = 0;
    for (i = 1; i <= num_rotulo; i++)
    if (rotulo[i] > 0){
    tamanocluster[++tamanocluster[0]] = rotulo[i];
    rotulo[i] = tamanocluster[0];
    } else
    rotulo[i] = rotulo[-rotulo[i]];

    / * Etiquetado final de todos los objetos de la matriz * /
    for (i = 0; i < X; i++)
    for (j = 0; j < Y; j++)
    MA[i][j] = rotulo[MA[i][j]];
    // ver matirz
    / *
    for (i = 0; i < X; i++){
    for (j = 0; j < Y; j++)
    if (MA[i][j] != 0)
    printf("%3d", MA[i][j]);
    else
    printf("   ");

    putchar('\n');
    }
    getchar(); * /
    // Determino el cluster de mayor tamaño con metodo diferente al de la burbuja que es mas rapido
    int mayor_cluster=0;double mayor=0;
    for (ta=1;ta <= tamanocluster[0];ta++)
    {
    if (tamanocluster[ta] > mayor_cluster)
    {
    mayor_cluster=tamanocluster[ta];
    }
    }
    // Mido todos los momentos y demás
    // printf("mayor_cluster=%d\n", mayor_cluster);getchar();
    mayor=mayor_cluster / (double (M));
    // printf("mayor=%f\n", mayor);getchar();
    P[aux] += 1.0 * mayor;
    P2[aux] += pow(1.0 * mayor, 2);
    P4[aux] += pow(1.0 * mayor, 4);
    U[aux]=1.0-((P4[aux] / (double)FPV) / (3 * (pow((P2[aux] / (double)FPV), 2))));
    Ji[aux]=((P2[aux] / (double)FPV)-(P[aux] / (double)FPV) * (P[aux] / (double)FPV));

    / * for (i = 1; i <= tamanocluster[0]; i++)
    printf("cluster[%02d] == %2d\n", i, tamanocluster[i]);
    getchar(); * /
    / * termino H-K * /
    / * cubri real * /
    bandera=0;  perco_D_auxiliar[aux][FPV]=0;
    // ____detecto percolación down____ //
    bandera=0;  perco_D_auxiliar[aux][FPV]=0;
    for (i=0;i < Y;i++)
    {for (j=0;j < Y;j++)
    {if (bandera == 0)
    {if (MA[0][i] != 0 & & MA[X-1][j] != 0)
    { if (MA[0][i] == MA[X - 1][j])
    {
        perco_D[aux] += 1;
    perco_D_auxiliar[aux][FPV] = 1;
    bandera = 1; // printf("Percolo_2 FPV=%d\n", FPV);
    getchar();
    }
    }
    }
    }
    }
    // ____termina
    detecto
    percolación
    down____ //

    // ____detecto
    percolación
    right____ // \
 \
    banderaR = 0;
    perco_R_auxiliar[aux][FPV] = 0;
    for (j=0;j < X;j++)
    {for (i=0;i < X;i++)
    {if (banderaR == 0)
    {if (MA[i][0] != 0 & & MA[j][Y-1] != 0)
    { if (MA[i][0] == MA[j][Y - 1])
    {
        perco_R[aux] += 1;
    perco_R_auxiliar[aux][FPV] = 1;
    banderaR = 1;
    }
    }
    }
    }
    }

    // ____termina
    detecto
    percolación
    right____ //

    / * ____Calculo
    la
    RU
    y
    RI____ * /
    if (perco_D_auxiliar[aux][FPV] == 1 | | perco_R_auxiliar[aux][FPV] == 1)
    {perco_U[aux] += 1;}
    if (perco_D_auxiliar[aux][FPV] == 1 & & perco_R_auxiliar[aux][FPV] == 1){perco_I[aux] += 1;}
    / * ____termina Calculo la RU y RI____ * /

    / * ____Calculo la RA____ * /
    perco_A[aux]=(perco_U[aux]+ perco_I[aux]) * ((double )0.5);
    / * ____termina Calculo la RA____ * /

    } // cierro for de aux, lleva el cubrimiento



    t_f=time(NULL);
    dt=difftime(t_f, t_i);
    // printf("dt=%f \n", dt);
    // getchar();
    int uj;
    if ((archivo=fopen(grabadatosRD, "w")) == NULL){printf("error al abrir el archivo\n");getchar();exit(0);}
    fprintf(archivo, "cubri_real\t  cubrimiento\t    RD\t   RR\t   U\t    A\t    I\t P\t P2\t P4\t Ji\t U\t tiempo\t  promedios\n");
    for (uj=0;uj < Np;uj++)
    {
    fprintf(archivo, "%.4f\t %.4f\t  %f\t %f\t %f\t %f\t %f\t %f\t %f\t %f\t %f\t %f\t %f\t %d\n", cubri_real[uj] / ((double)M * FPV), 1.0-((k * cubrimiento[uj]) / ((double)M)), perco_D[uj] / ((double)(FPV)), perco_R[uj] / ((double)(FPV)), perco_U[uj] / ((double)(FPV)), perco_A[uj] / ((double)(FPV)), perco_I[uj] / ((double)(FPV)), P[uj] / ((double)(FPV)), P2[uj] / ((double)(FPV)), (P4[uj] / ((double)(FPV))), (Ji[uj] * X * Y), U[uj], dt, FPV);
    }
    fclose(archivo);

    } // cierra for sobre promedios FPV

    } // main

    void Condiciones_Periodicas(void)
    {
    int iii, i;
    / *::
        Se
    llena
    el
    vector
    vecinos::::::::: * /
    for (i=0;i < L;i++){mas[i]=i+1;}
    for (i=1;i < L;i++){menos[i]=i-1;}
    mas[L-1]=0;menos[0]=L-1;

    }
    int ind(int i){
    // Devuleve un número entre 0 y N-1.
    // Sirve para hacer condiciones circulares de contorno.
    // Supone que N es el tamaño lineal del sistema.
    if (i >= 0){
    return (i % L);
    } else {
    return (ind(L + i));
    }
    }