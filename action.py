import datetime
import speak
import webbrowser
import weather
import os
import urllib.parse
import aiml_api  # Add this import

def Action(send):
    data_btn = send.lower()

    # Add these new volume control conditions at the start
    if "volume up" in data_btn or "increase volume" in data_btn:
        current_vol = float(speak._current_volume)
        result = speak.set_volume(min(1.0, current_vol + 0.2))
        speak.speak(result)
        return result

    elif "volume down" in data_btn or "decrease volume" in data_btn:
        current_vol = float(speak._current_volume)
        result = speak.set_volume(max(0.0, current_vol - 0.2))
        speak.speak(result)
        return result

    elif "set volume" in data_btn:
        try:
            # Extract volume percentage from command (e.g., "set volume 75")
            vol = int(''.join(filter(str.isdigit, data_btn)))
            result = speak.set_volume(vol / 100)
            speak.speak(result)
            return result
        except:
            speak.speak("Please specify a volume level between 0 and 100")
            return "Please specify a volume level between 0 and 100"

    if "who are you" in data_btn:
        speak.speak("I am a program by Walid in python")  
        return "I am a program by Walid in python"

    elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn: 
        speak.speak("Hey sir, How i can help you!")  
        return "Hey sir, How i can help you!" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "play song" in data_btn:
        song_query = data_btn.replace("play music", "").replace("play song", "").strip()
        if song_query:
            # Using Spotify's play URL format
            spotify_url = f"https://open.spotify.com/search/{urllib.parse.quote(song_query)}/play"
            webbrowser.open(spotify_url)
            speak.speak(f"Playing {song_query} on Spotify")
            return f"Playing {song_query} on Spotify"
        else:
            webbrowser.open("https://open.spotify.com/")
            speak.speak("spotify.com is now ready for you, enjoy your music")
            return "spotify.com is now ready for you, enjoy your music"

    elif "youtube" in data_btn or "play video" in data_btn:
        video_query = data_btn.replace("youtube", "").replace("play video", "").strip()
        if video_query:
            try:
                from requests_html import HTMLSession
                from bs4 import BeautifulSoup
                import requests

                # Search for the video
                search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(video_query)}"
                response = requests.get(search_url)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find video ID from search results
                scripts = soup.find_all('script')
                for script in scripts:
                    if 'videoRenderer' in str(script):
                        script_text = str(script)
                        video_id = script_text.split('"videoId":"')[1].split('"')[0]
                        # Create direct video URL with autoplay
                        video_url = f"https://www.youtube.com/watch?v={video_id}&autoplay=1"
                        webbrowser.open(video_url)
                        speak.speak(f"Playing {video_query} on YouTube")
                        return f"Playing {video_query} on YouTube"
                
                # Fallback if video ID not found
                webbrowser.open(search_url)
                speak.speak(f"Searching for {video_query} on YouTube")
                return f"Searching for {video_query} on YouTube"
                
            except Exception as e:
                # Fallback to search results if direct play fails
                search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(video_query)}"
                webbrowser.open(search_url)
                speak.speak(f"Searching for {video_query} on YouTube")
                return f"Searching for {video_query} on YouTube"
        else:
            url = 'https://youtube.com/'
            webbrowser.get().open(url)
            speak.speak("YouTube open")
            return "YouTube open"

    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn:
        # Extract city name if provided
        words = data_btn.split()
        city = "Fes"  # Default city
        
        # Check if city is provided after "weather"
        if len(words) > 1 and words[0].lower() == "weather":
            city = " ".join(words[1:])
        
        ans = weather.Weather(city)
        speak.speak(ans)
        return ans

    elif 'music from my laptop' in data_btn:
        url = '' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    else:
        try:
            # Get response from AIML API
            response = aiml_api.get_aiml_response(data_btn)
            speak.speak(response)
            return response 
        except Exception as e:
            speak.speak("I'm not able to understand!")
            return "I'm not able to understand!"

