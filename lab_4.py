from stegano import lsb
import numpy as np
from PIL import Image

image_to_hide = open('images_to_hide/kirill_smart.png', 'rb')

file = image_to_hide.read()

secret_image = lsb.hide('images_to_hide/kirill_kfc.jpg', file)

secret_image.save("images_to_hide/secret_image.png")
secret_image.close()

founded_image = open('images_to_hide/founded_image.png', 'wb')
secret = lsb.reveal("images_to_hide/secret_image.png")

secret = bytes(secret, 'utf-8')
founded_image.write(secret)

founded_image.close()

# with open('images_to_hide/secret_image.png', 'rb') as f:
#     im = Image.open(f)
#     im_zero = im.convert('L')
#     im_zero.save('images_to_hide/zero_channel.bmp')
#
#     arr = np.asarray(im_zero)
#
#     slicer = np.array([[10 for i in range(arr.shape[1])] for j in range(arr.shape[0])])  # filling new array with 1's

    # for i in range(8):
    #     slicer *= 2  # making each slice brighter
    #     byte_and = slicer & arr
    #     im_slice = Image.fromarray(byte_and)  # converting image back to array
    #     im_slice = im_slice.convert('RGB')
    #     im_slice.save(f'images_to_hide/slice_{i}.bmp')


