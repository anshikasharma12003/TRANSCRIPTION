import requests

# API key
API_KEY = 'ec5a498bd4d75cb9df59c4a427bcb7f8ceef0956'

# local audio file
AUDIO_FILE = "C:\\Users\\Anshika Sharma\\Videos\\test.mp3"

def audio(file_path, api_key):
    url = "https://api.deepgram.com/v1/listen"
    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "audio/mp3"  
    }
    
    # Send the audio file for transcription
    with open(file_path, "rb") as audio_file:
        response = requests.post(url, headers=headers, data=audio_file)
    
    if response.status_code == 200:
        result = response.json()
        
        # Print the full JSON response for debugging
        print("Full JSON Response:")
        print(result)
        
        # Extract transcribed text from JSON
        channels = result.get("results", {}).get("channels", [{}])
        if channels:
            alternatives = channels[0].get("alternatives", [{}])
            if alternatives:
                transcribe = alternatives[0].get("transcript", "No transcript exist")
                with open("transcribe.docx", "w", encoding="utf-8") as file:
                    file.write(transcribe + "\n")
                print("Transcribe saved to transcribe.docx")
            else:
                print("No alternatives available")
        else:
            print("No channels available")
    else:
        print("Error:", response.status_code, response.docx)

if __name__ == '__main__':
   audio(AUDIO_FILE, API_KEY)
