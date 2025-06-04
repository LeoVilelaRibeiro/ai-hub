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
                    title="Text Extractor",
                    icon=":material/list_alt:",
                ),
                st.Page(
                    "navigation/named_entity_recognition/about_ner.py",
                    title="About",
                    icon=":material/info:",
                ),
            ],
            "Movie Recommender": [
                st.Page(
                    "navigation/movie_recommender/popularity.py",
                    title="Popularity",
                    icon=":material/trending_up:",
                ),
                st.Page(
                    "navigation/movie_recommender/association_rules.py",
                    title="Association Rules",
                    icon=":material/auto_graph:",
                ),
                st.Page(
                    "navigation/movie_recommender/collaborative_filtering.py",
                    title="Collaborative Filtering",
                    icon=":material/group:",
                ),
                st.Page(
                    "navigation/movie_recommender/content_based.py",
                    title="Content Based",
                    icon=":material/movie:",
                ),
                st.Page(
                    "navigation/movie_recommender/about_movie_recommender.py",
                    title="About",
                    icon=":material/info:",
                ),
            ],
            "Guardrails": [
                st.Page(
                    "navigation/guardrails/toxicity.py",
                    title="Toxicity Checker",
                    icon=":material/security:",
                ),
                st.Page(
                    "navigation/guardrails/about_guardrails.py",
                    title="About",
                    icon=":material/info:",
                ),
            ],
        }
    )
