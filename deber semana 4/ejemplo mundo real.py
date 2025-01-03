# Sistema básico para controlar computadoras en un cyber

class Computadora:
    def __init__(self, id_computadora):
        self.id = id_computadora
        self.ocupada = False
        self.tiempo_inicio = 0

    def iniciar(self, tiempo):
        if not self.ocupada:
            self.ocupada = True
            self.tiempo_inicio = tiempo
            print(f"Computadora {self.id} en uso desde el minuto {tiempo}.")
        else:
            print(f"Computadora {self.id} ya está ocupada.")

    def finalizar(self, tiempo, tarifa):
        if self.ocupada:
            tiempo_usado = tiempo - self.tiempo_inicio
            costo = tiempo_usado * tarifa
            self.ocupada = False
            print(f"Computadora {self.id} liberada. Tiempo usado: {tiempo_usado} minutos. Costo: ${costo:.2f}.")
        else:
            print(f"Computadora {self.id} no está en uso.")

class CyberCafe:
    def __init__(self, tarifa):
        self.computadoras = []
        self.tarifa = tarifa

    def agregar_computadora(self, id_computadora):
        self.computadoras.append(Computadora(id_computadora))
        print(f"Se agregó la computadora {id_computadora}.")

    def iniciar_computadora(self, id_computadora, tiempo):
        for pc in self.computadoras:
            if pc.id == id_computadora:
                pc.iniciar(tiempo)
                return
        print(f"No se encontró la computadora {id_computadora}.")

    def finalizar_computadora(self, id_computadora, tiempo):
        for pc in self.computadoras:
            if pc.id == id_computadora:
                pc.finalizar(tiempo, self.tarifa)
                return
        print(f"No se encontró la computadora {id_computadora}.")

# Ejemplo de uso
cyber = CyberCafe(tarifa=0.5)
cyber.agregar_computadora(1)
cyber.agregar_computadora(2)

cyber.iniciar_computadora(1, 10)
cyber.finalizar_computadora(1, 50)

cyber.iniciar_computadora(2, 60)
cyber.finalizar_computadora(2, 120)
