import json
from datetime import datetime

# === MODELOS (CLASES) ===
class Interes:
    def __init__(self, nombre, moda=0):
        self.nombre = nombre
        self.moda = moda

    def incrementar(self):
        self.moda += 1

    def decrementar(self):
        self.moda = max(0, self.moda - 1)

    def to_dict(self):
        return {"nombre": self.nombre, "moda": self.moda}

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.intereses = {}

    def agregar_interes(self, nombre, moda=1):
        if nombre not in self.intereses:
            self.intereses[nombre] = Interes(nombre, moda)
        else:
            self.intereses[nombre].incrementar()

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "intereses": [i.to_dict() for i in self.intereses.values()]
        }

class Miembro:
    def __init__(self, usuario, colonia):
        self.usuario = usuario
        self.colonia = colonia

class Colonia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []
        self.intereses = {}

    def agregar_miembro(self, usuario):
        miembro = Miembro(usuario, self)
        self.miembros.append(miembro)

    def agregar_interes(self, nombre, moda=1):
        if nombre not in self.intereses:
            self.intereses[nombre] = Interes(nombre, moda)
        else:
            self.intereses[nombre].incrementar()

    def decrementar_interes(self, nombre):
        if nombre in self.intereses:
            self.intereses[nombre].decrementar()

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "intereses": [i.to_dict() for i in self.intereses.values()]
        }


class Chat:
    def __init__(self, emisor, receptor):
        self.emisor = emisor
        self.receptor = receptor
        self.mensajes = []

    def enviar(self, texto):
        self.mensajes.append({"de": self.emisor, "texto": texto})
        print(f"💬 {self.emisor} → {self.receptor}: {texto}")

# === SIMULACIÓN ===
def simulacion_empatia():
    print("🔍 Iniciando simulación de empatía...\n")

    # Crear colonia
    colonia = Colonia("Amantes de Lima")

    # Crear usuarios con intereses
    ana = Usuario("Ana")
    ana.agregar_interes("surf", 39)
    ana.agregar_interes("yoga", 20)

    beto = Usuario("Beto")
    beto.agregar_interes("surf", 19)
    beto.agregar_interes("gastronomia", 10)

    # Agregar a la colonia
    colonia.agregar_miembro(ana)
    colonia.agregar_miembro(beto)

    # Agregar intereses a la colonia
    for interes in ana.intereses.values():
        colonia.agregar_interes(interes.nombre, interes.moda)
    for interes in beto.intereses.values():
        colonia.agregar_interes(interes.nombre, interes.moda)

    print("Estado inicial:")
    print(json.dumps(colonia.to_dict(), indent=2, ensure_ascii=False))

    # Simular 5 interacciones
    print("\n💬 Simulando 5 interacciones entre Ana y Beto...\n")
    chat = Chat("Ana", "Beto")
    # 5 mensajes de ejemplo
    mensajes = [
        "¡Hola! ¿Conoces algún buen lugar de surf por aquí?",
        "Sí, hay una playa escondida a 10 min. ¿Te gustaría ir?",
        "¡Claro! También me encanta la gastronomía después de surfear.",
        "Perfecto, conozco un food-truck cerca que tiene tacos increíbles.",
        "¡Genial! Quedamos para surf + tacos este fin de semana."
    ]
    for texto in mensajes:
        chat.enviar(texto)

    # Detectar intereses comunes
    intereses_comunes = set(ana.intereses.keys()) & set(beto.intereses.keys())
    print(f"\nIntereses comunes detectados: {intereses_comunes}")

    # Sugerir interés con mayor moda del otro
    max_ana = max(ana.intereses.values(), key=lambda x: x.moda)
    max_beto = max(beto.intereses.values(), key=lambda x: x.moda)

    print(f"\nAna sugiere a Beto: {max_ana.nombre}")
    print(f"Beto sugiere a Ana: {max_beto.nombre}")

    # Aceptan ambos
    print("\nAmbos aceptan la sugerencia.\n")
    beto.agregar_interes(max_ana.nombre)
    ana.agregar_interes(max_beto.nombre)
    colonia.agregar_interes(max_ana.nombre)
    colonia.agregar_interes(max_beto.nombre)

    # Mostrar estado final
    print("Estado final:")
    resultado = {
        "colonia": colonia.to_dict(),
        "usuarios": [ana.to_dict(), beto.to_dict()]
    }
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

    # Guardar los resultados en un archivo JSON
    with open("output_ejemplo.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    print("\nSimulación guardada en 'output_ejemplo.json'")

# === EJECUCIÓN ===
if __name__ == "__main__":
    simulacion_empatia()