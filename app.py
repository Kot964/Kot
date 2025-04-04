import streamlit as st
import random

st.set_page_config(page_title="Генератор номеров РФ", page_icon="📱")

st.title("📱 Генератор российских номеров телефонов")

# Расширенный словарь регионов и их DEF-кодов
region_def_codes = dict({
    "Москва и МО (UTC+3)": ["910", "915", "916", "917", "919", "980", "985", "986", "989"],
    "Санкт-Петербург и ЛО (UTC+3)": ["921", "931"],
    "Новосибирская обл. (UTC+7)": ["913", "923"],
    "Красноярский край (UTC+7)": ["902", "933"],
    "Хабаровский край (UTC+10)": ["962"],
    "Свердловская обл. (UTC+5)": ["912", "922"],
    "Челябинская обл. (UTC+5)": ["900", "908"],
    "Ростовская обл. (UTC+3)": ["938", "928"],
    "Калининградская обл. (UTC+2)": ["911", "931"],
    "Самарская обл. (UTC+4)": ["927", "937"],
    "Республика Башкортостан (UTC+5)": ["917", "927"],
    "Татарстан (UTC+3)": ["917", "927"],
    "Нижегородская обл. (UTC+3)": ["831", "920"],
    "Воронежская обл. (UTC+3)": ["473", "920"],
    "Омская обл. (UTC+6)": ["381", "950"],
    "Пермский край (UTC+5)": ["342", "902"],
    "Приморский край (UTC+10)": ["423", "902"],
    "Саратовская обл. (UTC+4)": ["845", "927"],
    "Тюменская обл. (UTC+5)": ["345", "922"],
    "Ульяновская обл. (UTC+4)": ["842", "927"],
    "Иркутская обл. (UTC+8)": ["395", "964"],
    "Ярославская обл. (UTC+3)": ["485", "920"],
    "Кемеровская обл. (UTC+7)": ["384", "923"],
    "Томская обл. (UTC+7)": ["382", "923"],
    "Алтайский край (UTC+7)": ["385", "902"],
    "Амурская обл. (UTC+9)": ["416", "914"],
    "Архангельская обл. (UTC+3)": ["818", "921"],
    "Астраханская обл. (UTC+4)": ["851", "927"],
    "Белгородская обл. (UTC+3)": ["472", "920"],
    "Брянская обл. (UTC+3)": ["483", "920"],
    "Владимирская обл. (UTC+3)": ["492", "920"],
    "Волгоградская обл. (UTC+3)": ["844", "904"],
    "Вологодская обл. (UTC+3)": ["817", "921"],
    "Ивановская обл. (UTC+3)": ["493", "920"],
    "Ингушетия (UTC+3)": ["873", "901"],
    "Кабардино-Балкарская Респ. (UTC+3)": ["866", "901"],
    "Калмыкия (UTC+3)": ["847", "901"],
    "Карачаево-Черкесская Респ. (UTC+3)": ["878", "901"],
    "Карелия (UTC+3)": ["814", "921"],
    "Кировская обл. (UTC+3)": ["833", "912"],
    "Костромская обл. (UTC+3)": ["494", "920"],
    "Курганская обл. (UTC+5)": ["352", "912"],
    "Курская обл. (UTC+3)": ["471", "920"],
    "Липецкая обл. (UTC+3)": ["474", "920"],
    "Магаданская обл. (UTC+11)": ["413", "914"],
    "Марий Эл (UTC+3)": ["836", "902"],
    "Мордовия (UTC+3)": ["834", "902"],
    "Ненецкий АО (UTC+3)": ["818", "921"],
    "Новгородская обл. (UTC+3)": ["816", "921"],
    "Орловская обл. (UTC+3)": ["486", "920"],
    "Пензенская обл. (UTC+3)": ["841", "902"],
    "Псковская обл. (UTC+3)": ["811", "921"],
    "Сахалинская обл. (UTC+11)": ["424", "914"],
    "Северная Осетия (UTC+3)": ["867", "901"],
    "Смоленская обл. (UTC+3)": ["481", "920"],
    "Ставропольский край (UTC+3)": ["865", "962"],
    "Тамбовская обл. (UTC+3)": ["475", "920"],
    "Тверская обл. (UTC+3)": ["482", "920"],
    "Тульская обл. (UTC+3)": ["487", "920"],
    "Хакасия (UTC+7)": ["390", "923"],
    "Чеченская Респ. (UTC+3)": ["871", "901"],
    "Чувашия (UTC+3)": ["835", "902"],
    "Якутия (UTC+9)": ["411", "914"],
    "Ямало-Ненецкий АО (UTC+5)": ["349", "912"]
})

selected_regions = st.multiselect("Выберите регион(ы) / часовой пояс:", options=list(region_def_codes.keys()), default=list(region_def_codes.keys())[:5])
count = st.number_input("Введите количество номеров", min_value=1, max_value=1000000, value=1000)


def generate_rf_numbers(count, def_codes):
    numbers = []
    for _ in range(count):
        def_code = random.choice(def_codes)
        number = '7' + def_code + ''.join(str(random.randint(0, 9)) for _ in range(7))
        numbers.append(number)
    return numbers

if st.button("Сгенерировать"):
    selected_def_codes = []
    for region in selected_regions:
        selected_def_codes.extend(region_def_codes.get(region, []))

    if not selected_def_codes:
        st.error("Пожалуйста, выберите хотя бы один регион")
    else:
        numbers = generate_rf_numbers(count, selected_def_codes)
        st.success(f"Сгенерировано {count} номеров по выбранным регионам")
        st.code('\n'.join(numbers[:10]), language='text')

        txt = '\n'.join(numbers)
        st.download_button(
            label="📥 Скачать .txt файл",
            data=txt,
            file_name="rf_numbers.txt",
            mime="text/plain"
        )
