#Escribe una función recursiva que tome un número entero positivo como entrada y devuelva la suma de sus dígitos. No se permite el uso de bucles (como for o while), ni funciones de alto nivel como map() o reduce(). Solo se puede resolver utilizando recursión.
#Si el número es un solo dígito, su suma será el mismo número.
#Para números con más de un dígito, la suma de sus dígitos es igual al último dígito del número más la suma de los dígitos restante

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
    
print(suma_digitos(15))

resultado = 6 

