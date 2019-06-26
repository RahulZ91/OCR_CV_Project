import pytesseract
from pytesseract import Output
import cv2
import time
import nltk

# Reading the image -- input it to pytesseract --obtain text and dictionary objects
im_r = cv2.imread('Cric_eg.jpg', 1)  # Cric_eg,q6

# Module for pre-processing if required
'''
# im_r=cv2.resize(img,(img.shape(img)))
# Apply Gaussean filter prior to sharpening
#im_n=cv2.GaussianBlur(im_r,(5,5),1.73)
# Apply the Sobel derivative
#derx=cv2.Sobel(im_n,-1,1,0,None,7)
'''
# Module for Affine transform if required
'''
# Affine transform(zoom)
d=np.array([im_r.shape])

# Convert the ip and op points to float
ip=np.float32([[50,100],[150,120],[180,180]])
op=np.float32([[50,100],[150,120],[180,180]])

# Obtain the M matrix
M=cv.getAffineTransform(ip,op)

#
dst=cv.warpAffine(im_r,M,((d[0:,1:2]),(d[0:,0:1])))
'''

# The user enters the word to be searched
word = raw_input("Enter the word to be searched")

# Conversion to data and sring using Tesseract
d = pytesseract.image_to_data(im_r, output_type=Output.DICT, lang='eng')
result = pytesseract.image_to_string(im_r, lang='eng')

# Convert the word to be searched to lowercase for easier comparison
wl = word.lower()
print(wl + " : is the word to be found")

# Convert the words stored as dictionary elements to lowercase in newList[] for an easier comparison and prints the list
newList = []
for m in d:
    b = d.get('text')
print(b)
for y in b:
    newList.append(y.lower())
print(newList)

# Search in the newList[] and obtain the index(-ices) if the word is found
indices = [i for i, x in enumerate(newList) if x == wl]
if len(indices)==0:
    print("Sorry- string not found")
else:
    print ("String found ")

# Count of the number of occurences of the word found
def count(word, array):
    n = 0
    for x in array:
        if x == word:
            n += 1
    return n

# Print total no fo occurences
print('The total count of the word to be searched i.e.'+word+' is '+str(count(wl, newList)))

# Create the bounding box for the required word that was to be identified - boxes generated incrementally
for q in d:
    for p in indices:
        (x, y, w, h) = (d['left'][p], d['top'][p], d['width'][p], d['height'][p])
        print(x,y,w,h)
        cv2.rectangle(im_r, (x-1, y-1), (x + w + 2, y + h + 2), (0, 0, 255), 3)
        cv2.imshow('img', im_r)
        cv2.waitKey(0)
        time.sleep(1)
    break

