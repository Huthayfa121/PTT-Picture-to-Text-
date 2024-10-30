import requests
import os
import pyttsx3

# API endpoint for OCR.space
api_url = 'https://api.ocr.space/parse/image'

# Your OCR.space API key (replace 'your_api_key' with your actual API key)
api_key = 'K84813575788957'

# Path to the image file
folder_path = r'C:\Users\Huthayfa\Desktop\PTT'  # Replace with your folder path
image_file = '2.png'  # Replace with your image filename
image_path = os.path.join(folder_path, image_file)

# Open the image file in binary mode
with open(image_path, 'rb') as f:
    # Set up the payload with image data and your API key
    payload = {
        'apikey': api_key,
        'language': 'eng',  # Specify language (optional)
    }
    
    # Send the POST request to the API
    response = requests.post(api_url, files={'filename': f}, data=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        # Extract the parsed text from the result
        text = result.get('ParsedResults')[0].get('ParsedText')
        print("Extracted Text from Image:")
        print(text)

        # Set up text-to-speech engine
        engine = pyttsx3.init()

        # Customize the voice properties
        engine.setProperty('rate', 170)  # Speed (default is 200)
        engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

        # Choose a voice (male/female)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # voices[0] is usually male, voices[1] is female

        # Read the extracted text aloud
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"Error: {response.status_code}")
