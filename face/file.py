import cv2

cap=cv2.VideoCapture(0)
face_cd=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

while True:
      re,frm=cap.read()
      if not re:              
            print("Not opend")
            break
      gry=cv2.cvtColor(frm,cv2.COLOR_BGR2GRAY)
      
      face=face_cd.detectMultiScale(gry,1.3,5)
      
      for (x,y,w,h) in face:
            cv2.rectangle(frm,(x,y),(x+w,y+h),(0,255,0),2)
            
            cv2.imshow("siva",frm)
            key= cv2.waitKey(1)& 0xFF
            if key == ord("q"):
                break
            
                  
          
cap.release()
cv2.destroyAllWindows()








