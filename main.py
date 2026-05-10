import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

observer = Observer()

folder_path = r"C:\Users\Saad\Pictures\Screenshots"

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        image_path = event.src_path
        if image_path.endswith(".png"):
            print("Screenshot name: " + os.path.basename(image_path))
            time.sleep(2)
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img)
            clean_text = text.strip()
            clean_text = clean_text.lower()
            #clean_text = clean_text.replace(" ", "_")
            #clean_text = clean_text.replace("\n", "_")
            words = clean_text.split()
            words = [word for word in words if len(word) > 2]
            if len(words) == 0:
                new_name = os.path.basename(image_path)
            else:
                new_name = "_".join(words[:5]) + ".png"
            
            new_path = os.path.join(folder_path, new_name)
            print(new_name)
            
            

handler = MyHandler()

observer.schedule(handler, folder_path)

observer.start()
print("Watching Started")

while True:
    time.sleep(1)


