import getpass
import random

number_of_rounds = int(input("Wybierz ilość rund: "))
game_mode = input("Wybierz tryb gry: komputer/2 graczy: ")
player1_name = input("Wprowadź imię gracza: ")
results = []

choices = ["papier", "kamień", "nożyce"]

if game_mode == "komputer":
    player1_points = 0
    computer_points = 0
    for i in range(1, number_of_rounds+1):
        player1_choice = input("Wprowadź papier/kamień/nożyce: ")
        computer_choice = random.choice(choices)

        if player1_choice == computer_choice:
            print("Remis")
        elif player1_choice == "kamień":
            if computer_choice == "papier":
                print("Przegrywasz")
                computer_points+=1
            else:
                print("Wygrywasz")
                player1_points+=1
        elif player1_choice == "papier":
            if computer_choice == "nożyce":
                print("Przegrywasz")
                computer_points += 1
            else:
                print("Wygrywasz")
                player1_points += 1
        elif player1_choice == "nożyce":
            if computer_choice == "kamień":
                print("Przegrywasz")
                computer_points += 1
            else:
                print("Wygrywasz")
                player1_points += 1

        result = "Runda "+str(i) + ". " + str(player1_name) + ": " + str(player1_points) + " : Komputer: " + str(computer_points)
        results.append(result)
    print("\nPodsumowanie: ")
    for result in results:
        print(result)
    if computer_points > player1_points:
        print("Komputer wygrywa mecz")
    elif player1_points > computer_points:
        print(str(player1_name)+" wygrywa mecz")
    else:
        print("Remis")
elif game_mode == "2 graczy":
    player2_name = input("Wprowadź imię drugiego gracza: ")
    player1_points = 0
    player2_points = 0

    for i in range(1, number_of_rounds+1):
        player1_choice = getpass.getpass("(GRACZ 1) Wprowadź papier/kamień/nożyce: ")
        player2_choice = getpass.getpass("(GRACZ 2) Wprowadź papier/kamień/nożyce: ")

        if player1_choice == player2_choice:
            print("Remis")
        elif player1_choice == "kamień":
            if player2_choice == "papier":
                print(str(player2_name)+" wygrywa")
                player2_points+=1
            else:
                print(str(player1_name)+" wygrywa")
                player1_points+=1
        elif player1_choice == "papier":
            if player2_choice == "nożyce":
                print(str(player2_name)+" wygrywa")
                player2_points += 1
            else:
                print(str(player1_name)+" wygrywa")
                player1_points += 1
        elif player1_choice == "nożyce":
            if player2_choice == "kamień":
                print(str(player2_name)+" wygrywa")
                player2_points += 1
            else:
                print(str(player1_name)+" wygrywa")
                player1_points += 1

        result = "Runda "+str(i) + ". " + str(player1_name) + ": " + str(player1_points) + " : "+ str(player2_name) +": " + str(player2_points)
        results.append(result)
    print("\nPodsumowanie: ")
    for result in results:
        print(result)
    if player2_points > player1_points:
        print(str(player2_name)+" wygrywa mecz")
    elif player1_points > player2_points:
        print(str(player1_name)+" wygrywa mecz")
    else:
        print("Remis")


