import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ FREE & STABLE MODEL
model = genai.GenerativeModel("gemini-1.5-flash")


def explain_complexity(code, time_complexity, space_complexity):
    """
    Uses Gemini ONLY for explanation.
    Never guesses complexity.
    Safe fallback included.
    """

    prompt = f"""
You are a senior software engineer.

Explain the following complexity analysis in simple terms.

Detected Time Complexity: {time_complexity}
Detected Space Complexity: {space_complexity}

Rules:
- Do NOT change the complexity values
- Do NOT invent new Big-O
- Keep explanation concise and clear

Code:
{code[:1200]}
"""

    try:
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text.strip()

        raise Exception("Empty Gemini response")

    except Exception as e:
        print("GEMINI ERROR:", e)

        # ✅ SAFE FALLBACK (ALWAYS RETURNS SOMETHING)
        return (
            f"The time complexity is {time_complexity} based on the detected loop structure. "
            f"The space complexity is {space_complexity} because the algorithm does not "
            f"use additional memory proportional to input size."
        )
