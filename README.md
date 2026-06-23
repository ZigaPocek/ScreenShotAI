# ScreenShotAI
AI program that sends you the answers through computers notification system.

!DISCLAIMER: this version uses google gemini 2.5 flash and only works for the macOS.


### 1. Install the New Google Library ###

```pip install watchdog google-genai pillow```

### 2. Set Up your API key ###

```export GEMINI_API_KEY="your_actual_gemini_api_key"```

### 3. Create new folder for screenshots (in the project folder) ###

```mkdir screenshots```

### 4. Tell macOS to save screenshots there ###

```defaults write com.apple.screencapture location location_to_screenshots_folder```

### 5. Apply the changes ###

```killall SystemUIServer```


