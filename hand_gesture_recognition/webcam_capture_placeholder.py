import cv2

def capture_and_display_webcam():
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

        # For demonstration, let's draw a simple rectangle on the frame
        # In a real application, this would be where hand detection/drawing happens
        cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 2)
        cv2.putText(frame, "Webcam Feed", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('Webcam Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("--- Simple Webcam Capture for Hand Gesture Recognition (Conceptual) ---")
    print("This script demonstrates basic webcam capture using OpenCV.")
    print("It does NOT perform actual hand detection or gesture recognition.")
    capture_and_display_webcam()
