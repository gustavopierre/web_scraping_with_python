from PIL import Image
import pytesseract
from pytesseract import Output

print(pytesseract.image_to_string(Image.open('text.png'), output_type=Output.BYTES))
#print(pytesseract.image_to_boxes(Image.open('text.png')))
print(pytesseract.image_to_data(Image.open('text.png'), output_type=Output.DICT))
