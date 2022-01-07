import random
import pandas as pd
import csv
import numpy as np
import math

total_money = 0
money_to_give = 500
upg_1 = 0
upg_2 = 0
upg_3 = 0
upg_4 = 0
def_cost_to_upgrade = 500

print('Game is ready to play!')
print('Typing "collect" will give you money. Typing "upgrade" will allow you to upgrade your levels, as long as you have fulfilled the reqirements.')
with open(f'C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/upg1.txt','r') as f:
    try:
        lvl = f.read()
        if lvl != '':
            upg_1 = lvl
        else:
            upg_1 = 0
    except ValueError:
        print('Error reading from file. Possibly no data in the file. Setting values to 0.')
        print(upg_1)
        upg_1 = 0
    except:
        print('Error')

with open(f'C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/upg2.txt','r') as f:
    try:
        lvl = f.read()
        if lvl != '':
            upg_2 = lvl
        else:
            upg_2 = 0
    except ValueError:
        print('Error reading from file. Possibly no data in the file. Setting values to 0.')
        print(upg_2)
        upg_2 = 0
    except:
        print('Error')

with open(f'C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/upg3.txt','r') as f:
    try:
        lvl = f.read()
        if lvl != '':
            upg_3 = lvl
        else:
            upg_3 = 0
    except ValueError:
        print('Error reading from file. Possibly no data in the file. Setting values to 0.')
        print(upg_3)
        upg_3 = 0
    except:
        print('Error')

with open(f'C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/upg4.txt','r') as f:
    try:
        lvl = f.read()
        if lvl != '':
            upg_4 = lvl
        else:
            upg_4 = 0
    except ValueError:
        print('Error reading from file. Possibly no data in the file. Setting values to 0.')
        print(upg_4)
        upg_4 = 0
    except:
        print('Error')

with open('C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/money.txt','r') as f:
    try:
        money = f.read()
        total_money = money
    except ValueError:
        print('Error reading from file. Possibly no data in the file. Setting values to 0.')
        total_money = 0
    except:
        print(Exception)



while True:
    print(upg_1,upg_2)
    command = input('')
    c = str(command).lower()
    if c == 'test':
        upg_1 = 100
        upg_2 = 100
        upg_3 = 100
        upg_4 = 100
        total_money = 1000000
    if c == 'upgrade':
        print()
        print('Which would you like to upgrade?')
        print('Upgrade 1: Gives a + 0.05x multiplier. Cost: 2500 ')
        print('Upgrade 2: Gives a + 0.15x multiplier. Cost: 6250')
        print('Upgrade 3: Gives a + 0.4x multiplier. Cost: 12500 ')
        print('Upgrade 4: Gives a + 1x multiplier. Cost: 25000')
        choice = input('')
        if choice == '1' or choice.lower() == 'upgrade 1':
            print('How many levels?')
            level_amt = input('')
            if level_amt == 'max':
                max_upgrade = int(total_money) / 2500
                if int(max_upgrade) < max_upgrade:
                    f= math.floor(max_upgrade)
                    cost_to_upgrade = int(f) * 2500
                    total_money = int(total_money) - int(cost_to_upgrade)
                    upg_1 = int(upg_1) + int(f)
                    print(f'Upgrade 1 has been upgraded by {f} for a total of {upg_1}')
                    print(f'{cost_to_upgrade} has been deducted from your account')
                else:
                    cost_to_upgrade = int(max_upgrade) * 2500
                    total_money = total_money - cost_to_upgrade
                    upg_1 = int(upg_1) + int(max_upgrade)
                    print(f'Level one has been upgraded by {max_upgrade} for a total of {upg_1}')
                    print(f'{cost_to_upgrade} has been deducted from your account')
            elif level_amt != 'max':
                    amount_to_upgrade = int(level_amt)
                    cost_to_upgrade = int(amount_to_upgrade) * 2500
                    if total_money >= cost_to_upgrade:
                        total_money = int(total_money) - int(cost_to_upgrade)
                        upg_1 = int(upg_1) + int(amount_to_upgrade)
                        print(f'Level 1 has been upgraded by {amount_to_upgrade} for a total of {upg_1}')
                        print(f'{cost_to_upgrade} has been deducted from your account')
                    else:
                        print('Not enough money')

        if choice == '2' or choice.lower() == 'upgrade 2':
            if int(upg_1) < 20:
                print("Upgrade 1 has to be at least level 15.")
            else:
                print('How many levels?')
                level_amt = input('')
                if level_amt == 'max':
                    max_upgrade = int(total_money) / 6250
                    if int(max_upgrade) < max_upgrade:
                        f= math.floor(max_upgrade)
                        cost_to_upgrade = int(f) * 6250
                        total_money = int(total_money) - int(cost_to_upgrade)
                        upg_2 = int(upg_2) + int(f)
                        print(upg_2)
                        print(f'Level 1.1 has been upgraded by {f} for a total of {upg_2}')
                        print(f'{cost_to_upgrade} has been deducted from your account')
                    else:
                        cost_to_upgrade = int(max_upgrade) * 6250
                        total_money = total_money - cost_to_upgrade
                        upg_2 = upg_2 + max_upgrade
                        print(f'Level 1.1 has been upgraded by {max_upgrade} for a total of {upg_2}')
                        print(f'{cost_to_upgrade} has been deducted from your account')

                else:
                    try:
                        amount_to_upgrade = int(level_amt)
                        cost_to_upgrade = int(amount_to_upgrade) * 6250
                        if total_money >= cost_to_upgrade:
                            total_money = int(total_money) - int(cost_to_upgrade)
                            print(f'Level 1.1 has been upgraded by {amount_to_upgrade} for a total of {upg_2}')
                            print(f'{cost_to_upgrade} has been deducted from your account')
                        else:
                            print('Not enough money')
                    except:
                        print('Error')

        if choice == '3' and int(upg_1) < 30 and int(upg_2) < 30:
            print("Upgrade 1 and Upgrade 2 have to be at least level 30.")
        elif choice == '3' and int(upg_1) >=30 and int(upg_2) >=30:
            print('How many levels?')
            level_amt = input('')
            if level_amt == 'max':
                max_upgrade = int(total_money) / 12500
                if int(max_upgrade) < max_upgrade:
                    f= math.floor(max_upgrade)
                    cost_to_upgrade = int(f) * 12500
                    total_money = int(total_money) - int(cost_to_upgrade)
                    upg_3 = int(upg_3) + int(f)
                    print(upg_3)
                    print(f'Level 2 has been upgraded by {f} for a total of {upg_3}')
                    print(f'{cost_to_upgrade} has been deducted from your account')
                else:
                    cost_to_upgrade = int(max_upgrade) * 12500
                    total_money = total_money - cost_to_upgrade
                    upg_3 = upg_3 + max_upgrade
                    print(f'Level 3 has been upgraded by {max_upgrade} for a total of {upg_3}')
                    print(f'{cost_to_upgrade} has been deducted from your account')

            else:
                try:
                    amount_to_upgrade = int(level_amt)
                    cost_to_upgrade = int(amount_to_upgrade) * 12500
                    if total_money >= cost_to_upgrade:
                        total_money = int(total_money) - int(cost_to_upgrade)
                        print(f'Level 3 has been upgraded by {amount_to_upgrade} for a total of {upg_3}')
                        print(f'{cost_to_upgrade} has been deducted from your account')
                    else:
                        print('Not enough money')
                except:
                    print('Error')
        if choice == '4' and int(upg_1) < 50 and int(upg_2) < 50 and int(upg_3) < 50:
            print("Upgrades 1, 2, and 3 have to be at least level 50.")
        elif choice == '4' and int(upg_1) >=50 and int(upg_2) >=50 and int(upg_3) >= 50:
            print('How many levels?')
            level_amt = input('')
            if level_amt == 'max':
                max_upgrade = int(total_money) / 25000
                if int(max_upgrade) < max_upgrade:
                    f= math.floor(max_upgrade)
                    cost_to_upgrade = int(f) * 25000
                    total_money = int(total_money) - int(cost_to_upgrade)
                    upg_3 = int(upg_3) + int(f)
                    print(upg_3)
                    print(f'Level 2 has been upgraded by {f} for a total of {upg_3}')
                    print(f'{cost_to_upgrade} has been deducted from your account')
                else:
                    cost_to_upgrade = int(max_upgrade) * 25000
                    total_money = total_money - cost_to_upgrade
                    upg_3 = upg_3 + max_upgrade
                    print(f'Level 3 has been upgraded by {max_upgrade} for a total of {upg_3}')
                    print(f'{cost_to_upgrade} has been deducted from your account')

            else:
                try:
                    amount_to_upgrade = int(level_amt)
                    cost_to_upgrade = int(amount_to_upgrade) * 25000
                    if total_money >= cost_to_upgrade:
                        total_money = int(total_money) - int(cost_to_upgrade)
                        print(f'Level 3 has been upgraded by {amount_to_upgrade} for a total of {upg_3}')
                        print(f'{cost_to_upgrade} has been deducted from your account')
                    else:
                        print('Not enough money')
                except:
                    print('Error')
    # End of upgrade code

    if c == 'collect':
        mult = 1 + (int(upg_1) * 0.05 + int(upg_2) * 0.15 + int(upg_3) * 0.4 + int(upg_4) ) 
        print(mult)
        if mult != 0:
            money_to_give = 500 * mult
        else:
            money_to_give = 500
        total_money = int(total_money) + int(money_to_give)
        print(f'{math.floor(money_to_give)} has been added to your account')

    if c == 'reset':
        confirm = input('Are you sure? (y/n)').lower()
        if confirm == 'y':
            upg_1 = 0
            upg_2 = 0
            upg_3 = 0
            upg_4 = 0
            total_money = 0
            print('Data has been reset')
        elif confirm == 'n':
            print('Returning to game')
            pass
        else:
            print('Invalid command')

    #informative commands / invalid command

    if c == 'balance':
        print(f'Your total balance is: {total_money}')
    elif c == 'levels':
        print(f'Upgrade 1: {upg_1}')
        print(f'Upgrade 2: {upg_2}')
        print(f'Upgrade 3: {upg_3}')
        print(f'Upgrade 4: {upg_4}')
    elif c == 'collect':
        pass
    elif 'upgrade' in c:
        pass
    elif c == 'reset':
        pass
    elif c == 'y' or c == 'n':
        pass
    else:
        print('Invalid command')

    # writing to stats files to save data between playthroughs 

    with open('C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/upg1.txt','w') as f:
        f.write(str(upg_1))
    with open('C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/upg2.txt','w') as f:
        f.write(str(upg_2))
    with open('C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/upg3.txt','w') as f:
        f.write(str(upg_3))
    with open('C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/upg4.txt','w') as f:
        f.write(str(upg_4))
    with open('C:/Users/Ryan Beaulieu/Desktop/Python VENV/VENV/stats_folder/money.txt','w') as f:
        f.write(str(total_money))


    
