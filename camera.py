import cv2 

class Camera:

    def __init__(self, camera_id):
        self.camera_id = camera_id
        self.camera = cv2.VideoCapture(self.camera_id)
        if not self.camera.isOpened():
            raise Exception("Camera not found!")

        self.width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()
    
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None
        else:
            return None