# Code By Atul Kushwaha

import google.generativeai as genai

# Configure the API key securely
#get api key on:https://aistudio.google.com/app/apikey
genai.configure(api_key="YOUR_API_KEY_HERE")

# Load the Gemini model (flash version for faster responses)
#you can add your own models also
model = genai.GenerativeModel("gemini-1.5-flash")

print("Hello Sir\n How Can I help You\n Type\t'off'\tTo End this Session") # welcome message

while True:
    q = input("Enter your Query : ")
    if q.lower() == "off":
        print("Session ended.")
        break
    try:
        response = model.generate_content(f"{q}")
        print("Gemini:", response.text)
    except:
        print("Error:")
