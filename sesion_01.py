print("========Mi Super Calculadora==========") 
num_1 = float(input("Escriba el valor del primer numero: ")) 
num_2 = float(input("Escriba el valor del segundo numero: ")) 
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ") 
def suma(num_1, num_2): 
    return num_1 + num_2 

def resta(num_1, num_2): 
    return num_1 - num_2 

def multi(num_1, num_2): 
    return num_1 * num_2 

def divi(num_1, num_2): 
    return num_1 / num_2 

if operacion == "+": 
    resultado = suma(num_1, num_2) 
    print("El resultado de la suma es: ", resultado) 
    
if operacion == "-": 
    resultado = resta(num_1, num_2) 
    print("El resultado de la resta es: ", resultado) 
    
if operacion == "*": 
    resultado = multi(num_1, num_2) 
    print("El resultado de la multiplicacion es: ", resultado) 
    
if operacion == "/": 
    resultado = divi(num_1, num_2) 
    print("El resultado de la division es: ", resultado) 
      