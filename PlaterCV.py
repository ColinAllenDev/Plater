import cv2 as cv
import pytesseract as tesseract
from PIL import Image

# Capture webcam video output
video_capture = cv.VideoCapture(0)

paused = False

while True:
    if not paused:
        # Read webcam data frame-by-frame
        ret, frame = video_capture.read()
        cv.imshow('Webcam', frame)

        # Convert frame to grayscale for better OCR results
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Extract text from plate
        #text_string = tesseract.image_to_string(Image.fromarray(gray_frame))

        # Extract data from plate image
        boxes = tesseract.image_to_boxes(Image.fromarray(gray_frame))

        for b in boxes.splitlines():
            b = b.split()
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

            if 100 < x < 500 and 100 < y < 500:
                word = b[0]
                cv.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
                cv.putText(frame, word, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    
        cv.imshow('Isolated Words', frame)

        key = cv.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('p'):
            paused = not paused

video_capture.release()
cv.destroyAllWindows()