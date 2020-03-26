"""
In AFD_EX1.txt avem primul exemplu din documentul cu tema
In AFD_EX2.txt avem al doilea exemplu din documentul cu tema
In AFN_EX1.txt/AFN_EX2.txt avem doua exemple de AFN unde in AFN_EX1.txt avem o singura stare finala si in AFN_EX2.txt avem doua stari finale
IN EX_NOU.txt nu se afla nimic , fiind un fisier dedicat unui nou exemplu
"""

def dfs(x, cuv):
    global ok
    for i in range(nr_total_stari):
        if ( cuv[0] in matrice[x][i]) : #verificam daca primul caracter din cuvant se afla pe pozitia data in matrice
            cuv = cuv[1:] #sterg primul caracter
            if len(cuv) == 0:
                if i in stari_finale: #verifica daca starea i este o stare finala
                    ok = 1
                break
            dfs(i, cuv)
#citim numele fisieului
data=input("Numele fisierului:")
f=open(data,"r")

#citim numarul total de stari
s = f.readline()
nr_total_stari = int(s)

#Stara initiala
s = f.readline()
stare_initiala = int(s)

#Numarul de stari finale
s = f.readline()
nr_stari_finale = int(s)

stari_finale = [] #vector de stari finale

for i in range(nr_stari_finale):
    s = f.readline() #citim starile finale
    stari_finale.append(int(s))

#citim numarul de tranzitii
s = f.readline()
nr_de_tranzitii = int(s)

matrice = [] #matricea grafului
for i in range (nr_total_stari):
    linii = []
    for j in range (nr_total_stari):
        linii.append([])
    matrice.append(linii)
# punem literee corepunzatoare in matrice pe pozitiile care au coordonatele date
# de nodul de la care pleaca o tranzitie si nodul la care ajunge o tranzitie
for i in range(nr_de_tranzitii):
    s = f.readline()
    t = s.split()
    x = int(t[0])
    y = int(t[1])
    z = t[2]
    matrice[x][y].append(z)

#citim cuvantul de la tastatura ca sa ne fie mai usor sa bagam diferitele exemple
cuv=input("Cuvantul pe care trebuie sa il verificam este:")
f.close()

#Pentru cuvantul vid folosim enter
if cuv == '' and stare_initiala in stari_finale:
    print("Cuvantul vid este acceptat")
else:
    ok = 0
    dfs(stare_initiala, cuv)
    if ok == 0:
        print("Cuvantul", end=" ")
        print(cuv, end=" ")
        print("nu este acceptat!")
    else:
        print("Cuvantul", end=" ")
        print(cuv, end=" ")
        print("este acceptat!")