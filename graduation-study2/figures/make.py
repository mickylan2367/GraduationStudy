

from PIL import Image

im1 = Image.open('henonmap_sorted.png')
im2 = Image.open('ikedamap_ordinaldistribution.png')

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

pics = get_concat_h(im1, im2)
pics.show()
pics.save('yoko.png')
# get_concat_v(im1, im1).save('data/dst/pillow_concat_v.jpg')