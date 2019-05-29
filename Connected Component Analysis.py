import numpy as np
def liantong(img):
    label=1
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
                if min(list4)!=0:
                    img1[i][j]=min(list4)
                    equallist.append(list4)
                if max(list4)!=0 and min(list4)==0:
                    img1[i][j]=max(list4)
    for i, j in enumerate(equallist):
        equallist[i] = set(j)
    a=set()
    for i in equallist:
        a.add(min(i))
    for i in a:
        for j in equallist:
            if i in j:
                value=max(j)
                mask1=(img1==value)
                mask2=1-mask1
                img1=img1*mask2+mask1*i

    return img1[1:row+1,1:col+1]





