import pickle
from PIL import Image, ImageDraw

with open("DeepTable//tables.pickle", 'rb') as f:
    data_new_f = pickle.load(f)
print(data_new_f[0][1], '\n', data_new_f[1][1])
c = 0
width_cell, height_cell = 200, 25
if(True):
    for data_new in data_new_f[0]:
        c += 1
        new_img = Image.new(mode="RGB", size=(len(data_new[0]) * width_cell, len(data_new) * height_cell))
        draw = ImageDraw.Draw(new_img)
        draw.rectangle([(0, 0), (len(data_new[0]) * width_cell, len(data_new) * height_cell)], fill="white")
        for row, data in enumerate(data_new):
            for i, text in enumerate(data):
                w, h = draw.textsize(text)
                draw.line([((i * width_cell), 0), ((i * width_cell), len(data_new) * height_cell)], fill="black",
                          width=0)
                draw.text(((i * width_cell) + ((width_cell-w)/2), row*height_cell + (h/2)), text, fill="black",
                          align="left")
        draw.text((0, 0), str(data_new_f[1][c-1]), fill="red", align="left")
        try:
            new_img.save('pil_out\\' + str(c) + '.jpg', quality=100)
        except OSError:
            print("skip")

print(data_new_f[0][0])
print(data_new_f[1][1])

# 0 1 0 - ver
# 0 0 1 - matrix
# 1 0 0 - hor





