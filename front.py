
import streamlit as st
from stock_gem import run_stock_analysis

st.set_page_config(page_title="📈 Stock Insight Bot", layout="centered")
st.title("📊 AI Stock Insight Comparator")
st.markdown("Enter a company name or stock (e.g., `Tesla`, `AAPL`, `Infosys`)")

# Input
stock_name = st.text_input("🔎 Company or Stock Name")

# Action
if st.button("Get Insights"):
    if stock_name.strip() == "":
        st.warning("Please enter a valid stock name.")
    else:
        with st.spinner("Fetching insights..."):
            try:
                result = run_stock_analysis(stock_name)
                st.success("Insights fetched successfully!")
                st.markdown("### 🧠 AI Analysis Output")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
