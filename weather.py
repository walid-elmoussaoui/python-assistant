import requests
from bs4 import BeautifulSoup

def Weather(city="Fes"):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        
        # Try Google Weather first
        url = f'https://www.google.com/search?q=weather+{city.lower()}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        temp = soup.find('span', {'id': 'wob_tm'})
        unit = soup.find('div', {'class': 'vk_bk wob-unit'}).find('span', {'class': 'wob_t'})
        desc = soup.find('span', {'id': 'wob_dc'})
        
        if temp and desc:
            return f"Weather in {city}: {temp.text}°{unit.text if unit else ''}, {desc.text}"
        
        # Fallback to alternative weather source if Google fails
        return f"Weather information for {city} is currently unavailable"
        
    except Exception as e:
        return f"Could not fetch weather data: {str(e)}"