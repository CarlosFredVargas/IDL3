import streamlit as st

def main():
    st.title("Análisis de una Lista de 10 Números")

    # Entrada de 10 números por parte del usuario
    numeros = []
    for i in range(10):
        numero = st.number_input(f"Introduce el número {i + 1}:", step=1.0, format="%.2f")
        numeros.append(numero)
    
    if st.button("Calcular"):
        # Calcular la media
        media = sum(numeros) / len(numeros)
        
        # Contar mayores, menores e iguales a 10
        mayores = sum(1 for num in numeros if num > 10)
        iguales = sum(1 for num in numeros if num == 10)
        menores = sum(1 for num in numeros if num < 10)
        
        # Mostrar resultados
        st.write("### Resultados")
        st.write(f"Lista de números: {numeros}")
        st.write(f"Media de los números: {media:.2f}")
        st.write(f"Cantidad de números mayores que 10: {mayores}")
        st.write(f"Cantidad de números iguales a 10: {iguales}")
        st.write(f"Cantidad de números menores que 10: {menores}")

if __name__ == "__main__":
    main()
