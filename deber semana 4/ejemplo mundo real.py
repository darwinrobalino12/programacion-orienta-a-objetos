# Sistema básico para controlar computadoras en un cyber

class Computadora:
    # Representa una computadora en el cyber
    def __init__(self, id_computadora):
        self.id = id_computadora  # Identificador de la computadora
        self.ocupada = False  # Estado: True si está en uso, False si está libre
        self.tiempo_inicio = 0  # Momento en que empieza a usarse

    def iniciar(self, tiempo):
        # Inicia el uso de la computadora
        if not self.ocupada:
            self.ocupada = True
            self.tiempo_inicio = tiempo  # Registra el tiempo de inicio
            print(f"Computadora {self.id} en uso desde el minuto {tiempo}.")
        else:
            print(f"Computadora {self.id} ya está ocupada.")

    def finalizar(self, tiempo, tarifa):
        # Finaliza el uso y calcula el costo
        if self.ocupada:
            tiempo_usado = tiempo - self.tiempo_inicio  # Calcula el tiempo usado
            costo = tiempo_usado * tarifa  # Calcula el costo total
            self.ocupada = False  # Libera la computadora
            print(f"Computadora {self.id} liberada. Tiempo usado: {tiempo_usado} minutos. Costo: ${costo:.2f}.")
        else:
            print(f"Computadora {self.id} no está en uso.")

class CyberCafe:
    # Representa el cyber y administra las computadoras
    def __init__(self, tarifa):
        self.computadoras = []  # Lista de computadoras en el cyber
        self.tarifa = tarifa  # Tarifa por minuto

    def agregar_computadora(self, id_computadora):
        # Agrega una nueva computadora al cyber
        self.computadoras.append(Computadora(id_computadora))
        print(f"Se agregó la computadora {id_computadora}.")

    def iniciar_computadora(self, id_computadora, tiempo):
        # Inicia el uso de una computadora
        for pc in self.computadoras:
            if pc.id == id_computadora:  # Busca la computadora por ID
                pc.iniciar(tiempo)
                return
        print(f"No se encontró la computadora {id_computadora}.")

    def finalizar_computadora(self, id_computadora, tiempo):
        # Finaliza el uso de una computadora
        for pc in self.computadoras:
            if pc.id == id_computadora:  # Busca la computadora por ID
                pc.finalizar(tiempo, self.tarifa)
                return
        print(f"No se encontró la computadora {id_computadora}.")

# Ejemplo de uso
cyber = CyberCafe(tarifa=0.5)  # Crea un cyber con tarifa de $0.50 por minuto

cyber.agregar_computadora(1)  # Agrega computadora 1
cyber.agregar_computadora(2)  # Agrega computadora 2

cyber.iniciar_computadora(1, 10)  # Inicia el uso de la computadora 1 a los 10 minutos
cyber.finalizar_computadora(1, 50)  # Finaliza el uso de la computadora 1 a los 50 minutos

cyber.iniciar_computadora(2, 60)  # Inicia el uso de la computadora 2 a los 60 minutos
cyber.finalizar_computadora(2, 120)  # Finaliza el uso de la computadora 2 a los 120 minutos
