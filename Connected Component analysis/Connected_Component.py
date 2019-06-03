import numpy as np
def liantong(img):
    label=2
    row=img.shape[0]
    col=img.shape[1]
    img1=np.zeros(shape=(row+2,col+2))
    img1[1:row+1,1:col+1]=img
    equallist=[]
    for i in range(1,(row+1)):
        for j in range(1,(col+1)):
            if img1[i][j]==1:
                list4=[img1[i][j-1],img1[i-1][j]]
                if max(list4)==0:
                    img1[i][j]=label
                    label += 1
                elif min(list4)>1:
                    img1[i][j]=min(list4)
                    if list4[0]!=list4[1] and {list4[0],list4[1]} not in equallist:
                        equallist.append({list4[0],list4[1]})
                elif max(list4)>1 and min(list4)==0:
                    img1[i][j]=max(list4)
    l = len(equallist)
    for i, k in enumerate(equallist):
        for j in range(i + 1, l):
            if k == equallist[j]:
                continue
            elif k.isdisjoint(equallist[j]):
                continue
            else:
                k = k | equallist[j]
                equallist[j] = {0}
        equallist[i] = k

    b = []
    for i in range(len(equallist)):
        if equallist[i] != {0}:
            b.append(equallist[i])
    e_num=len(b)
    e_num_list=[i for i in range(1,e_num+1)]
    for i in range(2,int(img1.max())+1):
        i_isequal=False
        for k,j in enumerate(b):
            if i in j:
                i_isequal=True
                mask1 = (img1 == i)
                mask2 = 1 - mask1
                img1 = img1 * mask2 + mask1 * e_num_list[k]
        if not i_isequal:

            e_num+=1
            mask1 = (img1 == i)
            mask2 = 1 - mask1
            img1 = img1 * mask2 + mask1 * e_num

    return img1[1:row+1,1:col+1]

if __name__ == '__main__':
    import cv2
    img=cv2.imread('example.png')
    img=img.transpose((2,0,1))
    img1=img[0]
    _,img_b=cv2.threshold(img1,200,1, cv2.THRESH_BINARY)
    import matplotlib.pyplot as plt
    plt.imshow(liantong(img_b))






