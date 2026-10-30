"""
Day 24 - 2026-10-30
Tool: Password Strength Checker
What it does: Scores a password by length and by whether it mixes
lowercase, uppercase, digits and symbols, then labels it Weak,
Medium or Strong with tips on what is missing.
Who it helps: Anyone setting a new account password who wants a
quick, honest check before using it everywhere.
(Different from Day 2, which GENERATED a password - this one
checks a password you already chose.)
"""
import string


def password_score(password):
    score = 0
    tips = []
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")
    if len(password) >= 12:
        score += 1
    if any(c in string.ascii_lowercase for c in password):
        score += 1
    else:
        tips.append("Add a lowercase letter.")
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    else:
        tips.append("Add an uppercase letter.")
    if any(c in string.digits for c in password):
        score += 1
    else:
        tips.append("Add a digit.")
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Add a symbol like ! or #.")
    return score, tips


def strength_label(password):
    score, tips = password_score(password)
    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"
    return label, tips


if __name__ == "__main__":
    for pw in ["hello", "Hello123", "Hello@123bd"]:
        label, tips = strength_label(pw)
        print(pw, "->", label, "| tips:", tips if tips else "none")
