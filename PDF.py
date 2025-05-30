import os
from google.cloud import vision
from google.cloud import translate_v2 as translate
from pdf2image import convert_from_path


# Set the path for the Google Cloud service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/rahaf/Desktop/spatial-ship-429707-f2-71947f8a45e5.json"


# Initialize the Vision and Translate clients
vision_client = vision.ImageAnnotatorClient()
translate_client = translate.Client()


def pic_to_text(infile: str) -> str:
   """Detects text in an image file and returns the detected text as a string."""
   # Instantiates a client
   client = vision.ImageAnnotatorClient()


   # Opens the input image file
   with open(infile, "rb") as image_file:
       content = image_file.read()


   image = vision.Image(content=content)


   # For dense text, use document_text_detection
   # For less dense text, use text_detection
   response = client.document_text_detection(image=image)
   text = response.full_text_annotation.text
   print(f"Detected text: {text}")


   return text


def translate_text(text, target_language='ar'):
   """Translates text into the target language."""
   result = translate_client.translate(text, target_language=target_language)
   return result['translatedText']


def translate_image_to_arabic(image_path):
   # Detect text in the image
   detected_text = pic_to_text(image_path)
  
   # Translate the detected text to Arabic
   translated_text = translate_text(detected_text)
   print(f"Translated text: {translated_text}")
  
   return translated_text


def save_translated_text(file_path, text):
   """Saves the translated text to a file ensuring right-to-left writing direction."""
   with open(file_path, 'w', encoding='utf-8') as file:
       file.write(text)


def process_pdfs_in_folder(folder_path):
   """Processes all PDF files in the specified folder."""
   for filename in os.listdir(folder_path):
       if filename.endswith(".pdf"):
           pdf_path = os.path.join(folder_path, filename)
           print(f"Processing {pdf_path}")
           images = convert_from_path(pdf_path)
           for i, image in enumerate(images):
               image_path = os.path.join(folder_path, f"{filename}_page_{i + 1}.png")
               image.save(image_path, "PNG")
               translated_text = translate_image_to_arabic(image_path)
               translated_text_file = os.path.join(folder_path, f"{filename}_page_{i + 1}_translated.txt")
               save_translated_text(translated_text_file, translated_text)
               print(f"Translated text for {image_path} saved to {translated_text_file}")


# Example usage
process_pdfs_in_folder('/') # Place input folder path here
