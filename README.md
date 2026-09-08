# YouTube Video Analyzer Agent

A minor project on a AI-powered Streamlit application that analyzes YouTube videos with Google Gemini and Agno. Enter a video URL to receive a structured report covering the video overview, topic segments, timestamps, themes, key learning points, and demonstrations.

## 🌐 Deployment

[Youtube Analyzer](https://youtube-video-analyzer26.streamlit.app/)

## Features

- Extracts and analyzes YouTube video content with `YouTubeTools`.
- Generates descriptive timestamps and segment summaries.
- Identifies video type, major themes, topic progression, and practical references.
- Presents the analysis as formatted Markdown in a Streamlit interface.

## Requirements

- Python 3.10+
- A Google Gemini API key

Install the dependencies:

```bash
pip install streamlit agno google-generativeai python-dotenv
```

Create a `.env` file in the project root and add your API key:

```env
GOOGLE_API_KEY=your_google_api_key
```

## Run

```bash
streamlit run ui.py
```

Open the local Streamlit URL, enter a YouTube video URL, and select **Analyze Video**.

## Project Structure

- `agent.py` - Configures the Gemini-powered YouTube analysis agent.
- `ui.py` - Provides the Streamlit user interface and runs analyses.
