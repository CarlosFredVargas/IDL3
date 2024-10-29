import streamlit as st

def main():
    st.title("Múltiplos de un Número entre 0 y 100")

    # Entrada del número X
    x = st.number_input("Introduce el valor de X para encontrar sus múltiplos entre 0 y 100:", min_value=1, step=1)

    if st.button("Calcular"):
        # Crear el array de múltiplos de X entre 0 y 100
        multiplos = [i for i in range(0, 101) if i % x == 0]
        
        # Calcular la cantidad de datos y la sumatoria
        cantidad = len(multiplos)
        suma = sum(multiplos)
        
        # Mostrar resultados
        st.write("### Resultados")
        st.write(f"Múltiplos de {x} entre 0 y 100:", multiplos)
        st.write(f"Cantidad de múltiplos: {cantidad}")
        st.write(f"Sumatoria de los múltiplos: {suma}")

if __name__ == "__main__":
    main()
