import random

lotto_list = [x for x in range(1, 50)]
user_choice = []

intro = """
To jest symulator LOTTO
Wybierz 6 liczb z zakresu od 1 do 49.
"""
print(intro)


def comply_checker(a):
    try:
        a = int(a)
        if a <= 49 and a >= 1:
            if a not in user_choice:
                return True
            else:
                print("Wprowadziłeś już taką liczbę!")
                return False
        else:
            print("Wprowadź liczbę z zakresu od 1 do 49!")
            return False
    except ValueError:
        print("Wprowadź poprawną liczbę!")
        return False


def win_checker(lst, lst2):
    counter = 0
    final_message = ""
    for num in lst:
        if num in lst2:
            counter += 1
    if (counter == 5) or (counter == 6):
        final_message = f"Trafiłeś {counter} liczb!"
    elif (counter == 3) or (counter == 4):
        final_message = f"Trafiłeś {counter} liczby!"
    else:
        final_message = "Niestety nie wygrałeś."
    return final_message


for x in range(6):
    while True:
        y = input(f"Wprowadź {x + 1} liczbę: ")
        if comply_checker(y) == True:
            break
    y = int(y)
    user_choice.append(y)

user_choice = sorted(user_choice)
print(f"Twoje liczby: {user_choice}")

random.shuffle(lotto_list)
lotto_winning6 = [y for y in lotto_list[0:6]]
print(f"Wygrywające liczby: {lotto_winning6}")

print(win_checker(user_choice, lotto_winning6))
