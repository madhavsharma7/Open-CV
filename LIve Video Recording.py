import cv2
def main():
    windowname="live Video Feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)

    filename='output.avi'
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=30
    resolution=(640,480)

    videofileoutput=cv2.VideoWriter(filename,codec,framerate,resolution)
    if(cap.isOpened()):
        ret,frame=cap.read()
    else:
        ret=False
    while(ret):
        ret,frame=cap.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        videofileoutput.write(frame)
        cv2.imshow(windowname,frame)
        if cv2.waitKey(1)==27:
            break
    cv2.destroyWindow(windowname)

    cap.release()

main()
