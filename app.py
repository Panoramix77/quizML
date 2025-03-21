import streamlit as st
import random

# Lista de preguntas
quiz = [
    {
        "question": "¿Con qué conjunto de datos se deben calcular las métricas a la hora de comparar el funcionamiento de los modelos?",
        "options": ["Conjunto de validación", "Conjunto de entrenamiento", "Conjunto de test", "Todo el conjunto de datos"],
        "correct": 3
    },
    {
        "question": "¿Qué es la validación cruzada?",
        "options": [
            "Una técnica para dividir el conjunto de datos en entrenamiento y prueba",
            "Una técnica para evaluar el rendimiento del modelo utilizando múltiples divisiones del conjunto de datos",
            "Una técnica para aumentar el tamaño del conjunto de datos mediante la generación de datos sintéticos",
            "Una técnica para aumentar el tamaño del conjunto de datos mediante la generación de datos atípicos"
        ],
        "correct": 2
    },
    {
        "question": "¿Cuál de las siguientes tareas se clasifica como aprendizaje no supervisado?",
        "options": [
            "Clasificación de imágenes",
            "Predicción de precios de acciones",
            "Agrupamiento de documentos en categorías sin etiquetas previas",
            "La a y la b son correctas"
        ],
        "correct": 3
    },
    {
        "question": "¿Cuál de las siguientes funciones de activación se utiliza comúnmente en una capa de salida para problemas de clasificación binaria en machine learning?",
        "options": ["RELU (Rectified Linear Unit)", "Sigmoid", "Tanh", "Softmax"],
        "correct": 2
    },
    {
        "question": "¿Qué es el overfitting en machine learning?",
        "options": [
            "Un modelo que se ajusta perfectamente a los datos de entrenamiento",
            "Un modelo que se ajusta perfectamente a los datos de entrenamiento pero no generaliza bien a nuevos datos",
            "Un modelo que subestima la complejidad de los datos",
            "Un modelo que no tiene capacidad de aprender"
        ],
        "correct": 2
    },
    {
        "question": "¿Cuál de las siguientes técnicas se utiliza para preprocesar datos en machine learning y reducir la dimensionalidad?",
        "options": ["Regresión lineal", "Clustering", "Análisis de componentes principales (PCA)", "Gradiente descendente"],
        "correct": 3
    },
    {
        "question": "¿Cuál es el objetivo del algoritmo de agrupamiento (clustering) en machine learning?",
        "options": [
            "Predecir una variable continua",
            "Asignar etiquetas a nuevas instancias",
            "Encontrar patrones y estructuras subyacentes en los datos",
            "Ajustar una línea de mejor ajuste a los datos"
        ],
        "correct": 3
    },
    {
        "question": "¿Cuál es la diferencia entre aprendizaje supervisado y no supervisado?",
        "options": [
            "El aprendizaje supervisado no utiliza etiquetas de datos",
            "En el aprendizaje no supervisado, el modelo no se entrena",
            "El aprendizaje supervisado utiliza etiquetas para entrenar el modelo, mientras que el no supervisado no lo hace",
            "No hay diferencia, son términos intercambiables"
        ],
        "correct": 3
    },
    {
        "question": "¿Cuál es la función de pérdida comúnmente utilizada en problemas de regresión?",
        "options": ["Entropía cruzada", "Mean Squared Error (MSE)", "Log-Loss", "Precisión"],
        "correct": 2
    },
    {
        "question": "¿Qué es el bagging en machine learning?",
        "options": [
            "Una técnica de aumento de datos",
            "Un método para combinar múltiples modelos débiles para formar un modelo fuerte",
            "Un algoritmo de aprendizaje no supervisado",
            "Una función de activación en redes neuronales"
        ],
        "correct": 2
    },
    {
        "question": "¿Qué es la precisión (accuracy) en el contexto de machine learning?",
        "options": [
            "La cantidad de información que el modelo puede aprender",
            "La capacidad del modelo para generalizar a nuevos datos",
            "El número total de predicciones correctas dividido por el número total de predicciones",
            "La medida de cuán bien se ajusta el modelo a los datos de entrenamiento"
        ],
        "correct": 3
    },
    {
        "question": "¿En un problema de clasificación con más de dos clases, cuál es la función de activación comúnmente utilizada en la capa de salida?",
        "options": ["ReLU", "Sigmoid", "Softmax", "Tanh"],
        "correct": 3
    },
    {
        "question": "¿Qué es el aprendizaje por refuerzo en machine learning?",
        "options": [
            "Un tipo de aprendizaje supervisado",
            "Un enfoque para prevenir el overfitting",
            "Un método donde un agente aprende tomando decisiones en un entorno y recibe recompensas o penalizaciones",
            "Un algoritmo de clasificación"
        ],
        "correct": 3
    },
    {
        "question": "¿Qué es la matriz de confusión en problemas de clasificación?",
        "options": [
            "Una representación gráfica de los datos",
            "Una matriz que muestra el número de verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos",
            "Un método para reducir la complejidad del modelo",
            "Un tipo de regularización"
        ],
        "correct": 2
    },
    {
        "question": "¿En un problema de aprendizaje no supervisado, cuál es el objetivo principal?",
        "options": [
            "Predecir una variable de salida",
            "Encontrar patrones y estructuras ocultas en los datos",
            "Clasificar nuevas instancias en categorías predefinidas",
            "Ajustar un modelo a los datos de entrenamiento"
        ],
        "correct": 2
    }
]

# Mezclar preguntas y opciones al cargar la app
if 'quiz' not in st.session_state:
    st.session_state.quiz = quiz.copy()
    random.shuffle(st.session_state.quiz)
    for q in st.session_state.quiz:
        q["options_shuffled"] = q["options"].copy()
        random.shuffle(q["options_shuffled"])
        q["correct_index"] = q["options_shuffled"].index(q["options"][q["correct"] - 1]) + 1
    st.session_state.score = 0
    st.session_state.submitted = False

# Interfaz de la app
st.title("¡Test Interactivo de Machine Learning!")

for i, q in enumerate(st.session_state.quiz, 1):
    st.subheader(f"Pregunta {i}: {q['question']}")
    answer = st.radio("Selecciona una opción", q["options_shuffled"], key=f"q{i}")
    q["user_answer"] = answer

if st.button("Enviar respuestas"):
    st.session_state.submitted = True
    for q in st.session_state.quiz:
        if q["options_shuffled"].index(q["user_answer"]) + 1 == q["correct_index"]:
            st.session_state.score += 1

if st.session_state.submitted:
    percentage = (st.session_state.score / len(st.session_state.quiz)) * 100
    st.success(f"Test finalizado. Tu puntuación: {st.session_state.score}/{len(st.session_state.quiz)}")
    st.write(f"Porcentaje de aciertos: {percentage:.2f}%")
    if st.button("Reiniciar"):
        st.session_state.clear()
        st.experimental_rerun()
