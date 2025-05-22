import streamlit as st
from crewai import Agent, Task, Crew

st.title("📝 BlogBuilder: Automated Article Generator")

# Agents
planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory="You're working on planning a blog article "
    "about the topic: {topic}."
    "You collect information that helps the "
    "audience learn something "
    "and make informed decisions. "
    "Your work is the basis for "
    "the Content Writer to write an article on this topic.",
    allow_delegation=False,
    verbose=False,
)

writer = Agent(
    role="Content Writer",
    goal="Write insightful and factually accurate "
    "opinion piece about the topic: {topic}",
    backstory="You're working on a writing "
    "a new opinion piece about the topic: {topic}. "
    "You base your writing on the work of "
    "the Content Planner, who provides an outline "
    "and relevant context about the topic. "
    "You follow the main objectives and "
    "direction of the outline, "
    "as provide by the Content Planner. "
    "You also provide objective and impartial insights "
    "and back them up with information "
    "provide by the Content Planner. "
    "You acknowledge in your opinion piece "
    "when your statements are opinions "
    "as opposed to objective statements.",
    allow_delegation=False,
    verbose=False,
)

editor = Agent(
    role="Editor",
    goal="Edit a given blog post to align with "
    "the writing style of the organization. ",
    backstory="You are an editor who receives a blog post "
    "from the Content Writer. "
    "Your goal is to review the blog post "
    "to ensure that it follows journalistic best practices,"
    "provides balanced viewpoints "
    "when providing opinions or assertions, "
    "and also avoids major controversial topics "
    "or opinions when possible.",
    allow_delegation=False,
    verbose=False,
)

# Tasks

plan = Task(
    description=(
        "1. Prioritize the latest trends, key players, "
        "and noteworthy news on {topic}.\n"
        "2. Identify the target audience, considering "
        "their interests and pain points.\n"
        "3. Develop a detailed content outline including "
        "an introduction, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
    expected_output="A comprehensive content plan document "
    "with an outline, audience analysis, "
    "SEO keywords, and resources.",
    agent=planner,
)

write = Task(
    description=(
        "1. Use the content plan to craft a compelling "
        "blog post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
        "3. Sections/Subtitles are properly named "
        "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
        "engaging introduction, insightful body, "
        "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
        "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written blog post "
    "in markdown format, ready for publication, "
    "each section should have 2 or 3 paragraphs.",
    agent=writer,
)

edit = Task(
    description=(
        "Proofread the given blog post for grammatical errors and alignment "
        "with the brand's voice. Make sure the final output is in plain markdown text "
        "and does not include code block formatting such as triple backticks (```), "
        "since this will be rendered directly on a web interface."
    ),
    expected_output=(
        "A well-written blog post in markdown format, "
        "ready for publication. Do not include any code block markers "
        "(i.e., avoid using triple backticks ```), just return plain markdown text. "
        "Each section should have 2 or 3 paragraphs."
    ),
    agent=editor,
)

topic = st.text_input("📚 Choose a topic", placeholder="AI in Education")

col1, col2, col3 = st.columns([3, 1, 0.5])
response_placeholder = st.empty()

with col3:
    generate = st.button(
        "🚀 Generate", use_container_width=True, disabled=not bool(topic.strip())
    )

if generate:
    response_placeholder.markdown("🔄 Generating article...")
    try:
        crew = Crew(
            agents=[planner, writer, editor], tasks=[plan, write, edit], verbose=False
        )
        result = crew.kickoff({"topic": topic})
        response_placeholder.markdown(result)
    except Exception:
        st.error(
            "An error occurred while initializing the model with the provided key. "
            "Please check your environment variables or contact OpenAI support if the "
            "issue persists."
        )
        st.stop()
