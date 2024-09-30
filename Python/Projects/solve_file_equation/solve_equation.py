import re

file = open("in.official.txt", "r")
pattern = r'([+-]?)\s*([a-zA-Z])'
s=[]
def replace_signe(expression):
    def replace(match):
        signe = match.group(1) 
        lettre = match.group(2)

        if signe == '':
            signe = '+' 
        s.append(signe)  
        return f' {lettre}' 
    return re.sub(pattern, replace, expression)
import sys
original_stdout = sys.stdout
with open('output.txt', 'w') as f:
    sys.stdout = f
    for line in range(100):
        
        r = file.readline()
        gauche, droite = r.split("=")

        gauche = gauche.replace('- -', '+').replace('+ -', '-').replace('- +', '-').replace('+ +', '+')

        gauche = replace_signe(gauche)

        var = re.findall(r'[a-zA-Z]', gauche)

        var = ''.join(var)

        gauche= re.sub(r'[a-zA-Z]', '', gauche)

        gauche= gauche.strip()

        somme_g = eval(gauche)


        droite= droite.replace('- -', '+').replace('+ -', '-').replace('- +', '-').replace('+ +', '+')
        droite = replace_signe(droite)

        var1= re.findall(r'[a-zA-Z]', droite)
        var1 = ''.join(var1)


        droite= re.sub(r'[a-zA-Z]', '', droite)
        droite= droite.strip()

        somme_d = eval(droite)

        nombre = somme_d - somme_g
        
        if var=="":
            variable=var1
        elif var1=="":    
            variable=var  

        
        if s[-1]=="-" and var1=="" or s[-1]=="+" and var=="" :
            print(variable, "=",  -nombre)
        elif s[-1]=="+" and var1=="" or s[-1]=="-" and var=="":
            print(variable, "=",  nombre)
        
        