import streamlit as st
from agent import build_youtube_agent

st.set_page_config(
    page_title=" YouTube Video Analyzer",
    page_icon="🎥",
    layout="centered",
)

st.title("🤖 AI YouTube Video Analyzer")

@st.cache_resource # Cache the agent to avoid recreating on every page refresh
def get_agent(): 
    return build_youtube_agent()

agent = get_agent()

#Input
video_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=example")
btn = st.button("Analyze Video")

if video_url and btn:
    with st.spinner("Analyzing Video..."):
        response = agent.run(f"Analyze this video: {video_url}")
        st.markdown("Analyze report of video")
        st.markdown(response.content)