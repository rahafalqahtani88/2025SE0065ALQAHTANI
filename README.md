# 2025SE0065ALQAHTANI
# Semi-Automated Translation Pipeline

This project automates the translation of various media types (documents, images, websites, and videos) from English to Arabic. It leverages cloud-based APIs to perform high-quality translation and format content for right-to-left (RTL) display. This pipeline was developed for the Arabic Day of AI educational initiative.

---

## 📦 Supported Media Types

- 📄 PowerPoint Presentations (`.pptx`)
- 📝 Word Documents (`.docx`)
- 📕 PDF Documents (with embedded images/text)
- 🖼️ Images (`.png`, `.jpg`, `.jpeg`)
- 🎥 Videos (YouTube, Vimeo, etc.)

---

## ⚙️ Prerequisites

Install the required packages using pip:

```bash
pip install requests json os uuid python-pptx python-docx pdf2image google-cloud-vision google-cloud-translate dotenv elevenlabs
```

You will also need:
- Microsoft Azure Translator subscription key
- Google Cloud Vision & Translate credentials JSON
- ElevenLabs API key saved in a `.env` file

---

## 🧪 1. Translate PowerPoint & Word Documents

### PowerPoint (.pptx)
1. Place `.pptx` files in a local folder.
2. Insert your Azure `subscription_key`, `endpoint`, and `location` in the script.
3. Set input and output folder paths.
4. Run the script to translate and save Arabic versions.

### Word (.docx)
1. Same process as PowerPoint, using the `python-docx` library.
2. The script also sets paragraph formatting to RTL.

---

## 🖼️ 2. Translate PDFs & Images (OCR-based)

### PDFs
1. Convert PDF to images using `pdf2image`.
2. Detect text using Google Cloud Vision API.
3. Translate extracted text using Google Translate API.
4. Save results as `.txt` files for manual overlay.

### Images
1. Run `process_images_in_folder()` on a folder with `.png`, `.jpg`, `.jpeg` files.
2. Translated text is saved with RTL encoding.

---

## 🎬 4. Dub Educational Videos to Arabic

1. Set your ElevenLabs API key in `.env`.
2. Use `dubbing.py` to pass a video URL and desired language.
3. The video is processed and saved locally in a `data/` folder.

The process is monitored via `dubbing_utils.py`, which checks for status every 10 seconds.

---

## 📁 Recommended Folder Structure

```
translation-pipeline/
├── documents/
├── images/
├── pdfs/
├── websites/
├── videos/
├── .env
├── credentials.json
├── translate_pptx.py
├── translate_docx.py
├── translate_pdfs.py
├── translate_images.py
├── translate_websites.py
├── dubbing.py
└── dubbing_utils.py
```

---

## 📈 Performance

⚡ Achieves **2.4x faster** translation compared to manual methods, enabling scalable and rapid localization of content.


