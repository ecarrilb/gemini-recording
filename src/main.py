import streamlit as st

# formulario
@st.fragment
def formData():
    with st.form(key="my_form"):
        st.write("Configuración del chatbot")
        filePdf = st.file_uploader("Subir el Curriculum Vitae", type=["pdf"])
        fileAudio = st.file_uploader("Subir la llamada telefonica", type=["mp3", "wav", "m4a"])
        btnSend = st.form_submit_button("Enviar")

def main():
    st.set_page_config(page_title="🤖🔗 Quickstart App")

    #variables
    prompt = st.chat_input("Di algo...")

    # Contenido del chatbot
    st.title("Galaxy AI Chat Taento Humano")
    with st.sidebar:
        formData()
    if prompt:
        st.write(f"El usuario envió el siguiente prompt: {prompt}")

if __name__ == "__main__":
    main()