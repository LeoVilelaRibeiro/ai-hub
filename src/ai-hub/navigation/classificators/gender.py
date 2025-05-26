from navigation.classificators.utils.classify_gender import get_gender_by_name
import streamlit as st

st.title("🧠 Gender Classifier Demo")

name = st.text_input("Enter a first name", placeholder="e.g., Aline, Abel, Ada")

col1, col2 = st.columns([3, 1])

with col2:
    classify = st.button(
        "🚀 Classify", use_container_width=True, disabled=not bool(name.strip())
    )

result_placeholder = st.empty()

if classify:
    result = get_gender_by_name(name)
    if result == "Not Found":
        result_placeholder.error(f"❌ Name `{name}` not found in database.")
    else:
        icon = "👩" if result == "Female" else "👨"
        result_placeholder.success(
            f"✅ Name **{name}** classified as **{result.lower()}** {icon}."
        )
