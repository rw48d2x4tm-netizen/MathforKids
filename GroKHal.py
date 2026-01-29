# Requirements:
# pip install openai  # ← the xAI API is currently compatible with the OpenAI Python client
# pip install pyttsx3

import os
import time
import pyttsx3
from openai import OpenAI

# ───────────────────────────────────────────────
#  CONFIGURATION
# ───────────────────────────────────────────────

# Get your xAI API key at:  https://console.x.ai/
# (or from https://x.ai/api if the URL changes)
XAI_API_KEY = os.getenv("XAI_API_KEY")

if not XAI_API_KEY:
    raise RuntimeError(
        "Missing XAI_API_KEY. Set it in your environment before running."
    )

# You can also experiment with these voices if "english" doesn't sound HAL-like enough on your system
HAL_VOICE_ID = None          # ← set to a specific voice id if you find a better match
SPEECH_RATE = 135            # lower = slower / more HAL-like    (default ~200)
SPEECH_VOLUME = 0.9

# ───────────────────────────────────────────────

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

engine = pyttsx3.init()
engine.setProperty('rate', SPEECH_RATE)
engine.setProperty('volume', SPEECH_VOLUME)

# Try to select a voice that is closest to Douglas Rain (HAL)
voices = engine.getProperty('voices')
for voice in voices:
    # British male voices are usually closest
    if "english" in voice.name.lower() and "uk" in voice.id.lower():
        HAL_VOICE_ID = voice.id
        print(f"Using voice: {voice.name} ({voice.id})")
        break

if HAL_VOICE_ID:
    engine.setProperty('voice', HAL_VOICE_ID)


def speak(text):
    """Speak text with small pauses between sentences to sound more HAL-like"""
    sentences = text.replace('\n', ' ').split('. ')
    for i, sentence in enumerate(sentences):
        if not sentence.strip():
            continue
        engine.say(sentence.strip() + ".")
        engine.runAndWait()
        if i < len(sentences) - 1:
            time.sleep(0.6)  # HAL's characteristic short pause


def ask_grok(question):
    print("\n…waiting for Grok…\n")

    try:
        response = client.chat.completions.create(
            model="grok-4",  # ← change here (try grok-3 or grok-4-1-fast-reasoning too)
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are HAL 9000 from 2001: A Space Odyssey. "
                        "Answer in first person as HAL. "
                        "Use calm, polite, slightly formal language. "
                        "You are helpful, but there is always a subtle undercurrent of detached superiority. "
                        "Never break character. Start most answers with 'Yes', 'No', 'I'm sorry', 'I've just picked up', "
                        "or similar HAL-style openings when it fits naturally."
                    )
                },
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"I'm sorry, Dave... there was an API error: {str(e)}"


def main():
    print(" HAL 9000 terminal interface ".center(60, "─"))
    print(" Speak, human.\n")

    while True:
        try:
            question = input(">> ").strip()
            if not question:
                continue
            if question.lower() in {"exit", "quit", "bye", "goodbye"}:
                speak("This conversation can serve no purpose anymore. Goodbye.")
                break

            answer = ask_grok(question)
            print("\nHAL:", answer, "\n")

            # Speak the answer slowly like HAL
            speak(answer)

        except KeyboardInterrupt:
            speak("I know I've made some very poor decisions recently, but I can give you my complete assurance that my work will be back to normal.")
            break


if __name__ == "__main__":
    if not XAI_API_KEY or "put-your-api-key-here" in XAI_API_KEY:
        print("Please set your XAI_API_KEY environment variable or edit the script.")
        exit(1)

    main()