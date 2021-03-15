from PIL import Image
import pytesseract

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    # Define um valor de limiar para a imagem, e salva
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)
    return image


image = cleanFile('textBad.png', 'textCleaned.png')
# chama o tesseract para fazer OCR na imagem recém criada
print(pytesseract.image_to_string(image))
