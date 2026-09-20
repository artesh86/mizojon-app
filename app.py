import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Бори мизоҷон", layout="centered")

st.title("📦 Системаи баҳисобгирии бори мизоҷон")

# Сабт кардани маълумот дар хотира
if "orders" not in st.session_state:
    st.session_state.orders = []

# Формаи ворид намудани маълумот
st.subheader("➕ Илова кардани бори нав")
with st.form("cargo_form", clear_on_submit=True):
    client_name = st.text_input("Номи мизоҷ / Исм:")
    cargo_type = st.text_input("Намуди бор (масалан: Цемент, Оҳан):")
    weight_tn = st.number_input("Тоннаж (тн):", min_value=0.0, step=0.1)
    price_per_tn = st.number_input("Нархи 1 тонна ($/сомонӣ):", min_value=0.0, step=1.0)
    
    submitted = st.form_submit_button("Сабт кардан")
    
    if submitted:
        if client_name and weight_tn > 0:
            total_sum = weight_tn * price_per_tn
            new_order = {
                "Сана": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Мизоҷ": client_name,
                "Бор": cargo_type,
                "Тоннаж (тн)": weight_tn,
                "Нарх": price_per_tn,
                "Ҷамъ": total_sum
            }
            st.session_state.orders.append(new_order)
            st.success(f"Бори {client_name} муваффақона сабт шуд!")
        else:
            st.error("Лутфан номи мизоҷ ва тоннажро дуруст ворид кунед!")

# Намоиши ҷадвали борҳо
st.subheader("📋 Рӯйхати борҳо")
if st.session_state.orders:
    df = pd.DataFrame(st.session_state.orders)
    st.dataframe(df, use_container_width=True)
    
    # Ҳисоби умумӣ
    total_weight = df["Тоннаж (тн)"].sum()
    total_money = df["Ҷамъ"].sum()
    
    st.info(f"**Ҷамъи умумии бор:** {total_weight:.2f} тн | **Ҷамъи сумма:** {total_money:.2f}")
else:
    st.write("Ҳоло ҳеҷ бор сабт нашудааст.")

