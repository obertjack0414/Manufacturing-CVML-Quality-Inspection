import os
import time
import cv2
from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from inference_sdk import InferenceHTTPClient
import subprocess

# Configuration
app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = "static/captured_images"
ANNOTATED_FOLDER = "static/annotated_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ANNOTATED_FOLDER, exist_ok=True)

API_URL = "https://detect.roboflow.com"
API_KEY = "Your_API_Key"
MODEL_ID = "Your_Model_ID"

CLIENT = InferenceHTTPClient(api_url=API_URL, api_key=API_KEY)

# Capture an image using the Pi camera
def capture_image():
    try:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        image_path = os.path.join(UPLOAD_FOLDER, f"image_{timestamp}.jpg")

        # Run the libcamera-still command
        command = [
            "libcamera-still",
            "-o", image_path,
            "--width", "3280",
            "--height", "2464",
            "--quality", "95",
            "--timeout", "1000"
        ]
        subprocess.run(command, check=True)
        return image_path
    except Exception as e:
        print(f"Error capturing image: {e}")
        return None

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/capture-and-infer", methods=["POST"])
def capture_and_infer():
    try:
        # Capture image
        image_path = capture_image()
        if not image_path:
            return jsonify({"error": "Image capture failed"}), 500

        # Run inference with Roboflow
        result = CLIENT.infer(image_path, model_id=MODEL_ID)
        predictions = result.get("predictions", [])
        if not predictions:
            return jsonify({"error": "No predictions returned"}), 400

        # Annotate the image with predictions
        annotated_image_path = os.path.join(ANNOTATED_FOLDER, os.path.basename(image_path))
        image = cv2.imread(image_path)
        for pred in predictions:
            x, y, w, h = pred["x"], pred["y"], pred["width"], pred["height"]
            confidence = pred["confidence"]
            label = pred["class"]

            # Calculate bounding box corners
            top_left = (int(x - w / 2), int(y - h / 2))
            bottom_right = (int(x + w / 2), int(y + h / 2))

            # Draw the box and label
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(image, f"{label} ({confidence:.2f})", (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save annotated image
        cv2.imwrite(annotated_image_path, image)

        # Return URL for the annotated image
        return jsonify({"annotated_image_url": f"/{annotated_image_path}"})
    except Exception as e:
        print(f"Error during capture and inference: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/static/<path:filename>")
def serve_static_file(filename):
    return send_from_directory("static", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
