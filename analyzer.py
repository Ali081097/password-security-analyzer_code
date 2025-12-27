from password_utils import password_strength, suggest_password
from breach_check import check_breach

def main():
    password = input("Enter a password to analyze: ")

    strength = password_strength(password)
    breached = check_breach(password)

    print("\nPassword Analysis")
    print("-----------------")
    print(f"Strength Level : {strength['level']}")
    print(f"Security Score : {strength['score']}/5")

    if breached:
        print("⚠️ Warning: This password has appeared in data breaches!")
    else:
        print("✅ No breach records found.")

    print("\nSuggestion:")
    print(suggest_password())


if __name__ == "__main__":
    main()
