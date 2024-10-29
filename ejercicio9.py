import streamlit as st
import random

# Función para rellenar el array con valores aleatorios
def rellenar_array(tamaño):
    return [random.randint(1, 100) for _ in range(tamaño)]

# Función para copiar un array
def copiar_array(array):
    return array.copy()

# Función para ordenar el array por el método de burbuja
def ordenar_burbuja(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def main():
    st.title("Operaciones con Arrays")

    # Opciones del menú
    opcion = st.selectbox("Seleccione una opción:", [
        "Rellenar Array",
        "Copiar Array",
        "Mostrar Array",
        "Ordenar por Burbuja"
    ])

    # Tamaño del array
    tamaño = st.number_input("Tamaño del array:", min_value=1, step=1, value=10)
    
    # Almacenamiento del array en la sesión
    if "array" not in st.session_state:
        st.session_state["array"] = []
    if "copia_array" not in st.session_state:
        st.session_state["copia_array"] = []

    # Ejecutar la opción seleccionada
    if opcion == "Rellenar Array":
        st.session_state["array"] = rellenar_array(tamaño)
        st.success("Array rellenado con valores aleatorios.")

    elif opcion == "Copiar Array":
        if st.session_state["array"]:
            st.session_state["copia_array"] = copiar_array(st.session_state["array"])
            st.success("Array copiado exitosamente.")
        else:
            st.warning("Primero debe rellenar el array.")

    elif opcion == "Mostrar Array":
        if st.session_state["array"]:
            st.write("Array original:", st.session_state["array"])
            if st.session_state["copia_array"]:
                st.write("Copia del array:", st.session_state["copia_array"])
            else:
                st.warning("El array no ha sido copiado aún.")
        else:
            st.warning("Primero debe rellenar el array.")

    elif opcion == "Ordenar por Burbuja":
        if st.session_state["array"]:
            st.session_state["array"] = ordenar_burbuja(st.session_state["array"])
            st.success("Array ordenado con el método de burbuja.")
            st.write("Array ordenado:", st.session_state["array"])
        else:
            st.warning("Primero debe rellenar el array.")

if __name__ == "__main__":
    main()
