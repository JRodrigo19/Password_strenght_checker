special_chars = ['@', '!', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '=', '+', '_']

while True:
    try:
        password = input("\nEnter password (or type 'exit' to exit): ")

        if password.lower() == 'exit':
            print("\nExiting the program.")
            break

        if not password:
            print("\nNo password was entered.")
            continue

        strength = 0

        feedback = []

        if any(char in special_chars for char in password):
            strength += 20

        else:
            feedback.append("Sua senha não possui caracteres especiais")
    
        if any(char.isalpha() for char in password):

            if any(char.isupper() for char in password):
                strength += 20
            
            else:
                feedback.append("Sua senha não possúi letras maiúsculas")
        
            if any(c.islower() for c in password):
                strength += 20
            
            else:
                feedback.append("Sua senha não possúi letras minúsculas")
                
        else:
            feedback.append("Sua senha não possúi letras maísculas e/ou minúsculas")

        if any(char.isdigit() for char in password):
            strength += 20

        else:
            feedback.append("Sua senha não possúi números")

        if len(password) >= 12:
            strength += 20

        elif len(password) >= 8:
            strength += 10
            feedback.append("Sua senha possui tamanho de 8 ou mais caracteres, mas poderá melhorar se tiver no minimo 12")

        else:
            feedback.append("Sua senha não possúi o tamanho mínimo de 8 caracteres, adicione caracteres para chegar a 8 ou 12 para ficar melhor")

        print(f"Password strength: {strength}/100")

        for item in feedback:
            print(item)
    except Exception as e:
        print(f"Erro: {e}")



