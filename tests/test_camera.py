import cv2

def test_camera(camera_id=0):
    # Start video capture
    cap = cv2.VideoCapture(camera_id)

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # If frame is read correctly ret is True
            if not ret:
                print("Error: Can't receive frame (stream end?). Exiting ...")
                break

            # Display the resulting frame
            cv2.imshow('Camera Test', frame)

            # Press 'q' to exit the window
            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

# Test the default camera
test_camera()