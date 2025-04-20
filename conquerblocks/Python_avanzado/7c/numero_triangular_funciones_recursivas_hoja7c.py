#Crea una función recursiva llamada numero_triangular que calcule el n-ésimo 
#número triangular. Un número triangular se obtiene al sumar todos los 
#números naturales desde 1 hasta n

def numero_triangular(n):
    if n == 1:
        return 1
    else:
        return n + numero_triangular(n-1)
    
print(numero_triangular(5)) 

