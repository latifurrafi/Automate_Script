import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Load your image
image = Image.open('image.png')
text = pytesseract.image_to_string(image)

print("Extracted Text:\n", text)
