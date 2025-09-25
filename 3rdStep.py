
from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()  # Loads variables from .env

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# response = model.generate_content("Explain how AI works in a few words")
# print(response.text)


filename = r"D:\Desktop Backup\Python_Practice\PDFSpliting\extracted_text_part2.txt"
try:
    text = ""
    with open( filename, 'r', encoding='utf-8') as file:
        for line in file:
            text += line
    print("Read file and saved in text")
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Error reading the file!")



prompt = f"""
Summarize the text and create markdown file keeping all important topic subtopic and description.
```{text}```
"""



response = model.generate_content(prompt)

output_md = os.path.basename(filename).replace("\\","_").replace('.txt', '.md')

with open(output_md, "w", encoding="utf-8") as md_file:
    md_file.write(response.text)