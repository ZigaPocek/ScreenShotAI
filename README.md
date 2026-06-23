# ScreenShotAI
AI program that sends you the answers through computers notification system for asnwering quizzes.

!DISCLAIMER: this version uses google gemini 2.5 flash and only works for the macOS.

### 0. Set up notification shortcut on Mac ###

- Create new shortcut in Shortcuts and name it "SendToNotif".

- From actions drag "Show Notification" to the workspace.

- Set it up as ```Show Notification "Shortcut Input"```

- In the Details section check "Use as Quick Action" and set ```Receive "Text" from "Quick Actions"```

### 1. Install the New Google Library ###

Pip3:

```pip3 install watchdog google-genai pillow```

HomeBrew:

```/opt/homebrew/bin/pip3.10 isntall watchdog google-genai pillow```

### 3. Create new folder for screenshots (in the project folder) ###

```mkdir screenshots```

### 4. Tell macOS to save screenshots there ###

```defaults write com.apple.screencapture location location_to_screenshots_folder```

### 5. Apply the changes ###

```killall SystemUIServer```

### 6. Move to project folder in the Terminal ###

Disclaimer: Do not forget to change ```WATCH_PATH``` in ```watch_quiz_gemini.py``` to the screenshot map location!!!

Run (pip3):

```export GEMINI_API_KEY="your_actual_gemini_api_key"```

```python3 watch_quiz_gemini.py```

Run (homebrew):

```export GEMINI_API_KEY="your_actual_gemini_api_key"```

```/opt/homebrew/bin/pip3.10 watch_quiz_gemini.py```



