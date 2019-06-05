import numpy as np
def otsu(img):
    g_max = 0
    best_th = 0
    m,n=img.shape
    area=m*n
    for th in range(0, 256, 1):
        bin_img = (img > th)
        bin_img_inv = (img <= th)
        fore_pix = np.sum(bin_img)
        back_pix = np.sum(bin_img_inv)
        if fore_pix == 0:
            break
        if back_pix == 0:
            continue
        W0 = np.sum((img > th)) / area
        u0 = np.sum(img * (img > th) ) / np.sum((img > th) )
        W1 = np.sum((img <= th) ) / area
        u1 = np.sum(img * (img <= th) ) / np.sum((img <= th))
        g = W0 * W1 * ((u0 - u1) ** 2)
        if g > g_max:
            g_max = g
            best_th = th
    im_result = (img > best_th)
    return im_result
if __name__ == '__main__':
    import cv2
    img=cv2.imread('Lenna.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    import matplotlib.pyplot as plt
    thr=otsu(img)
    save=(thr*255).astype('uint8')
    cv2.imwrite('otsu.jpg',save)