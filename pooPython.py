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
#--------------------------------------------------------------------------------------------
#Herencia
class vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print("marca:", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class furgoneta(vehiculo):
    def carga(self,carga):
        self.cargado=carga
        if(self.cargago):
            return "La furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"
    

class moto(vehiculo):
    hacecaballito=""
    def caballito(self):
        self.hacecaballito="Voy haciendo caballito"
    def estado(self):
        print("marca:", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hacecaballito)


   
mimoto=moto("Honda", "CBR")
mimoto.caballito()
mimoto.estado()

mifurgoneta=furgoneta("toyota", "DFG")
