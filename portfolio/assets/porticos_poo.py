import numpy as np
# GRADOS DE LIBERTAD
n=9
KTOTAL=np.zeros((n,n))
E=2.1*10**7

class Frame:
    def __init__(self, name, cdxi, cdxf, cdyi, cdyf, E, A, I):
        self.name=name
        self.coord_xi=cdxi
        self.coord_xf=cdxf
        self.coord_yi=cdyi
        self.coord_yf=cdyf
        self.mod_elastico=E
        self.area=A
        self.inercia=I
        self.despl=np.array([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0]])
        self.despl_pro=np.array([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0]])
        self.fuerzas=np.array([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0]])
        self.matriz_rig=np.zeros((6,6))

        self.normal=0
        self.mon_i=0
        self.mon_j=0

        x1=self.coord_xi
        x2=self.coord_xf
        y2=self.coord_yf
        y1=self.coord_yi

        self.long=((x1-x2)**2+(y2-y1)**2)**0.5          
        L=self.long
        self.cx=(x2-x1)/L
        self.cy=(y2-y1)/L

    def matriz_elemento(self):

        E=self.mod_elastico
        A=self.area
        I=self.inercia
        L=self.long
        cx=self.cx
        cy=self.cy

        MK=   np.array([ [(E*A/L)*cx**2+12*E*I/L**3*cy**2 , (E*A/L-12*E*I/L**3)*cx*cy, -6*E*I/(L**2)*cy, -(E*A/L)*cx**2-12*E*I/L**3*cy**2, (12*E*I/L**3-E*A/L)*cx*cy, -6*E*I/(L**2)*cy],
        [(E*A/L-12*E*I/L**3)*cx*cy  , (E*A/L)*cy**2+12*E*I/L**3*cx**2, 6*E*I/(L**2)*cx, (12*E*I/L**3-E*A/L)*cx*cy, -(E*A/L)*cy**2-12*E*I/L**3*cx**2, 6*E*I/(L**2)*cx],
        [-6*E*I/(L**2)*cy  , 6*E*I/(L**2)*cx , 4*E*I/L, 6*E*I/(L**2)*cy, -6*E*I/(L**2)*cx, 2*E*I/L],
        [-(E*A/L)*cx**2-12*E*I/L**3*cy**2  ,(12*E*I/L**3-E*A/L)*cx*cy , 6*E*I/(L**2)*cy, (E*A/L)*cx**2+12*E*I/L**3*cy**2, (E*A/L-12*E*I/L**3)*cx*cy, 6*E*I/(L**2)*cy],
        [(12*E*I/L**3-E*A/L)*cx*cy  ,-(E*A/L)*cy**2-12*E*I/L**3*cx**2 , -6*E*I/(L**2)*cx, (E*A/L-12*E*I/L**3)*cx*cy, (E*A/L)*cy**2+12*E*I/L**3*cx**2, -6*E*I/(L**2)*cx],
        [-6*E*I/(L**2)*cy  ,6*E*I/(L**2)*cx , 2*E*I/L, 6*E*I/(L**2)*cy, -6*E*I/(L**2)*cx, 4*E*I/L]
        ])

        self.matriz_rig=MK

    def gdls(self, gl1,gl2,gl3,gl4,gl5,gl6):
        self.gdl=np.array([gl1,gl2,gl3,gl4,gl5,gl6])

    def ensamblaje(self):
        self.matriz_elemento()
        for i in [0,1,2,3,4,5]:
            if self.gdl[i]!=0:
                for j in [0,1,2,3,4,5]:
                    if self.gdl[j]!=0:
                     KTOTAL[self.gdl[i]-1, self.gdl[j]-1]=KTOTAL[self.gdl[i]-1, self.gdl[j]-1]+self.matriz_rig[i,j]

    def desplazamientos(self, U):
        
        gl=self.gdl
        for i in [0,1,2,3,4,5]:
            if gl[i]!=0:
                self.despl[i]=U[gl[i]-1]
            else:
                self.despl[i]=0

        return self.despl
    
    def resultados_desplazamientos(self, U):
        self.desplazamientos(U)
        print("\nDesplazamientos [",self.name,"]\n", self.despl)

    def resultados_fuerzas(self):
        self.fuerzas=np.matmul(self.matriz_rig, self.despl)
        print("\nFuerzas [",self.name,"]\n",self.fuerzas)

    def proyectar_desplazamientos(self):
        self.despl_pro[0]=self.cx*self.despl[0]+self.cy*self.despl[1]
        self.despl_pro[1]=-1*self.cy*self.despl[0]+self.cx*self.despl[1]
        self.despl_pro[2]=self.despl[2]
        self.despl_pro[3]=self.cx*self.despl[3]+self.cy*self.despl[4]
        self.despl_pro[4]=-1*self.cy*self.despl[3]+self.cx*self.despl[4]
        self.despl_pro[5]=self.despl[5]

    def fuerzas_internas(self):
        self.proyectar_desplazamientos()
        self.normal=self.mod_elastico*self.area/self.long*(self.despl_pro[3]-self.despl_pro[0])
        r=(self.despl_pro[4]-self.despl_pro[1])/self.long
        self.mon_i=2*self.mod_elastico*self.inercia/self.long*(2*self.despl_pro[2]+self.despl_pro[5]-3*r)
        self.mon_j=2*self.mod_elastico*self.inercia/self.long*(self.despl_pro[2]+2*self.despl_pro[5]-3*r)
    
    def resultados_fuerzas_int(self):
        self.fuerzas_internas()
        print("\nFuerzas Internas [",self.name,"]\nN:",self.normal,"Mi:", self.mon_i,"Mjyu:", self.mon_j)


np.set_printoptions(precision=1)
np.set_printoptions(suppress=True)
np.set_printoptions(linewidth=120)

A_viga=0.005
I_viga=2*10**-4

A_colum=0.01
I_colum=10**-4

#DEFINICIÓN DE ELEMENTOS
AB=Frame("Columna AB", 0, 0, 0, 6, E, A_colum, I_colum)
AB.matriz_elemento()
print(AB.name, "\n", AB.matriz_rig, "\n")
AB.gdls(0,0,0,1,2,3)
AB.ensamblaje()
print(KTOTAL)

BC=Frame("Viga BC", 0, 7.5, 6, 8.5, E, A_viga, I_viga)
BC.matriz_elemento()
print(BC.name, "\n", BC.matriz_rig, "\n")
BC.gdls(1,2,3,4,5,6)
BC.ensamblaje()
print(KTOTAL)

CD=Frame("Viga CD", 7.5, 15, 8.5, 6, E, A_viga, I_viga)
CD.matriz_elemento()
print(CD.name, "\n", CD.matriz_rig, "\n")
CD.gdls(4,5,6,7,8,9)
CD.ensamblaje()
print(KTOTAL)

ED=Frame("Columna ED", 15, 15, 0, 6, E, A_colum, I_colum)
ED.matriz_elemento()
print(ED.name, "\n", ED.matriz_rig, "\n")
ED.gdls(0,0,0,7,8,9)
ED.ensamblaje()
print(KTOTAL)

#RIGIDEZ
print("Matriz de rigidez total\n", KTOTAL)

print("\nFuerzas")
F=np.array([[2],[0],[0],[0],[-5],[0],[0],[0],[0]])
print(F)

np.set_printoptions(precision=4, suppress=False)
U=np.matmul(np.linalg.inv(KTOTAL),F)
print("\nVector de desplazamientos\n", U)

#CÁLCULOS
AB.resultados_desplazamientos(U)
AB.resultados_fuerzas()
AB.resultados_fuerzas_int()

BC.resultados_desplazamientos(U)
BC.resultados_fuerzas()
BC.resultados_fuerzas_int()

CD.resultados_desplazamientos(U)
CD.resultados_fuerzas()
CD.resultados_fuerzas_int()

ED.resultados_desplazamientos(U)
ED.resultados_fuerzas()
ED.resultados_fuerzas_int()


