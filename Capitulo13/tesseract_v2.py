from PIL import Image
import pytesseract
from pytesseract import Output
import numpy as np


def cleanFile(filePath, threshold):
    image = Image.open(filePath)
    # Define um valor de limiar para a imagem, e salva
    image = image.point(lambda x: 0 if x < threshold else 255)
    return image


def getConfidence(image):
    data = pytesseract.image_to_data(image, output_type=Output.DICT)
    text = data['text']
    confidences = []
    numChars = []

    for i in range(len(text)):
        if data['conf'][i] > -1:
            confidences.append(data['conf'][i])
            numChars.append(len(text[i]))
    
    return np.average(confidences, weights=numChars), sum(numChars)


filePath = 'textBad.png'
start = 80
step = 5
end = 200

for threshold in range(start, end, step):
    image = cleanFile(filePath, threshold)
    scores = getConfidence(image)
    print('threshold: ' + str(threshold) + ', confidence: ' + str(scores[0]) + ' numChars ' + str(scores[1]))
