from PIL import Image
import math
import numpy as np

"""
Get and use the functions associated with gaussconvolve2d that you used in the last HW02.
"""
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

def gauss2d(sigma):
    #make gauss2d with gauss1d outer 
    ans = np.outer(gauss1d(sigma), gauss1d(sigma))
    print("\n\n")
    print(ans)
    print("\n")
    return ans

def convolve2d(array,filter):
    # padding 0 to array , add row 1 and add column 1
    x = np.pad(array, (1, 1), mode='constant', constant_values=0)
    # calculate the size of x
    mx,my=np.shape(x)
    # reverse updown and rightleft
    filter = np.flip(filter)
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

def gaussconvolve2d(array, sigma):
    # make filter with sigma and gauss2d function
    f = gauss2d(sigma)
    # make answer with array and filter and convolve2d function
    ans = convolve2d(array, f)
    return ans

def sobel_filters(img):
    """ Returns gradient magnitude and direction of input img.
    Args:
        img: Grayscale image. Numpy array of shape (H, W).
    Returns:
        G: Magnitude of gradient at each pixel in img.
            Numpy array of shape (H, W).
        theta: Direction of gradient at each pixel in img.
            Numpy array of shape (H, W).
    Hints:
        - Use np.hypot and np.arctan2 to calculate square root and arctan
    """    # setting x filter and y filter
    x_f = np.array([[1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    y_f = np.array([[1, 2, 1], [0, 0 ,0], [-1, 2, -1]], np.float32)

    # calculate gradient of x and y
    gradi_x = convolve2d(img, x_f)
    gradi_y = convolve2d(img, y_f)

    # calculate the gradient magnitude and theta
    G = np.hypot(gradi_x, gradi_y)
    # mapping G to 0 ~ 255
    G = G / G.max() * 255
    theta = np.arctan2(gradi_y, gradi_x)
    print('magnitude is', G)
    print('theta is', theta)
    return (G, theta)

def non_max_suppression(G, theta):
    pass

def double_thresholding(img):

    # determine high and low threshold values
    T_high = img.max() * 0.15
    T_low = img.max() * 0.03
    
    # declare array for return
    ans = np.zeros(img.shape, dtype=np.int32)

    # set the pixel value
    weak_pixel_value = 80
    string_pixel_value = 255

    # calculate strong_x, strong_y, weak_x, weak_y
    strong_x, strong_y = np.where(img > T_high)
    weak_x, weak_y = np.where((img <= T_high) & (img >= T_low))

    ans[strong_x, strong_y] = string_pixel_value
    ans[weak_x, weak_y] = weak_pixel_value

    return ans

def hysteresis(img):
    """ Find weak edges connected to strong edges and link them.
    Iterate over each pixel in strong_edges and perform depth first
    search across the connected pixels in weak_edges to link them.
    Here we consider a pixel (a, b) is connected to a pixel (c, d)
    if (a, b) is one of the eight neighboring pixels of (c, d).
    Args:
        img: numpy array of shape (H, W) representing NMS edge response.
    Returns:
        res: hysteresised image.
    """
#   pass
#  return res
"""
# 1. Noise Reduction

# open the dog image
im = Image.open('iguana.bmp')
# convert the image to a black and white "luminance" greyscale image
im = im.convert('L')
im_grey = im.convert('L')
# display the image
im.show()
# convert the image to a numpy array (for subsequent processing)
im = np.asarray(im)
# change im array into float32 array
im = im.astype('float32')
# convert with gaussconvolve2d function
im = gaussconvolve2d(im, 1.6)
# change im array into original data type unsigned int 
im = im.astype('uint8')
# change im array into Image to use show method
pil_image=Image.fromarray(im)
pil_image.show()

# 2. Finding the intensity gradient of the image
G, theta = sobel_filters(im_grey)
G_img = Image.fromarray(G.astype('uint8'))
G_img.show()
"""
def main():
    #이미지 회색
    img = Image.open('iguana.bmp')
    img_gray = img.convert('L')
   # img_gray.show()
    # convert the image to a numpy array and convert type into float32
    img_arr = np.asarray(img_gray)
    img_arr = img_arr.astype('float32')

    #1. noise reduction
    img_result = gaussconvolve2d(img_arr,1.6)
    result_arr = img_result.astype('uint8')
    result_img = Image.fromarray(result_arr)
    result_img.show()
    imgX, imgY = img.size

    # 2.sobel filter
    G, theta = sobel_filters(img_result)
    G_img = Image.fromarray(G.astype('uint8'))
#    G_img.show()

    # 3.Non-max suppression
    
    #4. Double threshold
    dt_arr = double_thresholding(img_result)
    dt_img = Image.fromarray(dt_arr)
    dt_img.show()

if __name__=="__main__":
    main()
