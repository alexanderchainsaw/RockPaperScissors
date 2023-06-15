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
    name1_score, name2_score = 0, 0
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
            p1 = input(f'\n{name1}, select your move:\n'
                       f'-{r_pick}-{p_pick}-{s_pick}-\n').lower().strip()
            if p1 not in 'rps' or len(p1) != 1:
                print('Invalid pick. Try again')
                continue
            else:
                flag = False
        else:
            if pve:
                p2 = random.choice('rps')
            else:
                p2 = input(f'\n{name2}, select your move:\n'
                           f'-{r_pick}-{p_pick}-{s_pick}-\n').lower().strip()
            if p2 not in 'rps' or len(p2) != 1:
                print('Invalid pick. Try again')
                continue
            else:
                flag = True

            if p1 == p2:
                print(f"Both players selected {picks[p1]}. Draw!")
                name1_score += 0.5
                name2_score += 0.5
                print(f'\nSCORE:\n{name1}: {name1_score}\n{name2}: {name2_score}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break
            # two strings for victory evaluation.
            # Each letter of 1st string wins over each letter in the 2nd (r>s, p>r, s>p)
            strng1, strng2 = 'rps', 'srp'
            if strng1.index(p1) - strng2.index(p2) == 0:
                name1_score += 1
                print(f"{name1} has {verbs[strng1.index(p1)]} {name2}'s {picks[p2]} with {picks[p1]}!")
                print(f'\nSCORE:\n{name1}: {name1_score}\n{name2}: {name2_score}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break
            else:
                name2_score += 1
                print(f"{name2} has {verbs[strng1.index(p2)]} {name1}'s {picks[p1]} with {picks[p2]}!")
                print(f'\nSCORE:\n{name1}: {name1_score}\n{name2}: {name2_score}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break


if __name__ == '__main__':
    main()
