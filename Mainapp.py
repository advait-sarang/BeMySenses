from flask import Flask, render_template, Response, request, jsonify
import cv2
import pickle
import mediapipe as mp
import numpy as np
from translate import Translator
import pyttsx3

app = Flask(__name__)

# Load the pre-trained model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

# MediaPipe and OpenCV setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.5)

labels_dict = {i: chr(65 + i) for i in range(26)}  # A-Z character dictionary

# Route for rendering the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle real-time video feed and recognition
def gen_frames():
    cap = cv2.VideoCapture(0)  # Open webcam
    while True:
        success, frame = cap.read()  # Capture frame-by-frame
        if not success:
            break
        else:
            # Convert BGR to RGB for MediaPipe
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw hand landmarks on the frame
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()
                    )

                    # Prepare data for prediction
                    data_aux = []
                    x_ = []
                    y_ = []

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                    # Predict the character
                    prediction = model.predict([np.asarray(data_aux)])
                    predicted_character = labels_dict[int(prediction[0])]

                    # Display predicted character on the video frame
                    cv2.putText(frame, predicted_character, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for translating and speaking text
@app.route('/translate_and_speak', methods=['POST'])
def translate_and_speak():
    data = request.get_json()
    user_input = data['text']

    # Translate text
    translator = Translator(to_lang="hi")  # Use "hi" for Hindi
    translated_text = translator.translate(user_input)

    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.say(translated_text)
    engine.runAndWait()

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
