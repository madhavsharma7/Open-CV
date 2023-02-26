import cv2
def main():
    windowname="live video Feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)

    print('width:'+str(cap.get(3)))
    print('height:'+str(cap.get(4)))

    """cap.set(3,200)
    cap.set(4,200)
    print('width:'+str(cap.get(3)))
    print('height:'+str(cap.get(4)))"""

    if(cap.isOpened()):
        ret,frame=cap.read()
    else:
        ret=False
    while(ret):
        ret,frame=cap.read()
        #output=cv2.cvtcolor(frame,cv2.COLOR_BGR2RGB)
        #cv2.imshow('grey',output)
        cv2.imshow(windowname,frame)
        if cv2.waitKey(1)==27:
            break

    cv2.destroyWindow(windowname)

    cap.release()

main()
    
