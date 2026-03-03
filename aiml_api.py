from openai import OpenAI

def get_aiml_response(prompt):
    try:
        client = OpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta",
            api_key="AIzaSyBRWdcgbFbMRaXkN_r38U8GwjntD73ptuY"  # Replace with your actual API key
        )

        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[
                {"role": "system", "content": "You are a helpful virtual assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
            
    except Exception as e:
        print("AIML API Error:", str(e))
        return "I apologize, but I'm having trouble connecting to my knowledge base right now."