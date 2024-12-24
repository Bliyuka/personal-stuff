import cv2
import mediapipe as mp
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox, QPushButton, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from CvFpsCalc import CvFpsCalc
from functions import *
from tensorflow.keras.models import load_model



class WebcamViewer(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam Viewer with Hand Detection")
        self.setGeometry(100, 100, 1280, 720)  # Set to 16:9 ratio with 720p resolution
        self.setFixedSize(1280, 720)  # Make the window non-resizable

        # Variables
        self.current_camera_index = 0
        self.capture = None
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils
        self.hand_detection_enabled = False

        # Setup UI
        self.init_ui()

        # Start Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(90)  # Update every 30 ms

        self.cvFpsCalc = CvFpsCalc(buffer_len=10)
        self.model = load_model('keypoint_classifier_demo_2.keras')
        self.keypoint_classifier_labels = self.get_label()
        self.last_keybind_time = time.time()

    def init_ui(self) -> None:
        # Main layout
        layout = QVBoxLayout()

        # Dropdown for camera selection
        self.camera_selector = QComboBox()
        cameras = self.list_cameras()
        self.camera_selector.addItems([f"Camera {i}" for i in cameras])
        self.camera_selector.currentIndexChanged.connect(self.switch_camera)
        layout.addWidget(self.camera_selector)

        # Toggle button for hand detection
        self.toggle_button = QPushButton("Enable Hand Detection")
        self.toggle_button.clicked.connect(self.toggle_hand_detection)
        layout.addWidget(self.toggle_button)

        # Video Display
        self.video_label = QLabel()
        self.video_label.setFixedSize(1280, 720)  # Set QLabel size to 16:9 ratio with 720p resolution
        # self.video_label.setScaledContents(True)
        layout.addWidget(self.video_label)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Initialize camera
        if cameras:
            self.switch_camera(cameras[0])

    def list_cameras(self) -> list:
        available_cameras = []
        for index in range(5):  # Check first 5 camera indices
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                available_cameras.append(index)
                cap.release()
        return available_cameras

    def switch_camera(self, index: int) -> None:
        self.current_camera_index = index
        if self.capture:
            self.capture.release()
        self.capture = cv2.VideoCapture(self.current_camera_index)

    def toggle_hand_detection(self) -> None:
        self.hand_detection_enabled = not self.hand_detection_enabled
        self.toggle_button.setText("Disable Hand Detection" if self.hand_detection_enabled else "Enable Hand Detection")

    def get_label(self) -> list:
        with open('keypoint_classifier_label_2.csv',encoding='utf-8') as file:
            keypoint_classifier_labels = csv.reader(file)
            keypoint_classifier_labels = [row[0] for row in keypoint_classifier_labels] 
        return keypoint_classifier_labels

    def update_frame(self) -> None:
        if not self.capture or not self.capture.isOpened():
            return

        ret, frame = self.capture.read()
        if not ret:
            return

        fps = self.cvFpsCalc.get()

        # Process frame
        if self.hand_detection_enabled:
            frame.flags.writeable = False
            results = self.hands.process(frame)
            frame.flags.writeable = True
            
            
            if results.multi_hand_landmarks is not None:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                    Landmark_list = calc_landmark_list(frame, hand_landmarks)

                    pre_processed_landmark_list = pre_process_landmark(Landmark_list)

                    pred = self.model.predict(np.array([pre_processed_landmark_list]), verbose=0)
                    hand_sign_id = np.argmax(pred)
                    confidence_percentage = np.ceil(pred[0][hand_sign_id] * 100)


                    # Mark as 'Unknown' if confidence is below 80%
                    if confidence_percentage < 80:
                        hand_sign_text = "Unknown"
                    else:
                        hand_sign_text = self.keypoint_classifier_labels[hand_sign_id]
                        
                    cv2.putText(frame, f'{hand_sign_id} - {confidence_percentage}', (10, 140), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

                    self.last_keybind_time = keybind(hand_sign_text, self.last_keybind_time)  # Update the keybind time


        cv2.putText(frame, "FPS:" + str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 255, 255), 3, cv2.LINE_AA)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width
        q_img = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(q_img).scaled(self.video_label.width(), self.video_label.height()))

    def closeEvent(self, event):
        if self.capture:
            self.capture.release()
        self.hands.close()
        super().closeEvent(event)
