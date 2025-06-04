import streamlit as st
import requests
import os

st.title("🛡️ Toxicity Checker via Hugging Face API")

st.markdown(
  """
  This page uses the **`unitary/toxic-bert`** model via the **Hugging Face Inference API**  
  to classify whether a given text contains **toxic content**.

  Simply enter a sentence below and click analyze.

  ---
  """
)

text = st.text_area(
  "📝 Enter a sentence to analyze:",
  placeholder="You're the worst person I've ever met...",
  height=100,
)

col1, col2 = st.columns([3, 1])
result_placeholder = st.empty()

# Hugging Face API key validation
api_key = os.getenv("HUGGING_FACE_KEY")

if not api_key:
  st.error("❌ Environment variable `HUGGING_FACE_KEY` is not set.")
  st.stop()

headers = {
  "Authorization": f"Bearer {api_key}"
}

API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"


def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()


def format_result_as_code(response: list[dict]) -> str:
  lines = ["["]
  for entry in response:
    label = entry["label"]
    score = f'{entry["score"]:.4f}'
    lines.append(f'  {{ "label": "{label}", "score": {score} }},')
  lines.append("]")
  return "\n".join(lines)


with col2:
  run = st.button(
    "🚀 Analyze", use_container_width=True, disabled=not bool(text.strip())
  )

if run:
  with st.spinner("Analyzing..."):
    result = query({"inputs": text})

    if isinstance(result, dict) and result.get("error"):
      result_placeholder.error(f"❌ API Error: {result['error']}")
    elif isinstance(result, list):
      result_placeholder.markdown("### ✅ Classification Result:")
      formatted = format_result_as_code(result[0])
      result_placeholder.code(formatted, language="json")

      # Check if the sentence is toxic
      toxic_entry = next((item for item in result[0] if item["label"] == "toxic"), None)
      if toxic_entry:
        if toxic_entry["score"] > 0.5:
          st.warning("☣️ Yikes! This sentence is likely toxic. Choose your words wisely.")
        else:
          st.success("🌼 This sentence seems civil and respectful. Nicely done!")
      else:
        st.info("ℹ️ No clear toxic content detected.")
    else:
      result_placeholder.error("❌ Unexpected API response format.")
