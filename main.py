from colorama import Fore, Style
from time import sleep

rock = '\033[1m' + f'{Fore.RED}ROCK{Style.RESET_ALL}'
paper = '\033[1m' + f'{Fore.GREEN}PAPER{Style.RESET_ALL}'
scissors = '\033[1m' + f'{Fore.BLUE}SCISSORS{Style.RESET_ALL}'

r_pick = '\033[1m' + f'({Fore.RED}R{Style.RESET_ALL})OCK'
p_pick = '\033[1m' + f'({Fore.GREEN}P{Style.RESET_ALL})APER'
s_pick = '\033[1m' + f'({Fore.BLUE}S{Style.RESET_ALL})CISSORS'

picks = {'r': rock, 'p': paper, 's': scissors}
verbs = ['crushed', 'covered', 'snipped']
strng1, strng2 = 'rps', 'srp'


def main():
    print(f"Welcome to...\n")
    sleep(1)
    print(f"{rock}|{paper}|{scissors}\n")
    name1 = input('Player one, enter your name: ')
    name2 = input('Player two, enter your name: ')
    flag = True
    name1_score = 0
    name2_score = 0
    while True:
        if flag:
            p1 = input(f'\n{name1}, chose your move:\n'
                       f'-{r_pick}-{p_pick}-{s_pick}-\n').lower().strip()
            if p1 not in 'rps':
                print('Invalid pick. Try again')
                continue
            else:
                flag = False
        else:
            p2 = input(f'\n{name2}, chose your move:\n'
                       f'-{r_pick}-{p_pick}-{s_pick}-\n').lower().strip()
            if p2 not in 'rps':
                print('Invalid pick. Try again')
                continue
            else:
                flag = True

            p1_pick, p2_pick = picks[p1], picks[p2]
            if p1_pick == p2_pick:
                print(f"Both players chose {p1_pick}. Draw!")
                name1_score += 0.5
                name2_score += 0.5
                print(f'\nSCORE:\n{name1}: {name1_score}\n{name2}: {name2_score}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break
            if not strng1.index(p1) - strng2.index(p2):
                name1_score += 1
                print(f"{name1} has {verbs[strng1.index(p1)]} {name2}'s {p2_pick} with {p1_pick}!")
                print(f'\nSCORE:\n{name1}: {name1_score}\n{name2}: {name2_score}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break
            else:
                name2_score += 1
                print(f"{name2} has {verbs[strng1.index(p2)]} {name1}'s {p1_pick} with {p2_pick}!")
                print(f'\nSCORE:\n{name1}: {name1_score}\n{name2}: {name2_score}\n')
                if input('Rematch?(Y/N): ').lower() == 'y':
                    continue
                else:
                    break


if __name__ == '__main__':
    main()
