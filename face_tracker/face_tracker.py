import cv2

def detect_faces_webcam():
    # Load the pre-trained face detection model (Haar Cascade classifier)
    # You might need to provide the full path to this XML file
    # It's usually found in opencv_install_dir/data/haarcascades/
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if face_cascade.empty():
        print("Error: Could not load face cascade classifier. Make sure the XML file path is correct.")
        return

    cap = cv2.VideoCapture(0)  # 0 is typically the default webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Webcam feed started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("--- Simple Face Tracker (requires opencv-python: pip install opencv-python) ---")
    print("This script detects faces in a live webcam feed using OpenCV.")
    detect_faces_webcam()
