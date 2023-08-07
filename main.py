from colorama import Fore, Style
from time import sleep
import random

rock = '\033[1m' + f'{Fore.RED}ROCK{Style.RESET_ALL}'
paper = '\033[1m' + f'{Fore.GREEN}PAPER{Style.RESET_ALL}'
scissors = '\033[1m' + f'{Fore.BLUE}SCISSORS{Style.RESET_ALL}'

# for displaying available choices with highlighted keys
r_pick = '\033[1m' + f'({Fore.RED}R{Style.RESET_ALL})OCK'
p_pick = '\033[1m' + f'({Fore.GREEN}P{Style.RESET_ALL})APER'
s_pick = '\033[1m' + f'({Fore.BLUE}S{Style.RESET_ALL})CISSORS'

picks = {'r': rock, 'p': paper, 's': scissors}  # translate inputs into painted versions
verbs = ['crushed', 'covered', 'snipped']  # appropriate verbs for game completion outputs


def main():
    flag = True
    score1, score2 = 0, 0
    print(f"Welcome to...\n")
    sleep(1)
    print(f"{rock}|{paper}|{scissors}\n")
    selection = True
    while selection:
        mode = input("Choose mode:\n(1).PvP (2).PvE\n ")
        if mode == '1':
            name1 = input('Player one, enter your name: ')
            name2 = input('Player two, enter your name: ')
            pve = False
            selection = False
        elif mode == '2':
            name1, name2 = 'Player', 'Computer'
            pve = True
            selection = False
        else:
            print("Invalid input. Please enter 1 or 2.")
    while True:
        if flag:
            pick1 = input(f'\n{name1}, select your move:\n'
                          f'-{r_pick}-{p_pick}-{s_pick}-\n').lower().strip()
            if pick1 not in 'rps' or len(pick1) != 1:
                print('Invalid pick. Try again')
                continue
            else:
                flag = False
        else:
            if pve:
                pick2 = random.choice('rps')
            else:
                pick2 = input(f'\n{name2}, select your move:\n'
                              f'-{r_pick}-{p_pick}-{s_pick}-\n').lower().strip()
            if pick2 not in 'rps' or len(pick2) != 1:
                print('Invalid pick. Try again')
                continue
            else:
                flag = True

            if pick1 == pick2:
                print(f"Both players selected {picks[pick1]}. Draw!")
                score1 += 0.5
                score2 += 0.5
                print(f'\nSCORE:\n{name1}: {score1}\n{name2}: {score2}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break
            # two strings for victory evaluation.
            # Each letter of 1st string wins over each letter in the 2nd (r>s, p>r, s>p)
            strng1, strng2 = 'rps', 'srp'
            if not strng1.index(pick1) - strng2.index(pick2):
                score1 += 1
                print(f"{name1} has {verbs[strng1.index(pick1)]} {name2}'s {picks[pick2]} with {picks[pick1]}!")
                print(f'\nSCORE:\n{name1}: {score1}\n{name2}: {score2}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break
            else:
                score2 += 1
                print(f"{name2} has {verbs[strng1.index(pick2)]} {name1}'s {picks[pick1]} with {picks[pick2]}!")
                print(f'\nSCORE:\n{name1}: {score1}\n{name2}: {score2}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break


if __name__ == '__main__':
    main()
