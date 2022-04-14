import math

historial = []
resultado = 0
class Operacion:
    
    resultado1 = 0

    def suma(f_number, s_number):
        resultado1 = f_number + s_number
        return resultado1
        

    def resta(f_number, s_number):
        resultado1 = f_number - s_number
        return resultado1
                

    def multiplicacion(f_number, s_number):
        resultado1 = f_number * s_number
        return resultado1


    def division(f_number, s_number):
        resultado1 = f_number / s_number
        return resultado1


    def potencia(f_number, s_number):
        resultado1 = f_number ** s_number
        return resultado1


    def sqrt(f_number):
        resultado1 = math.sqrt(f_number)
        return resultado1
    

def que_operacion(f_number, s_number):
    if opt == 'suma':
        resultado = Operacion.suma(f_number, s_number)
        print(resultado)
        historial.append(resultado)
    elif opt == 'resta':
        resultado = Operacion.resta(f_number, s_number)
        print(resultado)
        historial.append(resultado)
    elif opt == 'multiplicacion':
        resultado = Operacion.multiplicacion(f_number, s_number)
        print(resultado)
        historial.append(resultado)
    elif opt == 'division':
        resultado = Operacion.division(f_number, s_number) 
        print(resultado)
        historial.append(resultado)
    elif opt == 'potencia':
        resultado = Operacion.potencia(f_number, s_number)
        print(resultado)
        historial.append(resultado)
    elif opt == 'raiz cuadrada':
        resultado = Operacion.sqrt(f_number)
        print(resultado)
        historial.append(resultado)

def history():
    if opt == 'suma':
        print(historial)
    elif opt == 'resta':
        print(historial)
    elif opt == 'multiplicacion':
        print(historial)
    elif opt == 'division':
        print(historial)
    elif opt == 'potencia':
        print(historial)
    elif opt == 'raiz cuadrada':
        print(historial)

while True:
    opt = input('Escriba una operacion: ').lower()
    if opt == 'raiz cuadrada':
        f_number = float(input('Ingrese el numero: '))
        s_number = 0
    elif opt == 'potencia':
        f_number = float(input('Ingrese la base: '))
        s_number = float(input('Ingrese la potencia: ')) 
    else:
        f_number = float(input('Ingrese el primer numero: '))
        s_number = float(input('Ingrese el segundo numero: '))
    que_operacion(f_number, s_number)
    num = int(input('SI QUIERE DEJAR DE USAR LA CALCULADORA PRESIONE (1) \nSI QUIERE SEGUIR USANDOLA PRESIONE (2)\nSI QUIERE VER EL HISTORIAL PRESIONE (3), SI ELIGE ESTA OPCION LA CALCULADORA SEGUIRA FUNCIONANDO \n--> '))
    if num == 1:
        break
    elif num == 3:
        history()
        print('--------------------------')

    else:
        print('--------------------------')







'''
print('SUMA')
f_number = input('El primer numero es:') #primer numero
s_number = input('El segundo numero es:') # segundo numero
sumar =  float(f_number) + float(s_number)
print(sumar)

#RESTA
print('RESTA')
f_number = input('El primer numero es:') #primer numero
s_number = input('El segundo numero es:') # segundo numero
resta =  float(f_number) - float(s_number)
print(resta)

#MULTIPLICACION
print('MULTIPLICACION')
f_number = input('El primer numero es:') #primer numero
s_number = input('El segundo numero es:') # segundo numero
multiplicacion =  float(f_number) * float(s_number)
print(multiplicacion)

#DIVISION
print('DIVISION')
f_number = input('El primer numero es:') #primer numero
s_number = input('El segundo numero es:') # segundo numero
dividir =  float(f_number) / float(s_number)
print(dividir)

#POTENCIA
print('POTENCIA')
import
f_number = input('La base es:') #primer numero
s_number = input('El exponente es:') # segundo numero
potencia =  float(f_number) ** float(s_number)
print(potencia)

#RAIZ CUADRADA
print('RAIZ CUADRADA')
import math
f_number = input('El numero es:') #primer numero
raiz_Cuadrada = math.sqrt(float(f_number))

print(raiz_Cuadrada)
'''