def generate_suggestions(time, space):
    tips = []

    if time in ["O(n²)", "O(n³)"]:
        tips.append("Reduce nested loops using hashing or prefix sums")

    if time == "O(2ⁿ)":
        tips.append("Apply memoization or convert recursion to DP")

    if space == "O(n)":
        tips.append("Consider in-place operations to reduce memory usage")

    if not tips:
        tips.append("Implementation is reasonably optimized")

    return tips
