import numpy as np
import cv2
import pytesseract
from time import sleep

print('')
print('Press "q" to stop video')
print('')

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # ocr
    text = pytesseract.image_to_string(frame)
    print('='*50)
    print(text)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # fps
    sleep(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
