import streamlit as st
import os
from google import genai
from google.genai import types

st.set_page_config(page_title="Asistente IA Generativa", layout="wide")

# Inicializar el historial de chat si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# BARRA LATERAL: Limpia y exclusiva para opciones de usuario
st.sidebar.title("Opciones")
if st.sidebar.button("Limpiar Conversación"):
    st.session_state.messages = []
    st.rerun()

# CUERPO PRINCIPAL DE LA APLICACIÓN
st.title("🤖 Mi Primer Asistente de IA Generativa")

# 1. Recuperar la API Key de forma interna y segura (desde el sistema operativo o Streamlit Secrets)
# Primero busca en las variables del sistema, si no, busca en los secretos locales de Streamlit
api_key_servidor = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not api_key_servidor:
    st.error("Error de configuración: La API Key no ha sido configurada en el servidor por el administrador.")
else:
    # Mostrar el historial de la conversación
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Caja de entrada del chat (Disponible inmediatamente para cualquier usuario)
    if prompt := st.chat_input("¿En qué puedo ayudarte hoy?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Pensando...")
            
            try:
                # Inicializar el cliente usando la llave oculta del servidor
                client = genai.Client(api_key=api_key_servidor)
                
                # Formatear el historial previo
                historial_google = []
                for m in st.session_state.messages[:-1]:
                    rol_formateado = "user" if m["role"] == "user" else "model"
                    historial_google.append(
                        types.Content(
                            role=rol_formateado,
                            parts=[types.Part.from_text(text=m["content"])]
                        )
                    )
                
                # Sesión de chat nativa
                chat = client.chats.create(
                    model="gemini-3.5-flash-lite",
                    history=historial_google
                )
                
                # Enviar mensaje
                response = chat.send_message(prompt)
                
                message_placeholder.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
            except Exception as e:
                message_placeholder.error(f"Ocurrió un error al conectar con Gemini: {str(e)}")
