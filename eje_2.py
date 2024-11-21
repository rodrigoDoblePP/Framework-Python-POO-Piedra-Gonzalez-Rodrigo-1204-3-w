#Ejercicio 2
#Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
#titular (que es una persona) y cantidad (puede tener decimales)




class Cuenta:
    # Clase Cuenta para representar una cuenta bancaria con titular y saldo.

    def __init__(self, titular, cantidad=0.0):
        # Constructor de la clase.
        # Argumentos:
        # - titular: Nombre de la persona titular de la cuenta (obligatorio).
        # - cantidad: Saldo inicial de la cuenta (opcional, por defecto 0.0).
        self.titular = titular  # Atributo para almacenar el titular de la cuenta.
        self.__cantidad = cantidad  # Atributo privado para almacenar el saldo de la cuenta.

    # Getter para el atributo titular.
    def get_titular(self):
        # Devuelve el nombre del titular de la cuenta.
        return self.titular

    # Setter para el atributo titular.
    def set_titular(self, titular):
        # Permite establecer o modificar el nombre del titular.
        self.titular = titular

    # Getter para el atributo cantidad.
    def get_cantidad(self):
        # Devuelve el saldo actual de la cuenta.
        return self.__cantidad

    # Método para mostrar los datos de la cuenta.
    def mostrar(self):
        # Imprime los datos principales de la cuenta.
        print(f"Titular: {self.titular}, Cantidad: {self.__cantidad}")

    # Método para ingresar dinero en la cuenta.
    def ingresar(self, cantidad):
        # Aumenta el saldo si la cantidad ingresada es positiva.
        # Argumentos:
        # - cantidad: Monto a ingresar.
        if cantidad > 0:
            self.__cantidad += cantidad  # Incrementa el saldo.

    # Método para retirar dinero de la cuenta.
    def retirar(self, cantidad):
        # Reduce el saldo por el monto especificado. El saldo puede quedar negativo.
        # Argumentos:
        # - cantidad: Monto a retirar.
        self.__cantidad -= cantidad  # Disminuye el saldo.

# Ejemplo de uso:
cuenta = Cuenta("Tagleson martinez de la garza", 1000)
cuenta.mostrar()  # Muestra: Titular: , Cantidad: 1000
cuenta.ingresar(500)  # Ingresa 500.
cuenta.mostrar()  # Muestra: Titular: Tagleson martinez de la garza, Cantidad: 1500
cuenta.retirar(200)  # Retira 200.
cuenta.mostrar()  # Muestra: Titular: Tagleson martinez de la garza, Cantidad: 1300