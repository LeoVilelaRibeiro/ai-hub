import streamlit as st
from navigation.named_entity_recognition.utils.crf_predictor import predict


st.title("🧠 CRF Named Entity Recognition")

st.markdown(
    """
  This page demonstrates a **Named Entity Recognition (NER)** model using **CRF
  (Conditional Random Fields)**.

  The model takes a text input and extracts entities like names, addresses, phone
  numbers, CPF, emails, etc.

  ---
  """
)

text = st.text_area(
    "📝 Enter a text to extract entities",
    placeholder="Meu nome é Renato Silva, moro na Rua das Flores, 123...",
    height=100,
)

col1, col2 = st.columns([3, 1])

with col2:
    run = st.button(
        "🚀 Extract", use_container_width=True, disabled=not bool(text.strip())
    )

result_placeholder = st.empty()


def format_dict_as_code_block(d: dict) -> str:
    lines = ["{"]
    for key, value in d.items():
        lines.append(f'  "{key}": "{value}",')
    lines.append("}")
    return "\n".join(lines)


if run:
    try:
        result = predict(text)
        if not result:
            result_placeholder.warning("⚠️ No entities were found in the text.")
        else:
            result_placeholder.markdown("### ✅ Extraction Result:")
            formatted_result = format_dict_as_code_block(result)
            result_placeholder.code(formatted_result, language="python")
    except Exception as e:
        st.error(f"❌ An error occurred during prediction: {e}")
