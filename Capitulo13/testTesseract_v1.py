from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('text.png')))
print(pytesseract.image_to_boxes(Image.open('text.png')))
print(pytesseract.image_to_data(Image.open('text.png')))
