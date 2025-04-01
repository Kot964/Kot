
import streamlit as st
import random

st.set_page_config(page_title="Генератор номеров РФ", page_icon="📱")

st.title("📱 Генератор российских номеров телефонов")

count = st.number_input("Введите количество номеров", min_value=1, max_value=1000000, value=1000)

def generate_rf_numbers(count):
    return ['79' + ''.join(str(random.randint(0, 9)) for _ in range(9)) for _ in range(count)]

if st.button("Сгенерировать"):
    numbers = generate_rf_numbers(count)
    st.success(f"Сгенерировано {count} номеров")
    st.code('\n'.join(numbers[:10]), language='text')

    txt = '\n'.join(numbers)
    st.download_button(
        label="📥 Скачать .txt файл",
        data=txt,
        file_name="rf_numbers.txt",
        mime="text/plain"
    )
