#%%
from PIL import Image
import numpy as np

img = Image.open('academy.png')
img = img.convert('RGBA')
colors = img.getpixel((1,1))
print(colors)

data = np.array(img)   # "data" is a height x width x 4 numpy array
print(data)
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability



# Replace white with red... (leaves alpha values alone...)
#white_areas = (red == 177) & (blue == 36) & (green == 48)
#data[..., :-1][white_areas.T] = (255, 0, 0) # Transpose back needed
#print(data)

width = img.size[0] 
height = img.size[1] 
for i in range(0,width):# process all pixels
    for j in range(0,height):
        data = img.getpixel((i,j))
        #print(data) #(255, 255, 255)
        if (data[0]==177 and data[1]==36 and data[2]==48):
            img.putpixel((i,j),(193, 0, 42))

img.show()
# save the image
img.save('academy_new.png')
# %%
