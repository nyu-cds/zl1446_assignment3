from numba import cuda
import numpy as np
from pylab import imshow, show

@cuda.jit(device=True)
def mandel(x, y, max_iters):
    '''
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the
    Mandelbrot set given a fixed number of iterations.
    '''
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iters

@cuda.jit
def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
    '''
    Calulating the mandel value for each element in the image array using CUDA function.
    The real and imag variables contain a value for each element of the complex space defined
    by the X and Y boundaries (min_x, max_x) and (min_y, max_y).
    '''
    height = image.shape[0]
    width  = image.shape[1]

    row, col = cuda.grid(2)
    x_range = cuda.blockDim.x * cuda.gridDim.x
    y_range = cuda.blockDim.y * cuda.gridDim.y
    x_list = range( (width - 1)/(x_range+1) )
    y_list = range( (height - 1)/(y_range+1) )
    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for xi in x_list:
        x_increase = x_range*xi
        x_now = row + x_increase
        real = min_x + x_now * pixel_size_x
        if x_now >= width:
            continue
        for yi in y_list:
            y_increase = y_range*yi
            y_now = col + y_increase
            imag = min_y + y_now * pixel_size_y
            if y_now >= height:
                continue
            image[y_now, x_now] = mandel(real, imag, iters)

if __name__ == '__main__':

    image = np.zeros((1024, 1536), dtype = np.uint8)
    blockdim = (32, 8)
    griddim = (32, 16)
    image_global_mem = cuda.to_device(image)
    compute_mandel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, image_global_mem, 20)
    image_global_mem.copy_to_host()
    imshow(image)
    show()