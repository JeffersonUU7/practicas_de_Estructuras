class NodoProceso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class PlanificadorSO:
    def __init__(self):
        self.cabeza = None

    def agregar_proceso(self, nombre):
        nuevo_proceso = NodoProceso(nombre)
        # Si la lista está vacía, el proceso se apunta a sí mismo
        if not self.cabeza:
            self.cabeza = nuevo_proceso
            nuevo_proceso.siguiente = self.cabeza
        else:
            # Buscamos el último nodo para conectarlo con el nuevo
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            
            # Reconectamos los punteros para mantener el ciclo
            actual.siguiente = nuevo_proceso
            nuevo_proceso.siguiente = self.cabeza

    def simular_ejecucion(self, total_vueltas):
        if not self.cabeza:
            print("No hay procesos en el planificador.")
            return

        actual = self.cabeza
        vueltas_completadas = 0

        print(f"--- Iniciando planificador ({total_vueltas} vueltas) ---")
        # El ciclo se detiene cuando alcancemos las vueltas indicadas
        while vueltas_completadas < total_vueltas:
            print(f"Ejecutando: {actual.nombre}")
            actual = actual.siguiente
            
            # Si regresamos a la cabeza, significa que completamos una vuelta entera
            if actual == self.cabeza:
                vueltas_completadas += 1
                print(f"--> Ciclo {vueltas_completadas} completado\n")

# Prueba
scheduler = PlanificadorSO()
scheduler.agregar_proceso("Navegador Web")
scheduler.agregar_proceso("Reproductor de Música")
scheduler.agregar_proceso("Editor de Texto")
scheduler.agregar_proceso("Antivirus")

# Simulamos 3 vueltas completas
scheduler.simular_ejecucion(3)