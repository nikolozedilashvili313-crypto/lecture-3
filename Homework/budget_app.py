import streamlit as st


st.title("პირადი ბიუჯეტის ტრეკერი")
st.caption("ინტერაქტიული ვებ-აპლიკაცია ყოველდღიური ხარჯების აღრიცხვისთვის")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

categories = ["საჭმელი", "ტრანსპორტი", "სხვა"]

with st.sidebar:
    st.header("ახალი ხარჯი")

    name = st.text_input("ხარჯის დასახელება (მაგ: ყავა, სადილი)")

    amount = st.number_input("თანხა", min_value=0.0)

    category = st.selectbox("კატეგორია", categories)

    if st.button("დამატება"):
        st.session_state.expenses.append(
            {"დასახელება": name, "თანხა": amount, "კატეგორია": category}
        )

    if st.button("სიის გასუფთავება"):
        st.session_state.expenses = []

selected = st.selectbox("ფილტრი კატეგორიით", ["ყველა"] + categories)

if selected == "ყველა":
    shown = st.session_state.expenses
else:
    shown = [e for e in st.session_state.expenses if e["კატეგორია"] == selected]

st.table(shown)

total = sum(e["თანხა"] for e in st.session_state.expenses)
st.metric("ჯამური თანხა", total)