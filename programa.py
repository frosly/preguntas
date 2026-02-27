import os

def ejecutar_trivia():
    preguntas = [
        {"pregunta": "¿Cuál es el país con más copas del mundo de fútbol?", "opciones": ["A) Alemania", "B) Brasil", "C) Argentina"], "respuesta": "B"},
        {"pregunta": "¿Cuál es el único país del mundo que ocupa todo un continente?", "opciones": ["A) Rusia", "B) Australia", "C) Antártida"], "respuesta": "B"},
        {"pregunta": "¿Quién pintó la Mona Lisa?", "opciones": ["A) Van Gogh", "B) Picasso", "C) Da Vinci"], "respuesta": "C"},
        {"pregunta": "¿Cuál es el animal terrestre más rápido?", "opciones": ["A) Guepardo", "B) León", "C) Halcón"], "respuesta": "A"},
        {"pregunta": "¿En qué año se hundió el Titanic?", "opciones": ["A) 1912", "B) 1905", "C) 1920"], "respuesta": "A"},
        {"pregunta": "¿Cuál es el elemento más abundante en el universo?", "opciones": ["A) Oxígeno", "B) Helio", "C) Hidrógeno"], "respuesta": "C"},
    ]

    print("--- 🧠 BIENVENIDO A LA SUPER TRIVIA 🧠 ---")
    nombre = input("Ingresa tu nombre para comenzar: ").strip()
    
    puntos = 0
    total = len(preguntas)

    for i, p in enumerate(preguntas):
        print(f"\nPregunta {i+1}: {p['pregunta']}")
        for opcion in p['opciones']:
            print(opcion)
        
        respuesta_usuario = input("Tu respuesta (A, B o C): ").upper()
        
        if respuesta_usuario == p['respuesta']:
            print("¡Correcto! ✅")
            puntos += 1
        else:
            print(f"Incorrecto ❌. La respuesta era {p['respuesta']}")

    # Lógica de mensajes finales
    porcentaje = (puntos / total) * 100
    print("\n" + "="*30)
    print(f"RESULTADO: {puntos}/{total}")
    
    if porcentaje >= 50:
        print(f"¡Felicitaciones, {nombre}! Lo hiciste genial. 🏆")
    else:
        print(f"No te rindas, {nombre}, sigue intentando. 💪")
    print("="*30)

    # Guardar en el registro
    with open("puntuaciones.txt", "a", encoding="utf-8") as f:
        f.write(f"Jugador: {nombre} | Puntos: {puntos}/{total}\n")

    mostrar_historial()

def mostrar_historial():
    print("\n--- 📜 REGISTRO DE PARTICIPANTES ---")
    if os.path.exists("puntuaciones.txt"):
        with open("puntuaciones.txt", "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Aún no hay registros.")

def menu():
    while True:
        ejecutar_trivia()
        repetir = input("\n¿Quieres volver a jugar? (s/n): ").lower()
        if repetir != 's':
            print("¡Gracias por jugar! Adiós.")
            break