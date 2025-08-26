# Importaciones y carga de reglas
import json
import streamlit as st
from fuzzywuzzy import fuzz

# Lee el archivo rules.json que contiene las reglas y se guarda en variable
datos_json = open("rules.json").read()
reglas = json.loads(datos_json)

# Configuración inicial de la interfaz
# state es la memoria del chatbot
st.title("Asistente Virtual Restaurant")
st.markdown("##### Chatbot basado en reglas")
state = st.session_state

# Función para generar el menú inicial
def opciones_menu():
    mensaje_inicio = reglas["inicio"]["pregunta"]  
    menu = []
    for opcion, desc in reglas["inicio"]["opciones"].items():  
        menu.append(f"* {opcion}. {desc}") 
    return f"{mensaje_inicio}\n" + "\n".join(menu)  
 
# Función para procesar pedidos con coincidencia difusa
def pedido(term):
    opciones = reglas["2"]["opciones"]
    prompt_minuscula = term.lower()  
    mejor_coincidencia = None
    mejor_puntaje = 0

    for opcion in opciones:  # Compara la entrada con cada opción disponible
        puntaje = fuzz.ratio(prompt_minuscula, opcion)  # Calcula la similitud (0-100)
        if puntaje > mejor_puntaje:  # Guarda la opción con mayor similitud
            mejor_puntaje = puntaje
            mejor_coincidencia = opcion

    if mejor_puntaje >= 80:  # Si la similitud es alta (≥80), usa la opción encontrada
        escribir(opciones[mejor_coincidencia])
        state.actual = mejor_coincidencia  # Actualiza el estado al nombre de la opción
    else:  
        escribir(reglas["no_entendido"]["respuesta"])

# Función para agregar mensajes
def escribir(term, role="assistant"):
    state.historial.append({"role": role, "mensaje": term})  

# Definición de las opciones de respuestas del menú en el estado inicial
opciones_inicio = {
    "1": reglas["1"]["respuesta"],
    "2": reglas["2"]["respuesta"],
    "3": reglas["3"]["respuesta"],
    "4": opciones_menu(),
}

# Función principal del chatbot
def main():
    if "historial" not in state:  # Inicializa el historial y el estado si no existen
        state.historial = []
        state.actual = "inicio"
        escribir(opciones_menu())  

    if prompt := st.chat_input("Escribe aquí..."):  # Captura la entrada del usuario
        escribir(prompt, "user")  # Registra la entrada del usuario en el historial

        if state.actual == "inicio":  
            if prompt in opciones_inicio:  
                escribir(opciones_inicio[prompt])  
                if prompt == "2":  
                    state.actual = "pedido"
            else:  
                escribir(reglas["no_entendido"]["respuesta"])
        elif state.actual == "pedido":  
            pedido(prompt)  
        else:  
            escribir("🫃 " + reglas["tomar_pedido"]["respuesta"])
            state.actual = "inicio"

    # Muestra todos los mensajes del historial
    for chat in state.historial:  
        with st.chat_message(chat["role"]):
            st.markdown(chat["mensaje"])

# Punto de entrada del programa
if __name__ == "__main__":
    main()
