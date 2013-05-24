#!/usr/bin/python
#
# Copyright (c) 2009-2012, Dan "Ducky" Little & GeoMOOSE.org
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# Yay, PIL!!
import Image

import sys
import os


# All of these images are assumed to be 20x20.
# It's fine if they are smaller because they'll just get more padding,
# larger than 20x20 and it'll get a little trickier.
imagesRoot = '../htdocs/images/';
spriteFolders = ['toolbar/'];

try:
	os.remove(imageRoot+'all.png')
except:
	pass

all_files = list()
for path in spriteFolders:
	imgs = os.listdir(imagesRoot+path)
	imgs = map(lambda x: imagesRoot+path+x, imgs)
	all_files = all_files + imgs

images = list()
for f in all_files:
	# this test should be better... but I'm lazy.
	if((f.find('.png') > 0 or f.find('.gif') > 0) and f.find('-selected') < 0):
		images.append(f)
images.sort()

sprite = Image.new('RGBA', (40,len(images)*30), (0,0,0,0))

i = 0

cssHeader = """
.sprite-control {
	background-image: url('../images/all.png');
	background-repeat: no-repeat;
	height: 18px; /* nee, < 2.6 20px */
	width: 20px;
	display: inline-block;
	cursor: pointer;
	background-position: 0px -%dpx;	/* This should default to the 'find' icon */
	/* IE hacks for the sprites. */
	*zoom: 1;
	*display: inline;
}

"""


cssTemplate = """ .sprite-control-%s { background-position: 0px -%dpx; } """
cssSelectedTemplate = """ .sprite-control-%s-selected { background-position: -20px -%dpx !important; } """

cssText = "/*\n" + open('../LICENSE', 'r').read() + '*/\n\n' + cssHeader

height = (len(images)+1)*30+10
findPosition = 0
for image in images:
	imagePath = image.split('/')
	imageName = imagePath[-1].split('.')[0]

	selectedImage = image
	for ext in ['gif','png','jpg']:
		selectedImage = selectedImage.replace('.'+ext,'-selected.'+ext)

	if(not(os.path.isfile(selectedImage))):
		selectedImage = image

	icon = Image.open(image)
	selected_icon = Image.open(selectedImage)
	
	offsetLeft = (20 - icon.size[0]) / 2
	offsetHeight = (20 - icon.size[1]) / 2
	sprite.paste(icon, (offsetLeft, i*30+10+offsetHeight))

	offsetLeft = 20 + (20 - selected_icon.size[0]) / 2
	offsetHeight = (20 - selected_icon.size[1]) / 2
	sprite.paste(selected_icon, (offsetLeft, i*30+10+offsetHeight)) 

	i+=1


	h = height-(height-((i-1)*30))+10
	cssText += cssTemplate % (imageName , h)
	cssText += cssSelectedTemplate % (imageName, h)
	cssText += '\n'
	if(imageName == 'find'):
		findPosition = h
	#print cssTemplate % (imageName , ((i+1)*30+10))

print cssText % findPosition
sprite.save(imagesRoot+'all.png')
