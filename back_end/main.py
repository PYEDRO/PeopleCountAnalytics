from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from moviepy.editor import VideoFileClip
import cv2
import uuid
import numpy as np
import os
import json
import requests

app = Flask(__name__)
CORS(app)

# Configurações YOLO
MODEL_PATH = 'yolov3.weights'
CONFIG_PATH = 'yolov3.cfg'
NAMES_PATH = 'coco.names'

def download_coco_names(names_path):
    url = "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
    if not os.path.exists(names_path):
        print("Baixando coco.names...")
        response = requests.get(url)
        with open(names_path, 'wb') as f:
            f.write(response.content)
        print("coco.names baixado.")

download_coco_names(NAMES_PATH)
classes = open(NAMES_PATH).read().strip().split('\n')

# Carregar YOLO
net = cv2.dnn.readNet(MODEL_PATH, CONFIG_PATH)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def process_video(video_path, polygon):
    cap = cv2.VideoCapture(video_path)
    output_filename = f"{uuid.uuid4()}.mp4"
    output_dir = 'output_videos'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, output_filename)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        height, width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)
        
        class_ids, confidences, boxes = [], [], []
        for out_detection in outs:
            for detection in out_detection:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and class_id == 0:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        pts = np.array(polygon, np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 0, 0), 3) 

        count = 0
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                center = (x + w // 2, y + h // 2)
                if cv2.pointPolygonTest(pts, center, False) >= 0:
                    count += 1
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

        
        cv2.putText(frame, f'Pessoas: {count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        out.write(frame)
    
    cap.release()
    out.release()

    # Comprimir o vídeo
    compressed_filename = f"compressed_{output_filename}"
    compressed_output_path = os.path.join(output_dir, compressed_filename)
    compress_video(output_path, compressed_output_path)
    
    if os.path.exists(compressed_output_path):
        print("Vídeo comprimido gerado com sucesso.")
        return compressed_filename
    else:
        raise FileNotFoundError("Erro ao gerar o vídeo comprimido")

def compress_video(input_path, output_path, bitrate="500k"):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, bitrate=bitrate, codec="libx264")

@app.route('/analyze', methods=['POST'])
def analyze():
    video = request.files['video']
    polygon = json.loads(request.form['polygon'])
    video_path = 'input.mp4'
    video.save(video_path)
    output_filename = process_video(video_path, polygon)
    return json.dumps({'video_filename': output_filename}), 200, {'Content-Type': 'application/json'}

@app.route('/videos/<filename>', methods=['GET'])
def get_video(filename):
    video_path = os.path.join('output_videos', filename)
    if os.path.exists(video_path):
        response = send_file(video_path, mimetype='video/mp4')
        response.headers['Cache-Control'] = 'no-store'
        return response
    else:
        return jsonify({"error": "Video not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
