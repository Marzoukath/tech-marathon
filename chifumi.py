from random import randrange
p=0
v=0
print("Bienvenue !!! Chifumi !!!")
while(1):
    
    m=int(input("Choisis un nombre pour jouer: \n 1.Pierre \n 2.Feuille \n 3.Ciseaux \n  \n Votre choix:  " ))

    n=randrange(1,3)

    dict = {"Pierre": 1, "Feuille": 2, "Ciseaux": 3}

    def obtenir_cle(valeur):
        for cle, val in dict.items():
            if val == valeur:
                return cle
        return "Cette valeur n'existe pas dans le dictionnaire"

    if(m==1 and n==3) or (m==2 and n==1) or (m==3 and n==2):
        
        print("Vous avez jouer",obtenir_cle(m), "et j'ai jouer", obtenir_cle(n))
        print("Felicitations, vous avez remporter la partie.")
        v=v+1
    elif(m==n):
        print("Egalite")
        print("On a tous jouer", obtenir_cle(m))
    else:
        print("Vous avez jouer",obtenir_cle(m), "et j'ai jouer", obtenir_cle(n))
        print("Vous avez perdu !!!")
        p=p+1
    a=input("Voulez vous continuer la partie? O/N: ")
    if(a=='N'):
        break
print("Vous avez comptabiliser", v,"points et moi",p,"points")
if(v>p):
    print("Vous avez remporter le jeu.")
elif(v==p):
    print("Egalite !!!!")
else: 
    
    print("L'ordinateur a remporte, vous avez perdu")
    
    
    
        

