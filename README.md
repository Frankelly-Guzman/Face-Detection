# Face Detection with OpenCV

This is a simple Python script that uses OpenCV to perform real-time face detection through your computer's webcam. It captures video frames, detects faces in the frames, and draws rectangles around the detected faces.

## Prerequisites

Before you run the script, you'll need to install the required Python library:

```bash
pip install opencv-python
```

How to Use
1. Clone the repository:
```bash
git clone https://github.com/Frankelly-Guzman/Face-Detection.git
cd Face-Detection
```

2. Run the face detection script:
```bash
python face_detection.py
```

This will open your computer's webcam and start detecting faces in real-time. To exit the program, press the 'q' key.

Customization
You can customize the face detection parameters by modifying the script. For example, you can adjust the scaleFactor, minNeighbors, and minSize values to fine-tune the face detection accuracy and performance.

# Example of modifying face detection parameters
```python
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,        # Adjust this value
    minNeighbors=5,         # Adjust this value
    minSize=(30, 30),       # Adjust this value
    flags=cv2.CASCADE_SCALE_IMAGE
)
```

## Credits
This project uses the OpenCV library for face detection.

Author
This Face Detection project was created by Frankelly Guzman.

If you have any questions or feedback, please feel free to [contact me](mailto:frankellyrguzman@gmail.com).

Enjoy experimenting with Face Detection using OpenCV!
