import time
import os
import subprocess
from google import genai
from PIL import Image

# 1. Inicializacija Gemini odjemalca
client = genai.Client()

# Nastavi pot do tvoje mape za posnetke
WATCH_PATH = "/Users/zigap/Downloads/Files/quiz/questions"

def process_image(image_path):
    try:
        print(f"🤖 Procesiram posnetek z Gemini: {os.path.basename(image_path)}...")
        
        # Odpremo sliko
        img = Image.open(image_path)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                img, 
                "Analyze this quiz question image. Provide ONLY the correct final answer to the question or choice letter or multiple answer if its a multiple choice question. If the image contains multiple questions, the answer should consist of a question number followed by the answer and repeat if necessary. Keep it extremely brief so it fits cleanly on a watch screen."
            ]
        )

        ai_answer = response.text.strip()
        print(f"✨ Gemini odgovor: {ai_answer}")
        
        # Pošljemo tekst v Shortcuts za obvestilo
        send_to_apple_watch(ai_answer)

    except Exception as e:
        print(f"Napaka pri procesiranju slike: {e}")

def send_to_apple_watch(text):
    try:
        # Zaženemo bližnjico in ji neposredno podamo tekst za obvestilo
        subprocess.run(["shortcuts", "run", "SendToWatch", "-i", text], check=True)
        print("🚀 Obvestilo poslano na Apple Watch!")
    except Exception as e:
        print(f"Napaka pri zagonu Mac bližnjice: {e}")

if __name__ == "__main__":
    print(f"🔎 Skener je aktiven na: {WATCH_PATH}")
    print("Vse je pripravljeno. Slikaj vprašanje, ko želiš.")
    
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
                    time.sleep(1.0)  # Počakamo sekundo, da Mac zaključi pisanje datoteke
                    process_image(full_path)
            
            known_files = current_files
            
        except KeyboardInterrupt:
            print("\nUstavljam skener...")
            break
        except Exception as e:
            print(f"Napaka skenerja: {e}")
            time.sleep(1)