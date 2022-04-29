import os
from PIL import Image

def transform_image(fname):
	img = Image.open(fname)
	pixel_arr = img.load()
	img_width = img.size[0]
	img_height = img.size[1]

	# sort every slice of pixels
	for y in range(img_height):
		pixel_slice = []
		for x in range(img_width):
			pixel_slice.append(pixel_arr[x,y])
			pixel_slice = sorted(pixel_slice)
		# copy over sorted slice into original pixel array
		for i in range(img_width):
			pixel_arr[i,y] = pixel_slice[i]
	pixel_arr_sorted = []
	for y in range(img_height):
		for x in range(img_width):
			pixel_arr_sorted.append(pixel_arr[x,y])

	# save new image
	new_img = Image.new('RGB', img.size)
	new_img.putdata(pixel_arr_sorted)
	new_img.show()
	new_img.save(f'{fname}_transformed.jpg')

directory = 'images'
for root, dirs, files in os.walk(directory, topdown=False):
    for fname in files:
        transform_image(fname=os.path.join(root, fname))
