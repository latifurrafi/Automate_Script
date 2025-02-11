import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Load your image
image = Image.open('/home/rafi/VSCODE/Automate_Script/pic.png')
text = pytesseract.image_to_string(image)

print("Extracted Text:\n", text)

print("Rafi")