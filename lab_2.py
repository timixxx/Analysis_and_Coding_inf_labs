from PIL import Image
import cv2
import numpy as np

path = 'sources/lab_2/rgb_img.bmp'

with open(path, 'rb') as f:
    im = Image.open(f)

    print('\nFilename:', path.split(sep='/')[2])
    print('File size:', im.size)
    print('Width:', im.width)
    print('Height:', im.height)
    print('Dots Per Inch: ', im.info['dpi'])
    print('Compression:', im.info['compression'])
    print('Mode:', im.mode)
    print('Format:', im.format, '\n')

    im_zero = im.convert('L')
    im_zero.save('sources/lab_2/zero_channel.bmp')

    img_cv = cv2.imread(path, 1)

    blue_ch = img_cv[:, :, 0]  # getting only blue channel from image
    blue_im = np.zeros(img_cv.shape)  # creating new array filled with zeros
    blue_im[:, :, 0] = blue_ch  # filling zeros array with blue channel elements

    cv2.imwrite('sources/lab_2/blue.bmp', blue_im)
    # cv2.imwrite('sources/lab_2/blue_ch.bmp', blue_ch)

    # cv2.imshow('blue', blue_channel)
    # cv2.waitKey(0)

    green_ch = img_cv[:, :, 1]
    green_im = np.zeros(img_cv.shape)
    green_im[:, :, 1] = green_ch
    cv2.imwrite('sources/lab_2/green.bmp', green_im)

    red_ch = img_cv[:, :, 2]
    red_im = np.zeros(img_cv.shape)
    red_im[:, :, 2] = red_ch
    cv2.imwrite('sources/lab_2/red.bmp', red_im)

    arr = np.asarray(im_zero)  # converting image to array

    slicer = np.array([[1 for i in range(arr.shape[1])] for j in range(arr.shape[0])])  # filling new array with 1's

    for i in range(8):
        slicer *= 2  # making each slice brighter
        byte_and = slicer & arr
        im_slice = Image.fromarray(byte_and)  # converting image back to array
        im_slice = im_slice.convert('RGB')
        im_slice.save(f'sources/lab_2/slice_{i}.bmp')
