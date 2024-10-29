import streamlit as st

# Definir las funciones para cada operación
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def main():
    st.title("Calculadora Básica")

    # Entrada de números
    num1 = st.number_input("Introduce el primer número:", format="%f")
    num2 = st.number_input("Introduce el segundo número:", format="%f")

    # Selección de la operación
    operacion = st.selectbox("Selecciona la operación:", ("Suma", "Resta", "Multiplicación", "División"))

    # Botón para calcular
    if st.button("Calcular"):
        if operacion == "Suma":
            resultado = sumar(num1, num2)
        elif operacion == "Resta":
            resultado = restar(num1, num2)
        elif operacion == "Multiplicación":
            resultado = multiplicar(num1, num2)
        elif operacion == "División":
            resultado = dividir(num1, num2)
        
        # Mostrar el resultado
        st.write(f"**Resultado:** {resultado}")

if __name__ == "__main__":
    main()
