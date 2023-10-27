def somme(T):
    s=0
    for i in T:
         s=s+i
    return s
def produit(T):
     p=1
     for i in T:
          p=p*i
          return p
def moyenne(T):
    m=0
    s=somme(T)
    m=s/10
    return m
def sign(T):
    print("les elements posetive sont:")
    N=[]
    P=[]
    for i in range(10):
        if T[i]>0:
            P.append(T[i])
    print(P)   
    print("les elements négatives sont:")
    for i in range(10):  
        if T[i]<0:
            N.append(T[i])
    print(N)
T=[]
for i in range(10):
     n=int(input(f"Entrer le nombre {i+1}:"))
     T.append(n)
print("la somme est",somme(T))
print("Le produit est",produit(T))
print("La moyenne est",moyenne(T))
sign(T)

