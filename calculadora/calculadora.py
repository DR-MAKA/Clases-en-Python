#Crear una clase que implemente una calculadora aritmetica 
#Funciones sumar, restar, modulo, potenciacion

#Definimos la clase calculadora 
class calculadora:
#a y b seran los numeros que el usiario ingrese para hacer las operaciones     
    a=0
    b=0
#la palabra clave self para especificar que estamos pasando el valor a los atributos de la instancia y no a la variable o argumento local con el mismo nombre.    
    def __init__(self,a,b):
        self.a=float(a)
        self.b=float(b)
    def sumar(self):
        suma = self.a+self.b
        print("el resultado de la suma es: ", suma)
    def restar(self):
        resta = self.a-self.b
        print("el resultado de la resta es: ", resta)
    def multiplicar(self):
        multiplicacion = self.a*self.b
        print("el resultado de la multiplicación es: ", multiplicacion) 
    def dividir(self):
         divicion = self.a/self.b
         print("el resultado de la divición es: ", divicion)

a=input("Ingrese un numero:")
b=input("Ingrese un numero:")
calculadora=calculadora(a,b)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()
