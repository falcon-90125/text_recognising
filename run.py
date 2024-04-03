import easyocr
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
from importlib import import_module

imp = import_module('coordinates') # координаты областей распознавания

img_path = 'input\passport.JPG'

img = mpimg.imread(img_path)

plt.imshow(Image.fromarray(img)) # исходное изображение
plt.show()

plt.imshow(Image.fromarray(img[imp.wny1:imp.wny2, imp.wnx1:imp.wnx2])) # фрагмент для распознавания
plt.show()

reader = easyocr.Reader(['ru']) # Объект OCR

# Функция распознавания
def recognising(y1, y2, x1, x2):
    resalts = reader.readtext(img[y1:y2, x1:x2])

    resalts_conc = ''
    for i in range(len(resalts)):
        resalts_conc += f"{resalts[i][1]} "
    resalts_conc = resalts_conc.replace(' ,', ',')
    return resalts_conc[:-1]


# Потребляемая мощность, Вт
power_consumption_name = recognising(imp.wny1, imp.wny2, imp.wnx1, imp.wnx2)
print(power_consumption_name)

# Значение "Потребляемая мощность"
power_consumption_vol = recognising(imp.wvy1, imp.wvy2, imp.wvx1, imp.wvx2)
print(power_consumption_vol)

# Коррелированная цветовая температура, K
colorful_temperature_name = recognising(imp.tny1, imp.tny2, imp.tnx1, imp.tnx2)
print(colorful_temperature_name)

# Значение "Коррелированная цветовая температура"
colorful_temperature_vol = recognising(imp.tvy1, imp.tvy2, imp.tvx1, imp.tvx2)
print(colorful_temperature_vol)
