import os
import google.generativeai as genai


class GeminiAssistant:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if self.api_key:
            genai.configure(api_key=self.api_key)

    def generate_summary(self, prompt: str) -> str:
        if not self.api_key:
            return "Gemini API key not configured."

        try:
            # Try a supported model. Change this if your account supports a different one.
            model = genai.GenerativeModel("gemini-flash-latest")

            response = model.generate_content(prompt)

            if response and response.text:
                return response.text

            return "No response generated."

        except Exception as e:
            print(f"[ERROR] {e}")
            return f"Gemini Error: {e}"