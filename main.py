import cv2
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
#initializing video and cascader settings

def window():
        app = QApplication([])
        window = QWidget()
        window.setWindowTitle('Censor')

        layout = QVBoxLayout()
        in_combo = QComboBox()
        target_combo = QComboBox()

        layout.addWidget(in_combo)
        layout.addWidget(target_combo)
        btn = QPushButton("Censor Webcam?")

        layout.addWidget(btn)

        window.setLayout(layout)
        window.show()
        app.exec()
def output(vid):
    video = cv2.VideoCapture(vid)
    success, frame = video.read()
    width = frame.shape[0]
    height = frame.shape[1]
    font = cv2.FONT_ITALIC
    face_cascade = cv2.CascadeClassifier("faces.xml")
    output = cv2.VideoWriter('output2.mkv', cv2.VideoWriter_fourcc(*'DIVX'), 30,(height, width))

    ##detecting faces and adding text
    while success:
        faces = face_cascade.detectMultiScale(frame, 1.1, 4)
        for (x, y, w, h,) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (21, 91, 192), -1)
        cv2.imshow("progress", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        output.write(frame)
        success,frame= video.read()
        print(faces)
    output.release()

def btnclick():
    output("flash.mp4")
if __name__ == '__main__':
    window()