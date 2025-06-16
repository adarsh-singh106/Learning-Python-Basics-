import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import os
import datetime # For time-based commands
import logging # For better debugging
from dotenv import load_dotenv # For API keys
import google.generativeai as genai # Gemini API

# --- Configuration & Initialization ---
load_dotenv() # Load environment variables from .env file

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Speech Engine
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # You can try different voices if available, e.g., voices[1].id for a female voice on some systems
    # engine.setProperty('voice', voices[0].id) # Example: set to the first available voice
    engine.setProperty('rate', 180)  # Speed of speech
except Exception as e:
    logging.error(f"Failed to initialize pyttsx3 engine: {e}")
    # Fallback: print to console if TTS fails
    def speak_fallback(text):
        print(f"Jarvis (TTS failed): {text}")
    speak = speak_fallback
    engine = None # Ensure engine is None if init failed
else:
    def speak(text):
        logging.info(f"Jarvis says: {text}")
        if engine:
            engine.say(text)
            engine.runAndWait()
        else:
            print(f"Jarvis (TTS engine not available): {text}")


# Recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()
# Adjust sensitivity to ambient noise if needed
# with microphone as source:
# recognizer.adjust_for_ambient_noise(source, duration=1)
# recognizer.energy_threshold = 4000 # Experiment with this value

# API Keys
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

if not NEWS_API_KEY:
    speak("News API key not found. News functionality will be disabled.")
    logging.warning("NEWS_API_KEY not found in .env file.")
if not GEMINI_API_KEY:
    speak("Gemini API key not found. Advanced AI features will be disabled.")
    logging.warning("GOOGLE_GEMINI_API_KEY not found in .env file.")
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest') # Or 'gemini-pro'
        speak("Gemini AI model initialized successfully.")
    except Exception as e:
        speak(f"Failed to configure Gemini AI: {e}")
        logging.error(f"Gemini configuration error: {e}")
        gemini_model = None

# Music Library (example - consider a more robust way for larger libraries)
music_library = {
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
    # Add more songs: "song name": "youtube_link"
}

# --- Helper Functions ---
def listen_for_command(prompt="Listening for command...", timeout=5, phrase_time_limit=5):
    """Listens for a command and returns the recognized text."""
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5) # Quick adjustment
        speak(prompt)
        logging.info(prompt)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            command = recognizer.recognize_google(audio)
            logging.info(f"User said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            logging.warning("No speech detected within timeout.")
            # speak("I didn't hear anything.") # Optional feedback
            return None
        except sr.UnknownValueError:
            logging.warning("Google Speech Recognition could not understand audio.")
            # speak("Sorry, I couldn't understand that.") # Optional feedback
            return None
        except sr.RequestError as e:
            logging.error(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, my speech service is down.")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred during listening: {e}")
            speak("An error occurred while listening.")
            return None

def ask_gemini(prompt_text):
    """Sends a prompt to Gemini and returns the response."""
    if not gemini_model:
        speak("Gemini AI is not available.")
        return "Gemini AI is not configured or failed to initialize."
    if not prompt_text:
        return "No prompt provided for Gemini."

    try:
        # For simple text-only prompts
        response = gemini_model.generate_content(prompt_text)
        # Accessing the text part of the response
        if response.parts:
            return response.text # Or response.parts[0].text
        else:
            # Handle cases where response might be blocked or empty
            # You might need to inspect response.prompt_feedback
            logging.warning(f"Gemini response was empty or blocked. Feedback: {response.prompt_feedback}")
            return "I received an empty response or the content was blocked."

    except Exception as e:
        logging.error(f"Gemini API request failed: {e}")
        return f"Sorry, I encountered an error with Gemini: {str(e)}"


# --- Command Processing ---
def process_command(command):
    """Processes the recognized command."""
    if not command:
        return

    # Core Commands
    if "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "open chat gpt" in command or "open chatgpt" in command: # More flexible
        speak("Opening ChatGPT.")
        webbrowser.open("https://chat.openai.com")
    elif "open gmail" in command:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")
    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://www.github.com")
    elif "what time is it" in command or "current time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p") # e.g., 03:30 PM
        speak(f"The current time is {now}.")
    elif "what is today's date" in command or "date today" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y") # e.g., Monday, July 22, 2024
        speak(f"Today is {today}.")

    # Music Command
    elif command.startswith("play "):
        # Attempt to extract song name (can be multi-word)
        song_name_parts = command.split("play ", 1)
        if len(song_name_parts) > 1 and song_name_parts[1]:
            song_name = song_name_parts[1].strip()
            if song_name in music_library:
                speak(f"Playing {song_name}.")
                webbrowser.open(music_library[song_name])
            else:
                speak(f"Sorry, I don't have '{song_name}' in my library. I can search YouTube for it.")
                webbrowser.open(f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}")
        else:
            speak("What song would you like me to play?")

    # News Command
    elif "news" in command or "headlines" in command:
        if not NEWS_API_KEY:
            speak("I can't fetch news without the News API key.")
            return
        speak("Fetching the latest news headlines.")
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}&pageSize=5" # Get top 5
            response = requests.get(url)
            response.raise_for_status() # Raises an HTTPError for bad responses (4XX or 5XX)
            data = response.json()
            articles = data.get("articles", [])
            if articles:
                speak("Here are the top headlines:")
                for i, article in enumerate(articles):
                    title = article.get('title')
                    speak(f"{i+1}. {title}")
                    logging.info(f"News: {title}") # Log to console as well
            else:
                speak("Sorry, I couldn't find any news articles.")
        except requests.exceptions.RequestException as e:
            logging.error(f"News API request failed: {e}")
            speak("Sorry, I couldn't fetch the news at the moment.")
        except Exception as e:
            logging.error(f"Error processing news: {e}")
            speak("An unexpected error occurred while fetching news.")

    # Gemini as a fallback for general queries or specific trigger
    # Option 1: Specific trigger for Gemini
    elif command.startswith("ask gemini ") or command.startswith("hey gemini "):
        query = command.replace("ask gemini ", "").replace("hey gemini ", "").strip()
        if query:
            speak(f"Okay, asking Gemini: {query}")
            gemini_response = ask_gemini(query)
            speak(gemini_response)
        else:
            speak("What would you like to ask Gemini?")

    # Option 2: Gemini as a general fallback (if no other command matched)
    # This should be the LAST elif or an else block
    else:
        # Check if it's a question or something Gemini might handle
        # You can add more sophisticated checks here
        common_question_starters = ["what is", "who is", "explain", "tell me about", "how to", "can you"]
        if any(command.startswith(starter) for starter in common_question_starters) or len(command.split()) > 3 : # Heuristic: longer phrases might be questions
            if gemini_model:
                speak("Let me check that with Gemini.")
                gemini_response = ask_gemini(command)
                speak(gemini_response)
            else:
                speak("I'm not sure how to respond to that, and my advanced AI is not available.")
        else:
            speak("I'm not sure how to help with that. You can try asking Gemini by saying 'Ask Gemini your question'.")


# --- Main Loop ---
if __name__ == "__main__":
    speak("Jarvis system initializing...")
    if not GEMINI_API_KEY:
        speak("Warning: Gemini API key not found. Advanced AI capabilities will be limited.")
    if not NEWS_API_KEY:
        speak("Warning: News API key not found. News functionality will be disabled.")

    speak("Jarvis is now online. How can I help you today?")
    # speak("You can activate me by saying 'Jarvis' followed by your command, or just state your command directly if I'm already listening.")
    # Current setup: Listens for any command directly after startup or after processing a command.
    # For wake word, you'd have a separate loop.

    # Simple continuous listening loop (no explicit wake word here for simplicity, but can be added)
    # For a wake word system, you'd have an outer loop listening for "Jarvis"
    # and an inner loop (like this one) that activates after "Jarvis" is heard.

    # Example for a wake word loop:
    # while True:
    #     print("Listening for wake word 'Jarvis'...")
    #     wake_command = listen_for_command(prompt="Listening for wake word 'Jarvis'...", timeout=None, phrase_time_limit=3) # Listen indefinitely for wake word
    #     if wake_command and "jarvis" in wake_command:
    #         speak("Yes? How can I help?")
    #         user_command = listen_for_command(prompt="Waiting for your command...")
    #         if user_command:
    #             if "goodbye" in user_command or "exit" in user_command or "shut down" in user_command:
    #                 speak("Goodbye!")
    #                 break
    #             process_command(user_command)
    #         else:
    #             speak("I didn't catch your command.")
    #     elif wake_command and ("goodbye" in wake_command or "exit" in wake_command or "shut down" in wake_command):
    #         speak("Goodbye!")
    #         break
    # else: # Loop exited
    #     speak("Jarvis shutting down.")


    # Current simpler loop (listens for any command directly):
    try:
        while True:
            user_command = listen_for_command(prompt="Waiting for your command...")
            if user_command:
                if "goodbye" in user_command or "exit" in user_command or "shut down" in user_command:
                    speak("Goodbye!")
                    break
                process_command(user_command)
            # No explicit "didn't catch command" here, as listen_for_command handles its own feedback/logging
            # Add a small pause or specific condition to re-prompt if needed
    except KeyboardInterrupt:
        speak("Jarvis shutting down due to user interrupt.")
    finally:
        if engine: # Ensure engine is not None before trying to stop
            engine.stop() # Cleanly stop the TTS engine
        logging.info("Jarvis application terminated.")