import re

def check_password_strength(password):
    # Initialize feedback and strength score
    feedback = []
    strength_score = 0
    
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        strength_score += 1  # Add 1 point for length
    
    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        strength_score += 1  # Add 1 point for uppercase letter
    
    # Check for lowercase letter
    if not any(char.islower() for char in password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        strength_score += 1  # Add 1 point for lowercase letter
    
    # Check for number
    if not any(char.isdigit() for char in password):
        feedback.append("Password should contain at least one digit.")
    else:
        strength_score += 1  # Add 1 point for number
    
    # Check for special characters
    special_characters = re.compile('[@#$%^&+=!*()_?<>:;,.]')
    if not special_characters.search(password):
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*()).")
    else:
        strength_score += 1  # Add 1 point for special character
    
    # Determine password strength
    if strength_score == 5:
        feedback.append("Password is strong!")
    elif strength_score == 4:
        feedback.append("Password is medium strength.")
    else:
        feedback.append("Password is weak.")
    
    return feedback

def main():
    print("Welcome to the password strength checker!")
    
    # Prompt the user to input a password using raw_input for Python 2.7
    password = raw_input("Enter your password: ")
    
    # Check the strength of the password
    feedback = check_password_strength(password)
    
    # Display feedback to the user
    print("\nPassword Strength Assessment:")
    for message in feedback:
        print(message)

if __name__ == "__main__":
    main()
