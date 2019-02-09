from PIL import Image
from PIL import ImageDraw
import time

start = time.process_time()

fractImage = Image.new('RGB', (1000,1000), 0)

fractDraw = ImageDraw .Draw(fractImage)

colourR = 0
colourG = 0
colourB = 0

for row in range(1000):

    if colourR == 255:
        colourR = 0
    else:
        colourR +=1

    for col in range(1000):
        fractDraw.point((col,row), (colourR,colourG,colourB))
       

fractImage.save('fract.jpg')

end = time.process_time()