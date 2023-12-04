def calcule(num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2

while True:
    try:
        num1 = input("Entrez le premier nombre : ")
        operator = input("Entrez l'opérateur (+, -, *, /, %) : ")
        num2 = input("Entrez le deuxième nombre : ")
        resultat = calcule(num1, operator, num2)
        print("Résultat :", resultat)
        break
    
    except ZeroDivisionError as e:
        print("Erreur :" ,type(e).__name__ , e)
        print("La division par zéro n'est pas autorisée. Veuillez réessayer.")
    except ValueError as e:
        print("Erreur :" ,type(e).__name__ , e)
        print("Veuillez entrer des nombres valides. Veuillez réessayer.")
    except Exception as e:
        print("Une exception de type a été levée :" ,type(e).__name__ , e)
        print("Une erreur s'est produite. Veuillez réessayer.")
 
 
 
 
 
    