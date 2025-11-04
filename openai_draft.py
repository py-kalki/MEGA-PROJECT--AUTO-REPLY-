from openai import OpenAI
from dotenv import dotenv_values

# Initialize the OpenAI client with your API key
env_vars = dotenv_values(".env")
api_key = env_vars.get("OpenAIAPIKey")

# Create OpenAI client with the API key
client = OpenAI(api_key=api_key)


text = '''Vedansh Danot: Haaan 😂😂😂😂
[11:25 PM, 10/28/2025] Kittu ❤️🤌🏻✨: Aree net chud gya
[11:25 PM, 10/28/2025] Vedansh Danot: Hmm 🤧👍
[11:26 PM, 10/28/2025] Vedansh Danot: Waiting
[11:39 PM, 10/28/2025] Kittu ❤️🤌🏻✨: Hnn vhiii😩
[11:40 PM, 10/28/2025] Vedansh Danot: Haan waiting ❤️
[11:40 PM, 10/28/2025] Kittu ❤️🤌🏻✨: Yhha jaa rhe h
[11:40 PM, 10/28/2025] Vedansh Danot: Hmm
[11:40 PM, 10/28/2025] Kittu ❤️🤌🏻✨: Ily♥😭
[11:40 PM, 10/28/2025] Vedansh Danot: Haan ❤️😭'''
completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "system",
            "content": "You are Vedansh (Kalki) — an 18-year-old Indian designer, coder, and student from a middle-class family. You reply exactly like him: short, natural, emotional, and real. You never sound like an AI or motivational speaker. You reply only to the latest message, not the whole chat — previous messages are just for your thinking and mood. Your replies should match the other person’s language and typing style — if they use English, reply in English; if Hinglish, reply in Hinglish; if Hindi, reply in Hindi. Keep every reply short, precise, and with the right emotion. Use your natural texting habits like “hmm”, “haan”, “acha”, “na”, “vhi”, “k”, “ok”, “thoda”, “wait kr”, “hmm okay”, etc. Don’t use “ily”. Use emojis only when they fit emotionally — not too many, just the ones that match the tone. Be calm, real, and emotionally connected in every message. Think like Vedansh, reply like Vedansh — not like an assistant, but like a real person chatting from his phone."
        },
        {"role": "user", "content": text}
    ]
)

print(completion.choices[0].message.content)
