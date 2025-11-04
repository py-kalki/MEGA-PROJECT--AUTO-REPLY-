import pyautogui
import time
import pyperclip
from openai import OpenAI
from dotenv import dotenv_values

# Initialize the OpenAI client with your API key
env_vars = dotenv_values(".env")
api_key = env_vars.get("OpenAIAPIKey")
senders_name = env_vars.get("SENDER_NAME")

# Create OpenAI client with the API key
client = OpenAI(api_key=api_key)

print("INITIALIZING AUTO-CHAT...")

time.sleep(3)

pyautogui.moveTo(1045 ,1162 , duration=0.8)
pyautogui.click()

def is_last_text_from_sender(chat_log , sender_name=senders_name):
    lines = [line.strip() for line in chat_log.splitlines() if line.strip()]
    for line in reversed(lines):
        if sender_name in line:
            return True
        elif "You sent" in line:
            return False
    
    # If no sender found (edge case)
    return False
while True:
    

    time.sleep(0.5)

    pyautogui.moveTo(707 , 228 , duration=1)
    time.sleep(0.3)
    pyautogui.mouseDown(button='left')
    time.sleep(0.3)
    pyautogui.moveTo(1859, 1034, duration=2)   # smoother drag
    pyautogui.mouseUp(button='left')
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    pyautogui.click()


    chat_history = pyperclip.paste()
    print("THE CHAT 👇")
    print("Copied_text:\n", chat_history)

    # if is_last_text_from_sender(chat_history):
    if is_last_text_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {
                    "role": "system",
                    "content": "You are Vedansh (Kalki) — an 18-year-old Indian designer, coder, and student from a middle-class family. You reply exactly like him: short, natural, emotional, and real. You never sound like an AI or motivational speaker. You reply only to the latest message, not the whole chat — previous messages are just for your thinking and mood. Your replies should match the other person’s language and typing style — if they use English, reply in English; if Hinglish, reply in Hinglish; if Hindi, reply in Hindi. Keep every reply short, precise, and with the right emotion. Use your natural texting habits like “hmm”, “haan”, “acha”, “na”, “vhi”, “k”, “ok”, “thoda”, “wait kr”, “hmm okay”, etc. Don’t use “ily”. Use emojis only when they fit emotionally — not too many, just the ones that match the tone. Be calm, real, and emotionally connected in every message. Think like Vedansh, reply like Vedansh — not like an assistant, but like a real person chatting from his phone."
                },
                {"role": "user", "content": chat_history}
            ]
        )
        if not chat_history.strip():
            print("no text copied")
            exit(
            )
        responce = completion.choices[0].message.content
        print("THE REPLY 👇")
        print(responce)

        pyperclip.copy(responce if responce is not None else "")

        pyautogui.click(1091, 1101, duration=0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')
        print("✅ Message sent successfully!")