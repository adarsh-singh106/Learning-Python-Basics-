import speech_recognition as sr
import webbrowser
import pyttsx3
from musiclibrary import music
import requests

# Gobal Variabels
recognize_command = sr.Recognizer()  # Speech recognizer ko initialize kar rahe hain
engine = pyttsx3.init()  # pyttsx3 ka engine init ho raha hai — yeh text ko bolta hai
news_api = "6b1b8a599cfc4890b61f3ee6cebdbd3b"  # News API ka key (public mat rakhna future me)

#  Speak karne ka function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function jo input command handle karta hai
def function1(c):
    print(c)
    
    # Agar Jarvis ka naam liya gaya hai
    if "jarvis" in c.lower():
        speak("Yes,I am listening...How can i Hekp You")
        with sr.Microphone() as source:
            print("wating for command...")  # Mic se naya command sunne ke liye ready ho rahe hain
            audio = r.listen(source, timeout=4, phrase_time_limit=1)
            c = r.recognize_google(audio)
            function1(c)

    # Common commands ke liye conditions:
    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "open google" in c.lower():
        speak("Opening google")
        webbrowser.open("https://www.google.com/")

    elif "open chat" in c.lower():
        speak("Opening chatgpt")
        webbrowser.open("https://www.chatgpt.com/")

    elif "open gmail" in c.lower():
        speak("Opening gmail")
        webbrowser.open("https://www.mail.google.com/")

    elif "open git" in c.lower():
        speak("Opening github")
        webbrowser.open("https://www.github.com/")

    # Agar "play song" bola gaya ho
    elif c.lower().startswith("play"):
        song_id = c.lower().split(" ")[1]  # 'play' ke baad jo word hai, usse song_id maan lo
        song_link = music[song_id]  # music dictionary se link nikalo
        webbrowser.open(song_link)  # browser me song khol do

    # News sunani ho to
    elif "news" in c.lower():
        # API ka URL bana rahe hain
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"

        # API call kar rahe hain
        response = requests.get(url)

        # Agar response OK hai to
        if response.status_code == 200:
            data = response.json()  # Response ko JSON me parse karna
            articles = data.get("articles", [])  # Articles ki list nikalna

            # Har ek news ka title bol do
            for i, article in enumerate(articles, start=1):
                print(f"{i}. {article.get('title')}")
                speak(f"{i}. {article.get('title')}")
        else:
            print(f"Failed to fetch news: {response.status_code}")
            speak(f"Failed to fetch news: {response.status_code}")

# Main program yahan se start hota hai
if __name__ == "__main__":
    speak("Initialising jarvis...")  # Starting message

    while True:
        # Step 1: Wake word sunna (like "jarvis")
        r = sr.Recognizer()  # Har loop me recognizer naya banate hain (safe practice)

        try:
            # Step 2: Mic se audio lena
            with sr.Microphone() as source:
                print("Listening...")  # User kuch bole, uska wait ho raha hai
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            # Step 3: Speech ko text me convert karna
            command = r.recognize_google(audio)
            print("Recognizing...")
            print(command)

            # Step 4: Agar "jarvis" suna gaya ho to second command lo
            if "jarvis" in command.lower():
                speak("Yes,I am listening...How can i Hekp You")
                with sr.Microphone() as source:
                    print("wating for command...")  # Ab asli kaam ki baat sunni hai
                    audio = r.listen(source, timeout=4, phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    function1(command)

        #  Possible errors:
        except sr.WaitTimeoutError:
            print("No speech detected.")  # Time out ho gaya, kuch nahi bola gaya
        except sr.UnknownValueError:
            print("Could not understand the audio.")  # Speech samajh nahi aayi
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")
