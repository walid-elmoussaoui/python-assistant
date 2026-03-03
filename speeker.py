import speech_recognition as sr

# pyaudio is required for microphone input but can be hard to install on Windows
# due to compiler requirements. We attempt to import it and set a flag so the
# rest of the module can degrade gracefully if it's unavailable.
try:
    import pyaudio
    _HAS_PYAUDIO = True
except ImportError:
    print("Warning: pyaudio package not found; speech-to-text will be disabled.")
    _HAS_PYAUDIO = False

def find_internal_microphone():
    """Automatically find and return the internal microphone index"""
    microphones = sr.Microphone.list_microphone_names()
    
    # Common keywords for internal microphones
    internal_keywords = [
        "internal", "built-in", "default", "macbook", "laptop", 
        "integrated", "realtek", "conexant", "idt", "via", "built in"
    ]
    
    print("Searching for internal microphone...")
    
    for index, name in enumerate(microphones):
        name_lower = name.lower()
        for keyword in internal_keywords:
            if keyword in name_lower:
                print(f"Found internal microphone: {name}")
                return index
    
    # If no specific internal mic found, use default (index 0)
    print("Using default microphone (likely internal)")
    return 0

def speech_to_text():
    """Speech to text using internal microphone only"""
    if not _HAS_PYAUDIO:
        print("Cannot perform speech-to-text: pyaudio is not installed.")
        return None

    recognizer = sr.Recognizer()
    
    # Get internal microphone
    internal_mic_index = find_internal_microphone()
    microphone = sr.Microphone(device_index=internal_mic_index)
    
    with microphone as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        
        print("Ready! Speak now...")
        
        try:
            # Listen for audio input
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            print("Processing speech...")
            
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
            
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return None
            
        except sr.UnknownValueError:
            print("Could not understand the audio. Please speak more clearly.")
            return None
            
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
            return None


def main():
    """Main function - automatically uses internal microphone"""
    print("Internal Microphone Speech-to-Text")
    print("=" * 40)
    
    print("Choose mode:")
    print("1. Single recognition")




    print("\n--- Single Recognition Mode ---")
    result = speech_to_text()
    if result:
         return result

