import random, time, sys
score = 0
choices = ['🪨', '🗒️', '✂️']
while True:
    odp = input("Papier (1), Kamień (2), Nożyce (3). Wybierz swoją opcję, 'Q' aby wyjść, 'S' aby zobaczyć punkty: ")
    if odp.lower() == 'q':
        quit()
    elif odp.lower() == 's':    
        print(f"Twoje punkty: {score}")
    elif odp == '1' or odp == "papier":
        print("Wybrałeś papier.")
        for x in range(15):
                print(f"\rKomputer wybiera... [ {random.choice(choices)} ]", end="", flush=True)
        time.sleep(0.15)
        AI = random.choice(choices)
        print(f"\rKomputer wybrał...  [ {AI} ]     ")
        time.sleep(0.5)
        if AI == '🪨':
            print("Wygrałeś!")
            score += 1
        elif AI == '🗒️':
            print("Remis!")
        elif AI == '✂️':
            print("Przegrałeś!")
    elif odp == '2' or odp == "kamien":
        print("Wybrałeś kamień.")
        for x in range(15):
            print(f"\rKomputer wybiera... [ {random.choice(choices)} ]", end="", flush=True)
            time.sleep(0.15)
        AI = random.choice(choices)
        print(f"\rKomputer wybrał...  [ {AI} ]     ")
        time.sleep(0.5)
        if AI == '🪨':
            print("Remis!")
        elif AI == '🗒️':
            print("Przegrałeś!")
        elif AI == '✂️':
            print("Wygrałeś!")
            score += 1
    elif odp == '3' or odp == "nozyce":
        print("Wybrałeś nożyce.")
        for x in range(15):
            print(f"\rKomputer wybiera... [ {random.choice(choices)} ]", end="", flush=True)
            time.sleep(0.15)
        AI = random.choice(choices)
        print(f"\rKomputer wybrał...  [ {AI} ]     ")
        time.sleep(0.5)
        if AI == '🪨':
            print("Przegrałeś!")
        elif AI == '🗒️':
            print("Wygrałeś!")
            score += 1
        elif AI == '✂️':
            print("Remis!")
    else:
        print("Nieprawidłowa opcja. Wybierz 1, 2, 3 lub Q.")
    time.sleep(0.5)
    