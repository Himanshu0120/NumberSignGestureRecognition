import cv2
import os
import glob
if os.path.isdir('D:/projects/NumberSignRecogition/data')==False:
    os.mkdir('data')
    os.mkdir('data/train')
    os.mkdir('data/test')
dir=input('Enter which data do you want to collect(test/train) : ')
if os.path.isdir(r'D:\projects\NumberSignRecogition\data/'+dir)==False:
    os.mkdir('data/'+dir)

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    cv2.rectangle(frame,(50,50),(250,300),(0,255,0),1)
    cv2.imshow('Vdo',frame)
    hand=frame[50:300,50:250]
    gray=cv2.cvtColor(hand,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    cv2.imshow('Threshold',thresh)
    key=cv2.waitKey(20)
    path='data/'+dir+'/'+chr(key & 0xFF)
    if chr(key & 0xFF)=='0':
        if os.path.isdir(path)==False:
            os.mkdir(path)
        n=str(len(glob.glob(path+'/*')))
        img_path=path+'/img'+n+'.jpg'
        cv2.imwrite(img_path,thresh)
        print('image Saved')
    if chr(key & 0xFF)=='1':
        if os.path.isdir(path)==False:
            os.mkdir(path)
        n=str(len(glob.glob(path+'/*')))
        img_path=path+'/img'+n+'.jpg'
        cv2.imwrite(img_path,thresh)
        print('image Saved')
    if chr(key & 0xFF)=='2':
        if os.path.isdir(path)==False:
            os.mkdir(path)
        n=str(len(glob.glob(path+'/*')))
        img_path=path+'/img'+n+'.jpg'
        cv2.imwrite(img_path,thresh)
        print('image Saved')
    if chr(key & 0xFF)=='3':
        if os.path.isdir(path)==False:
            os.mkdir(path)
        n=str(len(glob.glob(path+'/*')))
        img_path=path+'/img'+n+'.jpg'
        cv2.imwrite(img_path,thresh)
        print('image Saved')
    if chr(key & 0xFF)=='4':
        if os.path.isdir(path)==False:
            os.mkdir(path)
        n=str(len(glob.glob(path+'/*')))
        img_path=path+'/img'+n+'.jpg'
        cv2.imwrite(img_path,thresh)
        print('image Saved')
    if chr(key & 0xFF)=='5':
        if os.path.isdir(path)==False:
            os.mkdir(path)
        n=str(len(glob.glob(path+'/*')))
        img_path=path+'/img'+n+'.jpg'
        cv2.imwrite(img_path,thresh)
        print('image Saved')
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break