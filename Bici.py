class Vehiculo:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca              # Atributo publico
        self.tipo = tipo                # Atributo publico
        self._modelo = modelo           # Atributo protegido
        self.__numero_serie = 777       # Atributo privado

    def encender(self):
        print(self._modelo + " ha sido puesto en marcha.")

    def apagar(self):
        print(self._modelo + " se ha apagado correctamente.")

    def mover(self, velocidad):
        print(f"{self._modelo} se mueve a {velocidad} km/h.")


# Clase Bicicleta (hija)
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo, rodada, piñones):
        super().__init__(marca, modelo, tipo)
        self.tipo = tipo             # Publico
        self.piñones = piñones       # Publico
        self._rodada = rodada        # Protegido
        self.__kilometraje = 0       # Privado

    # Métodos
    def pedalear(self, pedalazo):
        print(f"La bicicleta da {pedalazo} pedalazos por minuto.")

    def frenar(self, intensidad_freno):
        print(f"La bicicleta tiene una intensidad de freno de {intensidad_freno}.")

    def cambiar_marcha(self, marcha):
        print(f"Cambiando a marcha {marcha} en pendiente.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self._modelo}, Tipo: {self.tipo}, Rodada: {self._rodada}")

    def servicio(self, bici):
        print(f"La bicicleta {bici} ha sido engrasada y recibido mantenimiento.")


# Polimorfismo
class Bicicleta_electrica(Vehiculo):
    def mover(self, velocidad):
        print(f"La bici alcanza velocidades de hasta {velocidad} km/h.")


# Uso
bici = Bicicleta("Trek", "FX 2", "Montaña", 29, 7)
bici.mover(15)
bici.pedalear(75)
bici.cambiar_marcha(2)
bici.mostrar_info()
bici.servicio(bici._modelo)

bici_e = Bicicleta_electrica("HONEYWHALE", "S8", "Bici Electrica")
bici_e.mover(45)   

