# Algoritmo que pida números hasta que se introduzca un
#cero. Debe imprimir la suma y la media de todos los números introducidos.

import streamlit as st

# Lista para almacenar los números introducidos
if "numeros" not in st.session_state:
    st.session_state["numeros"] = []

def main():
    st.title("Suma y Media de Números")
    st.write("Introduce números. El programa terminará cuando introduzcas un cero.")
    
    # Entrada de número
    numero = st.number_input("Introduce un número:", step=1, format="%d", key="numero_input")

    if st.button("Agregar número"):
        if numero == 0:
            if st.session_state["numeros"]:
                # Cálculo de la suma y la media
                suma = sum(st.session_state["numeros"])
                media = suma / len(st.session_state["numeros"])
                st.write("**Suma de todos los números:**", suma)
                st.write("**Media de todos los números:**", media)
            else:
                st.write("No se introdujeron números.")
            # Limpiar la lista después de mostrar los resultados
            st.session_state["numeros"].clear()
        else:
            # Agregar número a la lista
            st.session_state["numeros"].append(numero)
            st.write("Números introducidos:", st.session_state["numeros"])

if __name__ == "__main__":
    main()
