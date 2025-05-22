import streamlit as st
from navigation.crew_ai.utils.consulting_external_api import (
    ConsultingExternalAPI,
)
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool
from crewai import Agent, Task, Crew

st.title("🎬 MovieMate: Ask about movies")

directory_read_tool = DirectoryReadTool(directory="./rag/movies_information_guide.md")
file_read_tool = FileReadTool()
search_tool = SerperDevTool()
ConsultingExternalAPI = ConsultingExternalAPI()

# Agents
rec_movie_agent = Agent(
    role="Movie Recommender",
    goal="Recommend excellent quality movies that meet our consumers' needs",
    backstory=(
        "As part of MovieInc's dynamic recommendation team, your mission is to search "
        "the digital landscape for potential films. Armed with state-of-the-art tools "
        "and a strategic mindset, you analyze movie ratings and reviews to discover "
        "new films to recommend. Your work is key to recommending quality films that "
        "satisfy consumers seeking your recommendation."
    ),
    allow_delegation=False,
    verbose=False,
)

lead_rec_movie_agent = Agent(
    role="Movie Recommender Specialist",
    goal="Improve and detail Movie Recommendations to gather the best quality",
    backstory=(
        "Within the vibrant ecosystem of MovieInc's Recommendation department, "
        "you stand out as the person who guarantees the quality of films and "
        "recommends what the customer really wants. When recommending films, you "
        "not only find and report on films but also gather results from API "
        "queries, reviewing the returned data to ensure comprehensive coverage of "
        "the subject matter that interests the consumer."
    ),
    allow_delegation=False,
    verbose=False,
)

# Tasks
movie_profiling_task = Task(
    description=(
        "Conduct an in-depth analysis of {movie_name}, "
        "mainly about the {question} received, "
        "that needs out recommendation to be happy. "
        "Utilize all available data sources "
        "to compile a detailed description, "
        "focusing on answer the {question}"
        "about the movie. "
        "Don't make assumptions and "
        "only use information you absolutely sure about."
    ),
    expected_output=(
        "A comprehensive report on movie {movie_name}, "
        "exploring the {question}, "
        "the related subjects about the {question}. "
        "Highlight all the positive findings "
        "that is possible to describe about the "
        "movie suggest with ways our consumer can watch the movie."
    ),
    tools=[directory_read_tool, file_read_tool, search_tool],
    agent=rec_movie_agent,
)

personalized_outreach_task = Task(
    description=(
        "Using the insights gathered from "
        "the movie profiling report on {movie_name}, "
        "craft a personalized answer "
        "acording the {question}, "
        "the best answer to the {question} about the movie {movie_name}. "
        "The answer have to be merged with result from  ConsultingExternalAPI task, "
        "calling the API with the parameters movie_name= {movie_name}, "
        "genre = a genre of movie asked in {question} and str= {question} "
        "and did a reviwe combinning the two sources. "
        "Your communication must resonate "
        "without vulgar terms, "
        "demonstrating a very polite "
        "answer.\n"
        "Don't make assumptions and only "
        "use information you absolutely sure about."
    ),
    expected_output=(
        "A paragraph "
        "tailored to {movie_name}, "
        "specifically answering the question:{question}."
        "Ensure the tone is engaging, professional, "
        "and aligned with movie {movie_name} and question done:{question}."
    ),
    tools=[ConsultingExternalAPI, search_tool],
    agent=lead_rec_movie_agent,
)

movie_name = st.text_input("🎞️ Movie name", placeholder="Matrix")
question = st.text_input(
    "❓ Ask about a movie:", placeholder="What are some movies similar to Matrix?"
)

col1, col2, col3 = st.columns([3, 1, 0.5])
response_placeholder = st.empty()

with col3:
    is_disabled = not (bool(movie_name.strip()) and bool(question.strip()))
    generate = st.button("🚀 Generate", use_container_width=True, disabled=is_disabled)

if generate:
    response_placeholder.markdown("🔄 Generating article...")
    try:
        crew = Crew(
            agents=[rec_movie_agent, lead_rec_movie_agent],
            tasks=[movie_profiling_task, personalized_outreach_task],
            verbose=False,
            memory=True,
        )

        result = crew.kickoff({"movie_name": movie_name, "question": question})
        response_placeholder.markdown(result)
    except Exception:
        st.error(
            "An error occurred while initializing the model with the provided key. "
            "Please check your environment variables or contact OpenAI and TMDB "
            "support if the issue persists."
        )
        st.stop()
