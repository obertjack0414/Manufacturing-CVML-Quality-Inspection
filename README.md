# Manufacturing-CVML-Quality-Inspection
This repository is all of the code that I used to create and deploy my mock MES CVML quality inspection.

## Overview

This repository contains the implementation of a Computer Vision (CV) and Machine Learning (ML) system for automated quality inspection in manufacturing. The project integrates Raspberry Pi hardware, Roboflow inference, Flask, and a custom web application to simulate a just-in-time quality check system. This solution is designed to enhance manufacturing processes by providing real-time defect detection, reducing human error, and enabling scalability for Industry 4.0 applications.

---

## Features

- **Raspberry Pi Integration:** Captures images for real-time inspection using a connected camera.
- **Roboflow Inference:** Processes images using trained ML models for defect detection and classification.
- **Flask Backend:** Handles API requests for image capture, inference processing, and result delivery.
- **Custom Web Application:** Displays annotated images with detected defects and provides an intuitive interface for user interaction.
- **Scalability:** Designed to adapt to various manufacturing lines and integrate into larger MES environments.

---

## Getting Started

### Prerequisites

- **Hardware:** Raspberry Pi (with a connected camera module)
- **Software:**
  - Python 3.11+
  - Flask
  - Roboflow Inference SDK
  - Additional dependencies listed in `requirements.txt`

---

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/just-in-time-quality-check.git
   cd just-in-time-quality-check
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Roboflow API key:
     ```
     ROBOFLOW_API_KEY=your_api_key
     ```

4. **Run the Flask server:**
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

5. **Access the web application:**
   - Open your browser and navigate to: `http://<pi-ip-address>:5000`

---

## Folder Structure

```
.
├── static
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── app.js
│   ├── images
│       └── placeholder.jpg
├── templates
│   └── index.html
├── annotated_images
├── captured_images
├── app.py
├── requirements.txt
├── README.md
```

---

## Usage

1. Press the **"Capture and Infer"** button in the web app to trigger image capture.
2. The Raspberry Pi captures an image and sends it to the Flask server.
3. The Flask server forwards the image to Roboflow for inference.
4. The results (bounding boxes and classifications) are drawn on the image.
5. The annotated image is displayed on the web app.

---

## Future Enhancements

- **Improved UI:** Enhance the web app for better usability and aesthetics.
- **Predictive Maintenance:** Integrate analytics for proactive quality control.
- **Cloud Integration:** Extend the system to work seamlessly with cloud-based platforms.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---
