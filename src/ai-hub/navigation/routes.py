import streamlit as st

# Icons: https://fonts.google.com/icons?icon.set=Material+Symbols


def pages():
    return st.navigation(
        {
            "Main": [
                st.Page(
                    "navigation/main/home.py",
                    title="Home Page",
                    icon=":material/home:",
                    default=True,
                ),
            ],
            "Hostel Helper": [
                st.Page(
                    "navigation/hostel_helper/llamaindex_chat.py",
                    title="LlamaIndex",
                    icon=":material/apartment:",
                ),
                st.Page(
                    "navigation/hostel_helper/llamaindex_graph.py",
                    title="LangGraph + LlamaIndex",
                    icon=":material/apartment:",
                ),
                st.Page(
                    "navigation/hostel_helper/langchain.py",
                    title="Langchain",
                    icon=":material/apartment:",
                ),
                st.Page(
                    "navigation/hostel_helper/langgraph.py",
                    title="Langgraph",
                    icon=":material/apartment:",
                ),
                st.Page(
                    "navigation/hostel_helper/about_hostel_helper.py",
                    title="About",
                    icon=":material/info:",
                ),
            ],
            "Crew AI": [
                st.Page(
                    "navigation/crew_ai/blog_builder.py",
                    title="Blog Builder",
                    icon=":material/chat:",
                ),
                st.Page(
                    "navigation/crew_ai/movie_mate.py",
                    title="Movie Mate",
                    icon=":material/live_tv:",
                ),
                st.Page(
                    "navigation/crew_ai/about_crew_ai.py",
                    title="About",
                    icon=":material/info:",
                ),
            ],
            "Classificators": [
                st.Page(
                    "navigation/classificators/gender.py",
                    title="Gender",
                    icon=":material/male:",
                ),
                st.Page(
                    "navigation/classificators/about_classificators.py",
                    title="About",
                    icon=":material/info:",
                ),
            ],
            "Named Entity Recognition": [
                st.Page(
                    "navigation/named_entity_recognition/text_extractor.py",
                    title="Gender",
                    icon=":material/list_alt:",
                ),
                st.Page(
                    "navigation/named_entity_recognition/about_ner.py",
                    title="About",
                    icon=":material/info:",
                ),
            ],
        }
    )
