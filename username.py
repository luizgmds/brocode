def validation(username):
    usernameMaxChar = len(username)
    usernameSpaces = username.count(" ")
    usernameAlpha = username.isalpha()
    
    if usernameMaxChar <= 12 and usernameSpaces == 0 and usernameAlpha:
        return "Username Aceito"
    else:
        return "Username invalido"
    
validationResult = validation(username = input("Digite seu username: "))

print(validationResult)



