import streamlit as st

def main():
    st.title("Suma y Media de Números")
    st.write("Introduce números. El programa terminará cuando introduzcas un cero.")
    
    # Lista para almacenar los números introducidos
    numeros = []
    
    # Entrada de número
    while True:
        numero = st.number_input("Introduce un número:", step=1, format="%d")
        if numero == 0:
            break
        numeros.append(numero)
        
        # Mostrar la lista de números hasta ahora
        st.write("Números introducidos:", numeros)

    # Cálculo de la suma y la media
    if numeros:
        suma = sum(numeros)
        media = suma / len(numeros)
        st.write("**Suma de todos los números:**", suma)
        st.write("**Media de todos los números:**", media)
    else:
        st.write("No se introdujeron números.")

if __name__ == "__main__":
    main()
