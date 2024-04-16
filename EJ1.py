import os, time
        
class cajaDeAhorro:
    def __init__(self,nroCuenta,cuil,apellido,nombre,saldo):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = float(saldo)
    
    def __str__ (self): #MOSTRAR DATOS
        return f'Numero de cuenta: {self.__nroCuenta} \tCuil: {self.__cuil} \nApellido: {self.__apellido}\nNombre: {self.__nombre}\nSaldo: {self.__saldo}'
    
    def extraer(self,importe):
        importe = float(importe)
        if self.__saldo >= importe:
            self.__saldo -= importe
            print(f"Dinero retirado con exito. \nSaldo actual: {self.__saldo}")
        else: return -1
        
    def depositar(self,importe):
        importe = float(importe)
        if importe > 0:
            self.__saldo += importe
            print(f"Se ingresaron ${importe} con exito.\nSaldo actual: {self.__saldo}")
            
    def getCuil (self):
        return self.__cuil
    
    def validarCuil(self):
        if len(self.__cuil) != 11:
            print("El CUIL/T debe tener 11 dígitos.")
            return False

        sumador = 0
        multiplicadores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        
        for i in range(10):
            sumador += int(self.__cuil[i]) * multiplicadores[i]
            
        resto = sumador%11
        if resto == 0:
            digito_verificacion_calculado = 0
        elif  resto == 1:
            if self.__cuil[:2] == '20':
                digito_verificacion_calculado = 9
            elif self.__cuil[:2] == '27':
                digito_verificacion_calculado = 4
        else: digito_verificacion_calculado = 11 - resto

        if digito_verificacion_calculado == int(self.getCuil()[-1]):
            return True
        else: 
            return False
        
def test():
    cajasdeahorro = []
    for i in range(3):
        while True:
            try: 
                nrocuenta = int(input("Ingrese el numero de cuenta: "))
                cuil = input("Ingrese el Cuil/Cuit: ")
                apellido = input("Ingrese el apellido: ")
                nombre = input("Ingrese el nombre: ") 
                saldo = 0 
                
                caja = cajaDeAhorro(nrocuenta,cuil,apellido,nombre,saldo)
                
                if caja.validarCuil(): 
                    cajasdeahorro.append(caja)
                    break  # Sale del bucle while si la validación es exitosa
                else:
                    print("Error: El Cuil/Cuit ingresado no es válido. Por favor, inténtelo nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número para el número de cuenta y el Cuil/Cuit.")
                
    while True:
        clearScreen()
        flag = False
        cuilIngresar = input("Ingrese el cuil para acceder a la cuenta: ")
        for caja in cajasdeahorro:
            if caja.getCuil() == cuilIngresar and flag == False:
                while True:
                    print("\033[;36m"+"\n\n1. Depositar")
                    print("\033[;36m"+"2. Extraer")
                    print("\033[;36m"+"3. Salir")
                    opcion = int(input("Ingrese una opcion: "))
                        
                    if opcion == 1: 
                        clearScreen()
                        importe = input("Ingrese el importe a depositar: ")
                        caja.depositar(importe)
                    elif opcion == 2:
                        clearScreen()
                        importe = input("Ingrese el importe a extraer: ")
                        caja.extraer(importe)
                    elif opcion == 3:
                        print("Saliendo del sistema..")
                        time.sleep(1)
                        clearScreen()
                        flag = True
                        break
            if flag: break 
            else: print("El Cuil/Cuit ingresado no esta en el sistema. Por favor, intentelo nuevamente")

def clearScreen():
    os.system('cls')