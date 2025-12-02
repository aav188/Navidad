import random
import os
import time
import platform

# Función para limpiar pantalla (funciona en Windows, Linux y Mac)
def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def amigo_invisible_secreto():
    limpiar_pantalla()
    print("=== AMIGO INVISIBLE SÚPER SECRETO ===\n")
    
    # Pedir los 5 nombres
    print("Ingresa los 5 nombres de los participantes:")
    nombres = []
    for i in range(1, 6):
        while True:
            nombre = input(f"  Nombre {i}/5: ").strip()
            if nombre and nombre not in nombres:
                nombres.append(nombre)
                break
            elif not nombre:
                print("   ¡No puede estar vacío!")
            else:
                print("   ¡Ese nombre ya está en la lista!")
    
    # Hacer el sorteo secreto (círculo perfecto)
    sorteo = nombres.copy()
    random.shuffle(sorteo)
    asignaciones = {}
    for i in range(5):
        asignaciones[sorteo[i]] = sorteo[(i + 1) % 5]
    
    limpiar_pantalla()
    print("¡Sorteo realizado! Ahora cada uno descubrirá su amigo invisible...\n")
    input("Presiona Enter cuando todos estén listos y lejos de la pantalla...")
    
    while True:
        limpiar_pantalla()
        print("═" * 50)
        print("        AMIGO INVISIBLE - MODO SECRETO")
        print("═" * 50)
        print()
        nombre = input("Escribe tu nombre exacto → ").strip()
        
        if nombre.lower() == "salir":
            limpiar_pantalla()
            print("¡Gracias por jugar! 🎄¡Feliz amigo invisible!\n")
            time.sleep(2)
            break
        
        if nombre in asignaciones:
            regalas_a = asignaciones[nombre]
            
            limpiar_pantalla()
            print("\n" + "═" * 50)
            print(f"        ¡Hola {nombre.upper()}! 🎅")
            print("═" * 50)
            print()
            print("          Preparando tu resultado...")
            time.sleep(2)
            
            limpiar_pantalla()
            print("\n\n\n")
            print(" " * 15 + "¡TE TOCÓ REGALARLE A...!")
            print()
            print(" " * 20 + f"🎁  {regalas_a.upper()}  🎁")
            print("\n\n\n")
            print("           (se borrará en 5 segundos...)")
            
            time.sleep(5)  # 5 segundos de gloria
            
            # Borra todo para el siguiente
            limpiar_pantalla()
            print("Pantalla limpiada. Siguiente persona por favor...\n")
            time.sleep(1.5)
            
        else:
            print("Nombre no encontrado. Revisa mayúsculas/minúsculas.")
            time.sleep(2)

# Ejecutar
if __name__ == "__main__":
    amigo_invisible_secreto()