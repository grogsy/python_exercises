import random

def rps():
    valid_options = 'rock paper scissor'.split()
    player_choice = str(input("Pick: rock, paper, scissor>")).lower()
    ai_choice     = random.choice(valid_options)

    assert player_choice in valid_options

    print("You> %s || %s <Computer" % (player_choice, ai_choice))

    if player_choice == ai_choice:
        print('tie\n')
    elif (player_choice, ai_choice) in (('rock', 'scissor'), ('scissor', 'paper'), ('paper', 'rock')):
        print('you win\n')
    else:
        print('you lose\n')

def play(rounds=1):
    for i in range(rounds):
        rps()

if __name__ == '__main__':
    print("\nRock paper scissors. Hit ctrl-c to exit\n\n")
    while True:
        try:
            play()
        except KeyboardInterrupt:
            break
