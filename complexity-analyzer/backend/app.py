from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
import os
import json
import re

# ---------------- APP ----------------
app = Flask(__name__)
CORS(app)

# ---------------- GEMINI ----------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.5-flash"

# ---------------- STATIC FALLBACK ANALYZER ----------------
def static_analyze(code: str):
    # Count loops
    loops = re.findall(r'\b(for|while|do)\b', code)
    loop_count = len(loops)

    # Detect recursion (simple heuristic)
    recursion = False
    func_match = re.search(r'\b(\w+)\s*\([^)]*\)\s*{', code)
    if func_match:
        func_name = func_match.group(1)
        if len(re.findall(r'\b' + re.escape(func_name) + r'\s*\(', code)) > 1:
            recursion = True

    # Decide time complexity
    if recursion:
        time = "O(2^n)"
        reasoning = ["Recursive function detected"]
    elif loop_count == 0:
        time = "O(1)"
        reasoning = ["No loops detected"]
    elif loop_count == 1:
        time = "O(n)"
        reasoning = ["Single loop detected"]
    else:
        time = "O(n^2)"
        reasoning = ["Multiple loops detected (possible nesting)"]

    # Space complexity
    space = "O(n)" if recursion else "O(1)"

    return {
        "time_complexity": time,
        "space_complexity": space,
        "reasoning": reasoning,
        "suggestions": ["Consider optimizing loops if possible"]
    }

# ---------------- SYSTEM PROMPT ----------------
SYSTEM_PROMPT = """
You are a computer science professor.

Analyze the code and return ONLY valid JSON.
Rules:
- IF / ELSE are NOT loops
- Sequential loops are NOT nested
- One loop → O(n)
- Nested loops → O(n^2)
- Iterative Fibonacci → O(n) time, O(1) space
- Recursion increases space complexity

Return JSON ONLY:
{
  "time_complexity": "O(n)",
  "space_complexity": "O(1)",
  "reasoning": ["..."],
  "suggestions": ["..."]
}
"""

# ---------------- ROUTE ----------------
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    code = data.get("code", "")
    language = data.get("language", "Unknown")

    prompt = f"""
Language: {language}

Code:
{code}
"""

    # 1️⃣ Try Gemini
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=[SYSTEM_PROMPT, prompt],
            config={
                "temperature": 0,
                "response_mime_type": "application/json",
                "max_output_tokens": 512
            }
        )

        result = json.loads(response.text)

        return jsonify({
            "time_complexity": result["time_complexity"],
            "space_complexity": result["space_complexity"],
            "reasoning": result["reasoning"],
            "suggestions": result["suggestions"],
            "ai_explanation": "Generated using Gemini Flash 2.5"
        })

    # 2️⃣ Fallback if Gemini fails (quota / error)
    except Exception as e:
        fallback = static_analyze(code)

        return jsonify({
            "time_complexity": fallback["time_complexity"],
            "space_complexity": fallback["space_complexity"],
            "reasoning": fallback["reasoning"],
            "suggestions": fallback["suggestions"],
            "ai_explanation": "Gemini unavailable. Static analysis used."
        })

# ---------------- RUN ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

