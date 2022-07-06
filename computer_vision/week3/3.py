from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
# open the test image
# Note: If you didn't launch Python from the same directory where you saved
#       the file, chipmunk.png, you'll need to provide the full path name as
#       the argument to Image.open
#im = Image.open('0a_einstein.bmp')

# display relevant Image class attributes: dimensions (width, height),
# pixel format and file format
#print (im.size, im.mode, im.format)

def boxfilter(n):
    # only odd numbers could be accepted
    assert n % 2 == 1, "Dimension must be odd"
    # make n x n array
    arr = np.zeros((n, n))
    # decide each element
    ele = 1 / (n * n)
    # substititue zero to element
    arr = np.where(arr == 0, ele, arr)
    # print array
    np.set_printoptions(linewidth=np.inf)
    print_arr = "array({0})".format(arr)
    print(print_arr)
    print("\n")

# prob1 
boxfilter(3)
#boxfilter(4)
boxfilter(7)
print("\n\n")

def gauss1d(sigma):
    # decide size of array by definition
    size = math.ceil(sigma * 6)
    if (size % 2 == 0):
        size = size + 1
    # make gaussian kernel with density function
    x = np.linspace(-1 * int(size / 2), int(size / 2), size)
    y = np.exp(-1 * (x ** 2) / (2 * (sigma ** 2)))
    print(x)
    # normalize y 
    y = y / sum(y)
    return y
    print("array({})".format(y))
    print("\n")

# problem 2
gauss1d(0.3)
gauss1d(0.5)
gauss1d(1)
gauss1d(2)
print("\n\n")

def gauss2d(sigma):
    #make gauss2d with gauss1d outer 
    ans = np.outer(gauss1d(sigma), gauss1d(sigma))
    print("\n\n")
    print(ans)
    print("\n")
    return ans

#problem 3
gauss2d(0.5)

# 4 - a
def convolve2d(array,filter):
    # padding 0 to array , add row 1 and add column 1
    x = np.pad(array, (1, 1), mode='constant', constant_values=0)
    # calculate the size of x
    mx,my=np.shape(x)
    # calculate the size of filter
    fx,fy=np.shape(filter)

    # make a array
    o=[]
    
    # convolution 
    for i in range(0,mx-fx+1):
        for j in range(0,my-fy+1):
            # slice the x and convolve with filter and each component is the sum of calculation
            o.append((x[i:i+fx,j:j+fy]*filter).sum())
    # calculate the size of output
    ow=int(mx-fx)+1
    oh=int(my-fy)+1
    # resize the output
    o=np.array(o).reshape(ow,oh)
    return o

# input of data
data = np.array([[1,0,0,0,1], [2,3,0,8,0], [2,0,0,0,3], [0,0,0,1,0]])

print(convolve2d(data,gauss2d(0.5)))


# 4 - b
def gaussconvolve2d(array, sigma):
    # make filter with sigma and gauss2d function
    f = gauss2d(sigma)
    # make answer with array and filter and convolve2d function
    ans = convolve2d(array, f)
    return ans
 
print(gaussconvolve2d(data, 0.5))

# 4 - c
# open the dog image
im = Image.open('2b_dog.bmp')
# convert the image to a black and white "luminance" greyscale image
im = im.convert('L')
# display the image
im.show()
# convert the image to a numpy array (for subsequent processing)
im = np.asarray(im)
# change im array into double array
im = im.astype('double')
# convert with gaussconvolve2d function
im = gaussconvolve2d(im, 3)
# change im array into original data type unsigned int 
im = im.astype('uint8')
# change im array into Image to use show method
pil_image=Image.fromarray(im)
pil_image.show()



