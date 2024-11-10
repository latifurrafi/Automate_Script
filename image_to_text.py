import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

image = Image.open('/home/rafi/VSCODE/Automate_Script/test.png')

text = pytesseract.image_to_string(image)

print("Extracted Text:\n", text)
