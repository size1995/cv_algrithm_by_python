import numpy as np
def gaussian_2d_kernel(kernel_size=3, sigma=0):
    if kernel_size%2==0:
        raise ('核大小必须为奇数')
    kernel = np.zeros([kernel_size, kernel_size])
    center = kernel_size // 2
    if sigma == 0:
        sigma = ((kernel_size - 1) * 0.5 - 1) * 0.3 + 0.8
    s = 2 * (sigma ** 2)
    sum_val = 0
    for i in range(0, kernel_size):
        for j in range(0, kernel_size):
            kernel[i, j]=np.exp(-((i - center) * (i - center) + (j - center) * (j - center)) / s)
            sum_val += kernel[i, j]
    sum_val = 1 / (sum_val+1e-10)
    return kernel * sum_val
def Gaussion_blur_single(img_single,kernel_size=5, sigma=0):
    kernel=gaussian_2d_kernel(kernel_size, sigma)
    r=kernel_size//2
    img_blur=np.zeros(shape=(img_single.shape[0]+2*r,img_single.shape[1]+2*r))
    x1,x2=img_single.shape
    img_pad=np.zeros(shape=(img_single.shape[0]+2*r,img_single.shape[1]+2*r))
    img_pad[r:x1+r,r:x2+r]=img_single

    for i in range(r,x1+r):
        for j in range(r,x2+r):
            tempt=img_pad[i-r:i-r+kernel_size,j-r:j-r+kernel_size]
            tempt=tempt.astype('float32')
            kernel=kernel.astype('float32')
            img_blur[i][j]=np.sum(tempt*kernel)
    return img_blur[r:x1+r,r:x2+r]
def Gaussion_blur(img,kernel_size=3, sigma=0):
    x1,x2,x3=img.shape
    img=img.transpose((2,0,1))
    r,g,b=img
    r = Gaussion_blur_single(r,kernel_size, sigma).reshape((1,x1,x2))
    g = Gaussion_blur_single(g,kernel_size, sigma).reshape((1,x1,x2))
    b = Gaussion_blur_single(b,kernel_size, sigma).reshape((1,x1,x2))
    return np.concatenate((r,g,b)).transpose((1,2,0)).astype('uint8')
if __name__ == '__main__':
    import cv2
    img = cv2.imread('aa.jpg')
    img_blur = Gaussion_blur(img, kernel_size=25, sigma=0)
    cv2.imwrite('a.jpg',img_blur)








