import os
import json
from PIL import Image, ImageTk
import cv2
import base64
from io import BytesIO

# JSON files to store video metadata and last directory
METADATA_FILE = 'video_metadata.json'
DIRECTORY_FILE = 'last_directory.json'

# Function to generate video thumbnail
def get_thumbnail(media_path, thumbnail_size=(120, 90)):
    # If it's a video, try to capture the first frame
    if media_path.endswith(('.mp4', '.avi', '.mkv', '.mov')):
        cap = cv2.VideoCapture(media_path)
        if not cap.isOpened():
            print(f"Warning: Unable to open video file: {media_path}")
            return None  # Skip if the video cannot be opened

        ret, frame = cap.read()  # Read the first frame
        if ret:
            cap.release()
            frame = cv2.resize(frame, thumbnail_size)
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            buffer = BytesIO()
            image.save(buffer, format="PNG")
            thumbnail_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            return thumbnail_data
        else:
            cap.release()
            print(f"Warning: Could not read frame from video: {media_path}")
            return None  # Skip if the frame cannot be read

    # If it's an image, load it directly
    elif media_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        try:
            image = Image.open(media_path)
            image = image.resize(thumbnail_size)
            buffer = BytesIO()
            image.save(buffer, format="PNG")
            thumbnail_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            return thumbnail_data
        except Exception as e:
            print(f"Error: Could not open/read image file: {media_path}. Error: {e}")
            return None  # Skip if the image cannot be processed

    return None  # Skip unsupported file formats


# Function to load thumbnail from base64-encoded data
def load_thumbnail(thumbnail_data):
    thumbnail_bytes = base64.b64decode(thumbnail_data)
    buffer = BytesIO(thumbnail_bytes)
    img = Image.open(buffer)
    return ImageTk.PhotoImage(img)

# Load or create metadata file
def load_metadata():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save metadata back to JSON
def save_metadata(metadata):
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=4)

# Load last used directory
def load_last_directory():
    if os.path.exists(DIRECTORY_FILE):
        with open(DIRECTORY_FILE, 'r') as f:
            last_directory = json.load(f).get('last_directory', '')
            return last_directory
    return ''

# Save last used directory
def save_last_directory(directory):
    with open(DIRECTORY_FILE, 'w') as f:
        json.dump({'last_directory': directory}, f)
