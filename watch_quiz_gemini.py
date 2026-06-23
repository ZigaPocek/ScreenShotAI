import time
import os
import subprocess
from google import genai
from PIL import Image

client = genai.Client()

WATCH_PATH = "location_to_screenshots_folder"

def process_image(image_path):
    try:
        print(f"🤖 Processing the screenshot with Gemini: {os.path.basename(image_path)}...")
        
        img = Image.open(image_path)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                img, 
                "Analyze this quiz question image. Provide ONLY the correct final answer to the question or choice letter or multiple answer if its a multiple choice question. If the image contains multiple questions, the answer should consist of a question number followed by the answer and repeat if necessary. Keep it extremely brief so it fits cleanly on a watch screen."
            ]
        )

        ai_answer = response.text.strip()
        print(f"✨ Gemini answer: {ai_answer}")
        
        send_to_notif(ai_answer)

    except Exception as e:
        print(f"Error with processing the image: {e}")

def send_to_notif(text):
    try:
        subprocess.run(["shortcuts", "run", "SendToNotif", "-i", text], check=True)
        print("🚀 Notification sent!")
    except Exception as e:
        print(f"Error with running Mac shortcut{e}")

if __name__ == "__main__":
    print(f"🔎 Scanner is active on: {WATCH_PATH}")
    print("Everything is ready. Take a picture when ready")
    
    known_files = set(os.listdir(WATCH_PATH))

    while True:
        try:
            time.sleep(0.5)
            current_files = set(os.listdir(WATCH_PATH))
            new_files = current_files - known_files
            
            for filename in new_files:
                if filename.startswith('.'):
                    continue
                    
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    full_path = os.path.join(WATCH_PATH, filename)
                    time.sleep(1.0)  
                    process_image(full_path)
            
            known_files = current_files
            
        except KeyboardInterrupt:
            print("\nCreating scanner...")
            break
        except Exception as e:
            print(f"Scanner error: {e}")
            time.sleep(1)