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

        length = len(password)

        has_alpha = any(c.isalpha() for c in password)
        has_specialc = any(c in special_chars for c in password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_length12 = length >= 12
        has_length8 = 8 <= length < 12

        feedback = []

        #Verifica se possúi letras
        match(has_alpha):

            case (True):
                strength += 10

            case (False):
                feedback.append("Sua senha não possúi letras")
        
        #Verifica se possúi letras maiúsculas
        match(has_upper):

            case(True):
                strength += 30

            case(False):
                feedback.append("Sua senha não possúi letras maiúsculas")

        #Verifica se possúi letras minúsculas
        match(has_lower):
            
            case(True):
                strength += 10

            case(False):
                feedback.append("Sua senha não possúi letras minúsculas")

        #Verifica se possúi caracter especiais
        match(has_specialc):

            case(True):
                strength += 30

            case(False):
                feedback.append("Sua senha não possúi caracteres especiais")

        #Verifica se possúi digitos
        match(has_digit):

            case(True):
                strength += 10

            case(False):
                feedback.append("Sua senha não possúi digitos")

        #Verifica o tamanho
        match (has_length12, has_length8):

            case (False, False):
                print("Sua senha não possúi tamanho minímo de 8 caracteres")

            case (False, True):
                strength += 5
                print("Sua senha não possúi o tamanho recomendado de 12 caracteres")
            
            case (True, False):
                strength += 10
        
        match(has_alpha, has_digit, has_lower, has_upper, has_specialc, has_length12):

            case(True, True, True, True, True, True):
                feedback.append("Nenhuma alteração necessária")

        for item in feedback:
            print(item)

        print(f"Password strength: {strength}/100")
    except Exception as e:
        print(f"Erro: {e}")



