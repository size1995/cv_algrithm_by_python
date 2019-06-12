import numpy as np
def conv_single(img_single,kernel):
    r=1
    img_blur=np.zeros(shape=(img_single.shape[0]+2*r,img_single.shape[1]+2*r))
    x1,x2=img_single.shape
    img_pad=np.zeros(shape=(img_single.shape[0]+2*r,img_single.shape[1]+2*r))
    img_pad[r:x1+r,r:x2+r]=img_single
    for i in range(r,x1+r):
        for j in range(r,x2+r):
            tempt=img_pad[i-r:i-r+3,j-r:j-r+3]
            tempt=tempt.astype('float32')
            kernel=kernel.astype('float32')
            img_blur[i][j]=np.sum(tempt*kernel)
    return img_blur[r:x1+r,r:x2+r]
def sobel(img):
    Gx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    Gy=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    G1=conv_single(img,Gx)
    G2=conv_single(img,Gy)
    G1 = (G1 - G1.min()) / (G1.max() - G1.min())
    G2 = (G2 - G2.min()) / (G2.max() - G2.min())
    return G1,G2