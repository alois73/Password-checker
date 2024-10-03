def is_lower(value):
        value = list(value)
        check = []
        for i in range(len(value)):
            check.append(value[i].islower())
        return any(check)
    
def is_upper(value):
    value = list(value)
    check = []
    for i in range(len(value)):
        check.append(value[i].isupper())
    return any(check)
     
def is_digit(value):
    value = [int(char) if char.isdigit() else char for char in value]
    check = []
    for i in range(len(value)):
        check.append(isinstance(value[i], int)) 
    return any(check)
    
def is_alphanumerical(value):
    value = list(value)
    check = []
    for i in range(len(value)):
        check.append(value[i].isalnum())
    return any(check)
    
def is_long_enough(value):
    value = list(value)
    if len(value) < 6:
        return False
    return True
    
def criteria_check(value):
    criteria = []
    
    lower = is_lower(value)
    if lower == True:
        criteria.append(True)
    else:
        criteria.append(False)
        print('[*] There should be at least one lowercase letter')
    
    upper = is_upper(value)
    if upper == True:
        criteria.append(True)
    else:
        criteria.append(False)
        print('[*] There should be at least one uppercase letter')
        
    digit = is_digit(value)
    if digit == True:
        criteria.append(True)
    else:
        criteria.append(False)
        print('[*] There should be at least one number')
        
    anum = is_alphanumerical(value)
    if anum == True:
        criteria.append(True)
    else:
        criteria.append(False)
        print("[*] There there shouldn't be non alphanumerical characters")
        
    size = is_long_enough(value)
    if size == True:
        criteria.append(True)
    else:
        criteria.append(False)
        print("[*] The password should be at least 6 characters")
        
    return all(criteria)
    
def pass_check():
    password_passed = False 
    while not password_passed:
        password = input("Choose your password: ")
        password_passed = criteria_check(password) 
        if password_passed:
            print("[*] Password passed all checks!")
        else:
            print("Please try again.")

pass_check()