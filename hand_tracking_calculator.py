import cv2
import mediapipe as mp
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)
text = ""
k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Added one more slot for new gesture
idset = ["", "1", "12", "123", "1234", "01234", "0", "01", "012", "0123", "04", "4", "34", "014", "14", "234", "thumbsup"]
op = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "eval", "thumbsup"]

while True:
    success, img = cam.read()
    if not success:
        break

    imgg = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(imgg, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            x = []
            y = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = imgg.shape
                x.append(int((lm.x) * w))
                y.append(int((1 - lm.y) * h))
            
            if len(y) > 20:
                id = ""
                big = [x[3], y[8], y[12], y[16], y[20]]
                small = [x[4], y[6], y[10], y[14], y[18]]

                for i in range(len(big)):
                    if big[i] > small[i]:
                        id += str(i)
                
                # Detect "thumbs up" gesture
                if (y[4] < y[3]) and all(y[6] > y[5] for i in range(6, 21, 4)):
                    id = "thumbsup"
                
                if id in idset:
                    k[idset.index(id)] += 1

                for i in range(len(k)):
                    if k[i] > 20:
                        if id == "thumbsup":
                            text += "Thumbs Up "
                        elif i == 15:
                            try:
                                ans = str(eval(text))
                                text = "=" + ans
                            except:
                                text = "Error"
                        else:
                            text += op[i]
                        k = [0] * len(k)

            cv2.putText(imgg, text, (60, 80), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 5)
            mpDraw.draw_landmarks(imgg, handLms, mpHands.HAND_CONNECTIONS)
    else:
        text = ""

    cv2.imshow("WebCam", imgg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
