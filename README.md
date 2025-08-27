# Teacher AI Chatbot Rules 🤖

[![Python Version](https://img.shields.io/badge/python–3.10-blue)]()  
[![License: MIT](https://img.shields.io/badge/license-MIT-green)]()

Bienvenido/a al repositorio **Teacher AI Chatbot Rules** 👋

Este proyecto demuestra cómo implementar un **chatbot con reglas personalizadas** en **Python**, combinando:

- **JSON** (`rules.json`) como base de conocimiento para definir las reglas de interacción.
- **FuzzyWuzzy** para el **emparejamiento flexible de texto**, lo que permite reconocer la intención del usuario aunque no escriba exactamente igual a la regla.
- **Streamlit** para una **interfaz web interactiva** que muestra el flujo de conversación y la aplicación de reglas en tiempo real.
- Un **árbol de decisión** (`decision-tree.png`) que visualiza de forma gráfica cómo se recorren las reglas y respuestas.

El flujo básico es:

1. El usuario ingresa un mensaje en la interfaz en base a opciones predefinidas.
2. El sistema compara la entrada con las reglas en `rules.json` usando similitud difusa (**FuzzyWuzzy**).
3. Se selecciona la respuesta más adecuada según el puntaje de coincidencia.
4. El chatbot responde y Streamlit actualiza la vista mostrando la lógica aplicada.

---

## Árbol de decisión

![Árbol de decisión](./decision-tree.png)

---

## Contenido del proyecto

- `main.py`: Lógica principal para procesar la interacción del chatbot.
- `rules.json`: Conjunto de reglas configurables que dan forma al comportamiento del bot.
- `decision-tree.png`: Diagrama visual con el árbol de decisiones que el bot sigue.
- `requirements.txt`: Dependencias necesarias para ejecutar el sistema.

---

## Instalación

```bash
git clone https://github.com/julioavantt/teacher_ai_chatbot_rules.git
cd teacher_ai_chatbot_rules
python3 -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt



```
