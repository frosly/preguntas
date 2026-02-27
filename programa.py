import streamlit as st
import pandas as pd
import os

def cargar_datos():
    if os.path.exists("puntuaciones.csv"):
        return pd.read_csv("puntuaciones.csv")
    return pd.DataFrame(columns=["Nombre", "Puntos"])

def guardar_datos(nombre, puntos):
    df = cargar_datos()
    nuevo_registro = pd.DataFrame({"Nombre": [nombre], "Puntos": [f"{puntos}/6"]})
    df = pd.concat([df, nuevo_registro], ignore_index=True)
    df.to_csv("puntuaciones.csv", index=False)

def mostrar_trivia():
    st.title("🧠 Super Trivia Interactiva")
    
    # Inicializar estado del juego
    if 'paso' not in st.session_state:
        st.session_state.paso = 'inicio'
        st.session_state.puntos = 0
        st.session_state.pregunta_actual = 0

    if st.session_state.paso == 'inicio':
        nombre = st.text_input("Ingresa tu nombre para comenzar:")
        if st.button("Empezar Juego") and nombre:
            st.session_state.nombre = nombre
            st.session_state.paso = 'jugando'
            st.rerun()

    elif st.session_state.paso == 'jugando':
        preguntas = [
            {"p": "¿País con más copas del mundo?", "ops": ["Alemania", "Brasil", "Argentina"], "r": "Brasil"},
            {"p": "¿Planeta Rojo?", "ops": ["Marte", "Júpiter", "Venus"], "r": "Marte"},
            {"p": "¿Quién pintó la Mona Lisa?", "ops": ["Van Gogh", "Picasso", "Da Vinci"], "r": "Da Vinci"},
            {"p": "¿Animal terrestre más rápido?", "ops": ["Guepardo", "León", "Halcón"], "r": "Guepardo"},
            {"p": "¿Año del hundimiento del Titanic?", "ops": ["1912", "1905", "1920"], "r": "1912"},
            {"p": "¿Idioma más hablado del mundo?", "ops": ["Inglés", "Chino Mandarín", "Español"], "r": "Chino Mandarín"},
        ]

        i = st.session_state.pregunta_actual
        st.subheader(f"Pregunta {i+1}: {preguntas[i]['p']}")
        
        respuesta = st.radio("Selecciona una opción:", preguntas[i]['ops'], key=f"p{i}")
        
        if st.button("Siguiente"):
            if respuesta == preguntas[i]['r']:
                st.session_state.puntos += 1
            
            if i + 1 < len(preguntas):
                st.session_state.pregunta_actual += 1
                st.rerun()
            else:
                st.session_state.paso = 'final'
                guardar_datos(st.session_state.nombre, st.session_state.puntos)
                st.rerun()

    elif st.session_state.paso == 'final':
        puntos = st.session_state.puntos
        st.balloons()
        st.header(f"¡Terminaste, {st.session_state.nombre}!")
        st.write(f"Tu puntaje final es: **{puntos}/6**")
        
        if puntos >= 3:
            st.success("¡Felicitaciones! Lo hiciste genial. 🏆")
        else:
            st.error("No te rindas, sigue intentando. 💪")

        st.subheader("📜 Registro de Participantes")
        st.table(cargar_datos())

        if st.button("Reiniciar"):
            st.session_state.paso = 'inicio'
            st.session_state.puntos = 0
            st.session_state.pregunta_actual = 0
            st.rerun()
