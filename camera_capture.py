import cv2
def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if mirror is True:
            frame = frame[:,::-1]
            
        if size is not None and len(size) == 2:
            frame = cv2.resize(800, 600)

        return frame

cv2.imshow('camera capture', capture_camera)


