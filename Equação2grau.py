'''
Autor : João Otavio Martini Korczovei
Objetivo : Realizar uma equação de 2º grau
'''
import math
def equacao2grau():
    a=float(input("Informe o valor de a: "))
    b=float(input("Informe o valor de b: "))
    c=float(input("Informe o valor de c: "))
    delta=b**2-4*a*c
    if delta<0:
        print("Delta negativo, sem solução")
    else:
        x1=(-1*b+math.sqrt(delta))/2*a
        x2=(-1*b-math.sqrt(delta))/2*a
        print("Delta =",delta)
        print("Para raíz de delta positivo, x =",x1)
        print("Para raíz de delta negativo, x =",x2)        
def main():
    print(5*'-=-')
    print('Equação de 2 grau')
    print(5*'-=-')
    equacao2grau()
main()
print(5*'-=-')
input('Presione ENTER para fechar')


    
