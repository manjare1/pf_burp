import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import librosa

# Load YAMNet model from TensorFlow Hub
MODEL_URL = "https://tfhub.dev/google/yamnet/1"
yamnet_model = hub.load(MODEL_URL)

# Load the YAMNet class map (labels)
class_map_path = tf.keras.utils.get_file(
    'yamnet_class_map.csv',
    'https://raw.githubusercontent.com/tensorflow/models/master/research/audioset/yamnet/yamnet_class_map.csv'
)
class_map = np.loadtxt(class_map_path, delimiter=",", dtype="str", skiprows=1, usecols=(0, 1, 2))


# Function to process MP3 file
def preprocess_audio_from_mp3(file_path):
    """Load and process MP3 file."""
    audio, sample_rate = librosa.load(file_path, sr=16000, mono=True)  # Convert to mono, 16 kHz
    return audio, sample_rate


# Audio classification function
def classify_audio(audio):
    """Classify audio using YAMNet model."""
    scores, embeddings, spectrogram = yamnet_model(audio)
    top_class_index = tf.argmax(scores, axis=1).numpy()[0]
    class_name = class_map[top_class_index][2]  # Class name
    return class_name


# Main function
def test_burp_detect(mp3_file_path):
    # Preprocess MP3 file
    audio, sample_rate = preprocess_audio_from_mp3(mp3_file_path)

    # Classify audio
    detected_class = classify_audio(audio)

    # Check for "Burp" class
    if "Burp" in detected_class:
        print("Burp sound detected!")
        return True
    else:
        print(f"Detected: {detected_class}")