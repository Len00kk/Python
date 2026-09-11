import subprocess, time, random
def fancy():
    print("Media reader:")
    time.sleep(0.5)
    print("Snatching info...")
    time.sleep(0.5)
    print("Polishing...")
    time.sleep(0.5)
    print("Found!")
    time.sleep(0.5)
    print("===============================================================================================================")
    print(" ")
option = 0
fancy()
check = subprocess.run(['playerctl', 'metadata', '--format', '{{playerName}}'], capture_output = True, text = True)
MediaName = check.stdout
MediaName = MediaName.strip()
if MediaName == "spotify":
    command = subprocess.run(['playerctl', 'metadata', '--format', 'You are on Spotify listening to {{title}} made by {{artist}} from this album: {{album}}'], capture_output = True, text=True )
    Media = command.stdout
    option = 1
    print(Media)
elif MediaName == "brave" or "chrome" or "firefox" or "chronium":
    command = subprocess.run(['playerctl', 'metadata', '--format', 'You are on Youtube watching {{title}}'], capture_output = True, text=True )
    Media = command.stdout
    option = 2
    print(Media)
else:
    command = subprocess.run(['playerctl', 'metadata', '--format', 'You are not watching or listening to anything.'], capture_output = True, text=True )
print("===============================================================================================================")
time.sleep(3)
i = random.randint(1, 10)
if i == 1 or 6:
    print("It's good.")
elif i == 2 or 7:
    print("What the hell is that")
elif i == 3 or 8 or 9:
    print("What a banger")
elif i == 4 or 10:
    print("I guess it's fine")
elif i == 5:
    print("Turn that shit off")
print(" ")
time.sleep(2)
while True:  
    print("Is there anything else?")
    print("==================================================================================================")
    print("1. Play next")
    print("2. Pause/Play")
    print("3. Play Previous")
    print("4. Set app volume")
    print("5. Quit")
    print("==================================================================================================")
    ans = input("")
    ans = int(ans)
    if ans == 4 and option == 1:
        volume = input("What would you like to change your volume on Spotify to? (from 0.1 to 1)")
        volume = float(volume)
        command2 = subprocess.run(['playerctl', '-p', 'spotify', 'volume', str(volume)], text=True)
        print(f"Set volume to {volume}")
    elif ans == 4 and option == 2:
        volume = input("What would you like to change your volume on Youtube to? (from 0.1 to 1)")
        volume = float(volume)
        command2 = subprocess.run(['playerctl', '-p', str(MediaName), 'volume', str(volume)], text=True)
        print(f"Set volume to {volume}")
    elif ans == 1:
        command2 = subprocess.run(['playerctl', 'next'])
        time.sleep(0.2)
        command3 = subprocess.run(['playerctl', 'metadata', '--format', 'Skipped! Now playing: {{title}} - {{artist}}'], capture_output = True, text = True)
        result = command3.stdout
        print(result)
    elif ans == 2:
        command2 = subprocess.run(['playerctl', 'play-pause'])
        print("Done!")
    elif ans == 3:
        command2 = subprocess.run(['playerctl', 'previous'])
        time.sleep(0.2)
        command3 = subprocess.run(['playerctl', 'metadata', '--format', 'Skipped! Now playing: {{title}} - {{artist}}'], capture_output = True, text = True)
        result = command3.stdout
        print(result)
    elif ans == 5:
        quit()
    