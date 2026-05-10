from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import shutil
import os
import time

gaming_folder = r"C:\Users\Saad\Desktop\Gaming"
coding_folder = r"C:\Users\Saad\Desktop\Coding"
social_folder = r"C:\Users\Saad\Desktop\Social"
random_folder = r"C:\Users\Saad\Desktop\Random"

labels = [
    "college study material",
    "programming screenshot",
    "video game screenshot",
    "social media post",
    "important document",
    "meme image",
    "youtube video",
    "music player",
    "online shopping",
    "error message",
    "desktop wallpaper",
    "chat conversation"
]

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def classify_image(image_path):

    with Image.open(image_path) as img:

        inputs = processor(
    text=labels,
    images=img,
    return_tensors="pt",
    padding=True
)

        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probs = logits.softmax(dim=1)

        for label, prob in zip(labels, probs[0]):
            print(label, ":", round(prob.item() * 100, 2))

        best_match = probs.argmax(dim=1).item()
        best_probability = probs[0][best_match].item() * 100
        if best_probability < 50:
            category = "random"

        else:
            category = labels[best_match]
                
                

    file_name = os.path.basename(image_path)
    destination_gaming_folder = os.path.join(gaming_folder, file_name)
    destination_coding_folder = os.path.join(coding_folder, file_name)
    destination_social_folder = os.path.join(social_folder, file_name)
    destination_random_folder = os.path.join(random_folder, file_name)



    #if category == "gaming":
        #print(category)
        #destination_folder = gaming_folder
        #print(destination_gaming_folder)
        #time.sleep(2)
        #shutil.move(image_path, destination_gaming_folder)

    #elif category == "coding":
        #print(category)
        #destination_folder = coding_folder
        #print(destination_coding_folder)
        #time.sleep(2)
        #shutil.move(image_path, destination_coding_folder)

    #elif category == "social media":
        #print(category)
        #destination_folder = social_folder
        #print(destination_social_folder)
        #time.sleep(2)
        #shutil.move(image_path, destination_social_folder)

    #else:
        #print(category)
        #destination_folder = random_folder
        #print(destination_random_folder)
        #time.sleep(2)
        #shutil.move(image_path,destination_random_folder)

    folder_map = {

    "video game screenshot": gaming_folder,

    "programming screenshot": coding_folder,

    "social media post": social_folder,

    "college study material": random_folder,

    "important document": random_folder,

    "meme image": random_folder,

    "youtube video": random_folder,

    "music player": random_folder,

    "online shopping": random_folder,

    "error message": coding_folder,

    "desktop wallpaper": random_folder,

    "chat conversation": social_folder,

    "random": random_folder
}
    destination_folder = folder_map[category]

    destination_path = os.path.join(destination_folder, file_name)

    print(category)
    print(destination_path)

    time.sleep(2)

    shutil.move(image_path, destination_path)

    return category

