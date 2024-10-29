import streamlit as st
import math

# Procedimiento para calcular el área de una circunferencia
def calcular_area(radio):
    return math.pi * radio ** 2

# Procedimiento para calcular el perímetro de una circunferencia
def calcular_perimetro(radio):
    return 2 * math.pi * radio

def main():
    st.title("Cálculo de Área y Perímetro de una Circunferencia")
    
    # Entrada del radio
    radio = st.number_input("Introduce el radio de la circunferencia:", min_value=0.0, step=0.1)
    
    # Botón para realizar el cálculo
    if st.button("Calcular"):
        area = calcular_area(radio)
        perimetro = calcular_perimetro(radio)
        
        # Mostrar los resultados
        st.write(f"**Área de la circunferencia:** {area:.2f}")
        st.write(f"**Perímetro de la circunferencia:** {perimetro:.2f}")

if __name__ == "__main__":
    main()
