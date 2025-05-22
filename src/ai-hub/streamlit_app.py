from dotenv import load_dotenv
import streamlit as st
from navigation.routes import pages

st.set_page_config(page_title="AI Hub", layout="wide")

load_dotenv()
pages().run()
