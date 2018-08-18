import random

def rps():
    valid_options = 'rock paper scissor'.split()
    player_choice = str(input("Pick: rock, paper, scissor>")).lower()
    ai_choice     = random.choice(valid_options)

    assert player_choice in valid_options

    print("You> %s || %s <Computer" % (player_choice, ai_choice))

    if player_choice == ai_choice:
        print('tie')
    elif (player_choice, ai_choice) in (('rock', 'scissor'), ('scissor', 'paper'), ('paper', 'rock')):
        print('you win')
    else:
        print('you lose')

def play(rounds=1):
    for i in range(rounds):
        rps()

if __name__ == '__main__':
    while True:
        try:
            play()
        except KeyboardInterrupt:
            break
