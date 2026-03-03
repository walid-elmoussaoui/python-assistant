
<img width="688" height="890" alt="Screenshot 2026-03-03 022729" src="https://github.com/user-attachments/assets/e76f1ba9-040f-4f36-8f00-2502bd6c7f51" />


Project Description

This project is a Desktop AI Assistant Application developed in Python that seamlessly integrates both voice and text-based interaction. The application provides an intuitive graphical interface and leverages advanced AI capabilities to deliver intelligent, real-time responses. It is designed to function as a locally executed virtual assistant, similar to modern voice assistants, while remaining fully customizable and developer-controlled.

Core Features
1. Graphical User Interface (gui.py)

The application features a modern desktop interface built using Tkinter, ensuring a clean and user-friendly experience.

Key interface components include:

A visually displayed assistant icon/image

A text input field for typed user messages

A conversation display panel showing chat history

Interactive control buttons:

Speaker – Activates voice input

Send – Submits typed messages

Delete – Clears the conversation history

The interface is designed for simplicity, responsiveness, and ease of use.

2. Voice Interaction Capabilities
Speech Recognition (speeker.py)

The application converts spoken commands into text using the speech_recognition library with microphone input support via pyaudio. This enables hands-free communication with the assistant.

Text-to-Speech (speak.py)

AI-generated responses are converted into natural-sounding speech using the pyttsx3 library. The system includes adjustable volume control, allowing users to customize the audio output experience.

3. AI Backend Processing (action.py, aiml_api.py)

The backend is responsible for processing user inputs—whether typed or voice-converted—and generating intelligent responses.

Core capabilities include:

Integration with Google Gemini LLM via the OpenAI API

Context-aware response generation

Built-in natural language command handlers for common queries such as:

Greeting responses (e.g., “Hello”, “How are you?”)

Volume control commands

Assistant identity inquiries

Additionally, the assistant can retrieve real-time data from external APIs, such as weather information and web-based resources.

Additional Modules

weather.py – Handles weather data retrieval from external APIs

test.py – Contains development and testing utilities

ai_assistant.spec – PyInstaller configuration file used to package the application into a standalone executable

Technology Stack

GUI: Tkinter + Pillow (PIL)

Voice Input/Output: speech_recognition, pyttsx3, pyaudio

Artificial Intelligence: OpenAI API (Google Gemini integration)

Packaging: PyInstaller (for standalone .exe generation)

Overview

This application functions as a voice-enabled AI assistant comparable to Siri or Cortana, but is entirely custom-built and designed to run locally on a desktop environment. Its modular architecture allows for easy extension, customization, and future scalability.

The project demonstrates practical imple![Uploading proj1.png…]()
mentation of desktop UI development, speech processing, API integration, and AI-driven conversational systems within a cohesive Python-based architecture.
