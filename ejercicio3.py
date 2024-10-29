import streamlit as st

# Contraseña correcta
PASSWORD = "asdasd"

def main():
    st.title("Verificación de Contraseña")

    # Pedir la contraseña al usuario
    password = st.text_input("Introduce la contraseña:", type="password")

    if st.button("Verificar"):
        if password == PASSWORD:
            st.success("Bienvenido")
            # Limpiar el input desactivando el botón para simular la finalización
            st.stop()
        else:
            st.error("Contraseña incorrecta. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
