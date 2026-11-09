# 🤖 Asistente Virtual con IA Generativa (Gemini 3.8 Flash)

Este proyecto consiste en el desarrollo y despliegue de un chatbot interactivo basado en Inteligencia Artificial Generativa. Desarrollado como un trabajo académico para demostrar el ciclo completo de software: desde la configuración local, manejo de SDKs modernos, hasta la implementación segura de credenciales en producción.

🚀 **Acceso a la App en Vivo:** [https://asistenteiagenerativa-dx2vyypyc2vz4vl7jogaax.streamlit.app/]

## 🛠️ Tecnologías Utilizadas
* **Python 3.13** (Entorno de ejecución principal).
* **Streamlit** (Framework para la interfaz de usuario web).
* **Google GenAI SDK** (Librería oficial de Google para la conexión con modelos fundacionales).
* **Gemini 3.8 Flash** (Modelo de lenguaje para el procesamiento de respuestas).

## 📈 Resumen del Proceso de Ingeniería
1. **Aislamiento de Entorno:** Configuración de un entorno virtual `.venv` para mitigar el error `externally-managed-environment` (PEP 668).
2. **Estructura del Historial:** Implementación de memoria de conversación nativa usando las estructuras del nuevo SDK de Google, permitiendo un flujo de chat continuo.
3. **Seguridad Arquitectónica:** Migración de llaves hardcodeadas en interfaz hacia un esquema cerrado de Variables de Entorno (`os.environ` y `st.secrets`), garantizando que la API Key permanezca oculta en el servidor y el repositorio sea completamente seguro para el público.
4. **CI/CD con Streamlit Cloud:** Integración con GitHub para despliegue automático ante cambios en la rama `main`.

## 📦 Archivos Clave del Repositorio
* `app.py`: Código lógico de la interfaz, el historial y las llamadas a la API de Google.
* `requirements.txt`: Lista de dependencias del sistema requeridas para la compilación del contenedor en la nube.
