# Smart Screenshot Organizer

Smart Screenshot Organizer is an AI-powered screenshot management tool built with Python.

The application continuously monitors the screenshots folder using Watchdog and automatically classifies screenshots using OpenAI's CLIP model. Based on the detected content, screenshots are moved into categorized folders such as Gaming, Coding, Social Media, and more.

## Features

- Real-time screenshot detection
- AI-based screenshot classification
- Automatic folder organization
- CLIP zero-shot image classification
- Supports multiple screenshot categories
- File system automation using Watchdog
- OCR support groundwork using Tesseract

## Categories

- Programming Screenshot
- Video Game Screenshot
- Social Media Post
- College Study Material
- Important Document
- Meme Image
- YouTube Video
- Music Player
- Online Shopping
- Error Message
- Desktop Wallpaper
- Chat Conversation

## Tech Stack

- Python
- Transformers
- OpenAI CLIP
- Watchdog
- Pillow
- Pytesseract

## How It Works

1. The program watches the screenshots folder in real time.
2. When a screenshot is detected:
   - The image is processed using the CLIP model
   - The screenshot is classified into the closest matching category
   - The file is automatically moved into the appropriate folder

## Future Improvements

- OCR-based screenshot renaming
- Semantic screenshot search
- GUI application
- Duplicate screenshot detection
- AI-generated screenshot summaries

## Run

Open CMD or Terminal and give command:
python main.py
