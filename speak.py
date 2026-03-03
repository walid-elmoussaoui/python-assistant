# pip install pyttsx3 keyboard

import pyttsx3
import keyboard  # Requires 'keyboard' package (pip install keyboard)

# Global variables
_engine = None
_current_volume = 1.0  # Default volume (0.0 to 1.0)
_voice_disabled = False  # Flag to track if voice is temporarily disabled

def init_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        voices = _engine.getProperty('voices')
        _engine.setProperty('voice', voices[1].id)
        _engine.setProperty('volume', _current_volume)
        
        # Adjust speech rate (higher number = faster speech)
        rate = _engine.getProperty('rate')
        _engine.setProperty('rate', rate + 0)  # Increase rate by 50 for faster speech

def set_volume(level):
    """Set volume level between 0.0 and 1.0"""
    global _current_volume
    _current_volume = max(0.0, min(1.0, level))
    if _engine is not None:  # Only set if engine exists
        _engine.setProperty('volume', _current_volume)
    return f"Volume set to {int(_current_volume * 100)}%"

def toggle_voice():
    """Toggle voice on/off with TAB key"""
    global _voice_disabled
    _voice_disabled = not _voice_disabled
    status = "disabled" if _voice_disabled else "enabled"
    print(f"Voice {status} (press TAB to toggle)")

def speak(text):
    global _engine, _voice_disabled
    
    # Register TAB key to toggle voice
    keyboard.on_press_key('tab', lambda _: toggle_voice())
    
    # If voice is disabled, don't speak
    if _voice_disabled:
        keyboard.unhook_all()
        return

    # Initialize fresh engine instance each time to ensure clean state
    if _engine is not None:
        try:
            _engine.endLoop()  # Clean up any existing loop
        except:
            pass
        _engine = None
    
    init_engine()
    
    # Set up ESC key listener to stop current speech
    keyboard.on_press_key('esc', lambda e: _engine.stop())
    
    try:
        _engine.say(text)
        _engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")
    finally:
        # Clean up key listeners
        keyboard.unhook_all()