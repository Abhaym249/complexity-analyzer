import re

def analyze_complexity(code: str):
    """
    Heuristic static analysis.
    Returns time, space, reasoning
    """

    loops = len(re.findall(r'\bfor\b|\bwhile\b', code))
    recursion = len(re.findall(r'\bdef\b|\bfunction\b', code)) - 1

    # ---- TIME COMPLEXITY ----
    if loops == 0 and recursion <= 0:
        time = "O(1)"
    elif loops == 1:
        time = "O(n)"
    elif loops == 2:
        time = "O(n²)"
    elif loops >= 3:
        time = "O(n³)"
    else:
        time = "O(n)"

    if recursion > 1:
        time = "O(2ⁿ)"

    # ---- SPACE COMPLEXITY ----
    space = "O(1)"
    if re.search(r'\[.*\]|\bvector\b|\blist\b|\barray\b|\bmap\b', code):
        space = "O(n)"

    # ---- REASONING ----
    reasoning = []
    if loops:
        reasoning.append(f"{loops} loop(s) detected")
    if recursion > 0:
        reasoning.append("Recursive calls detected")
    if space == "O(n)":
        reasoning.append("Auxiliary data structure used")

    if not reasoning:
        reasoning.append("Only constant-time operations detected")

    return time, space, reasoning
