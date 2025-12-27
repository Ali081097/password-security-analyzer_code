import string

def password_strength(password: str) -> dict:
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    return {
        "score": score,
        "level": levels.get(score, "Very Weak")
    }


def suggest_password():
    return "Use at least 12 characters with upper, lower, number & symbols."
