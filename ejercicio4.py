import streamlit as st

# Lista para almacenar los puntos contaminantes de cada automóvil
if "puntos_contaminantes" not in st.session_state:
    st.session_state["puntos_contaminantes"] = []

def main():
    st.title("Centro de Verificación de Automóviles")

    # Entrada de puntos contaminantes para cada automóvil
    puntos = st.number_input("Ingrese los puntos contaminantes del automóvil:", min_value=0, step=1)

    if st.button("Registrar automóvil"):
        # Agregar los puntos a la lista
        st.session_state["puntos_contaminantes"].append(puntos)
        st.success(f"Puntos contaminantes registrados: {puntos}")

    # Mostrar las estadísticas si hay al menos un automóvil registrado
    if st.session_state["puntos_contaminantes"]:
        # Calcular el promedio
        promedio = sum(st.session_state["puntos_contaminantes"]) / len(st.session_state["puntos_contaminantes"])
        
        # Encontrar el mínimo y el máximo
        minimo = min(st.session_state["puntos_contaminantes"])
        maximo = max(st.session_state["puntos_contaminantes"])
        
        # Mostrar los resultados
        st.write("### Resultados")
        st.write("Promedio de puntos contaminantes:", promedio)
        st.write("Puntos contaminantes del automóvil que menos contaminó:", minimo)
        st.write("Puntos contaminantes del automóvil que más contaminó:", maximo)

    # Opción para ingresar los datos de otro automóvil
    if st.button("¿Desea ingresar otro automóvil?"):
        st.write("Puede ingresar los puntos contaminantes del siguiente automóvil.")

if __name__ == "__main__":
    main()
