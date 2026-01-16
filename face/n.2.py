import cv2
from telegram import Bot
import asyncio

sent_lim = 5
send_cou = 0


def tel():
    global send_cou
    if send_cou >= sent_lim:
        return  

    try:
        Tok = "8408024860:AAHdwYXOzQsU4ZIbbIfVg3QLMYjNUEt2Wsw"
        Id = 5671931913

        bot = Bot(token=Tok)

        async def main():
            im = "face.jpg"
            with open(im, "rb") as photo:
                await bot.send_photo(chat_id=Id, photo=photo)
             

        asyncio.run(main())
        
        send_cou += 1
        print(f"Sent photo {send_cou}/5")

    except Exception as e:
        print(e)


cap = cv2.VideoCapture(0)
face_cd = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    re, frm = cap.read()
    if not re:
        print("Not opened")
        break

    gry = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
    face = face_cd.detectMultiScale(gry, 1.1, 5)

    for (x, y, w, h) in face:
        cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if send_cou < sent_lim:
            cv2.imwrite("face.jpg", frm)
            tel()

    cv2.imshow("siva", frm)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
