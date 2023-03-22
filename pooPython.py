#Practica de POO en Python
class laptop():
    #Constructor
    def __init__(self):
        self.pantallaPulg=11
        self.teclado="ISO"
        self.ramGB=16
        self.gpuName="Rtx2080"
        #Encapsular
        self.__encendido=False
    def encender(self):
        self.__encendido=True
    def caracteristicas(self):
        print("La alptop cuenta con una pantalla de " + str(self.pantallaPulg))


milaptop=laptop()
milaptop.caracteristicas()




