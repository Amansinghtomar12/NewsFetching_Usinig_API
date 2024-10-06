import hashlib
    
def ValidateEmail(email):
    allowed_domains = (
        "gmail.com",
        "outlook.com",
        "hotmail.com",
        "rediffmail.com",
        "yahoo.com",
        "icloud.com",
        "mail.com",
        "zoho.com",
        "protonmail.com",
        "aol.com",
        "yandex.com",
        "live.com",
        "tutanota.com"
    )
    if email.endswith(allowed_domains):
        return True
    return False

def ValidatePassword(password):
    if len(password) < 8:
        return False
    else:
        special_characters = "!@#$%^&*()-_=+"
        
    has_special_char = False
    for char in password:
        if char in special_characters:
            has_special_char = True
            break 
    return has_special_char

def ValidateMobileNumber(mNumber):
    return (len(mNumber) == 10 and mNumber.isdigit())

def ValidateUsername(uName):
    if len(uName) <= 4:
        return False
    if not uName.isalnum():       # alphanumeric
        return False
    return True

def HashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()





