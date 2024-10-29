import streamlit as st

def main():
    st.title("Cálculo de Pago Mensual y Total en 20 Meses")
    
    # Lista para almacenar los pagos de cada mes
    pagos = []
    total_pagado = 0
    
    # Calcular los pagos para cada uno de los 20 meses
    for mes in range(1, 21):
        pago_mensual = 10 * (2 ** (mes - 1))  # Cada mes se duplica el pago
        pagos.append(pago_mensual)
        total_pagado += pago_mensual
    
    # Mostrar el pago mensual y el total pagado
    st.write("### Pago mensual para cada mes:")
    for mes, pago in enumerate(pagos, start=1):
        st.write(f"Mes {mes}: S/{pago}")

    st.write("### Total pagado después de 20 meses:")
    st.write(f"S/{total_pagado}")

if __name__ == "__main__":
    main()
