import cv2

def capture_webcam_feed():
    print("Opening webcam... Press 'q' to quit.")
    cap = cv2.VideoCapture(0)  # 0 is typically the default webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow('Webcam Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("--- Simple Webcam Capture (requires opencv-python: pip install opencv-python) ---")
    print("This script demonstrates capturing and displaying video from your webcam.")
    print("It does NOT implement video calling functionality.")
    capture_webcam_feed()
