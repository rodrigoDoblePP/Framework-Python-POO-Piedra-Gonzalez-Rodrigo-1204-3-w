#Ejercicio 3
#Vamos a definir ahora una “Cuenta Joven”,
#para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior. 
#Cuando se crea esta nueva clase, además del titular 
#y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def retirar(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"Se ha retirado {cantidad} unidades.")
        else:
            print("No hay suficiente saldo para realizar la retirada.")
    
    def mostrar(self):
        print(f"Titular: {self.titular}, Saldo: {self.cantidad}")
    

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    # Getter y Setter para bonificación
    def get_bonificacion(self):
        return self.bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    
    # Método para validar si el titular es mayor de edad y menor de 25 años
    def es_titular_valido(self):
        # Asumimos que la edad del titular está en la forma (nombre, edad)
        if isinstance(self.titular, tuple) and len(self.titular) == 2:
            edad = self.titular[1]
            return 18 <= edad < 25
        return False
    
    # Sobreescribimos el método de retirar para agregar la validación
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede realizar la retirada. El titular no es válido para la Cuenta Joven.")
    
    # Método mostrar para la Cuenta Joven
    def mostrar(self):
        print(f"Cuenta Joven - Bonificación: {self.bonificacion}%")
        super().mostrar() 

# Ejemplo de uso:
# Crear una cuenta joven con titular (nombre, edad), saldo y bonificación
cuenta_joven = CuentaJoven(("Rodrigo", 23), 1000, 5)

# Mostrar la información de la cuenta
cuenta_joven.mostrar()

# Intentar retirar dinero
cuenta_joven.retirar(200)

# Cambiar la bonificación
cuenta_joven.set_bonificacion(10)

# Mostrar la información después de cambiar la bonificación
cuenta_joven.mostrar()
