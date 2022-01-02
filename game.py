import random
import pandas as pd
import csv

total_money = 0
money_to_give = 500
upgrade_level = 0
def_cost_to_upgrade = 500
while True:
    command = input('')
    c = str(command).lower()
    if 'upgrade' in c:
        if len(c) > 8:
            amount_to_upgrade = c.split(' ')[1]
            cost_to_upgrade = int(amount_to_upgrade) * 500
            print(amount_to_upgrade)
        else:
            amount_to_upgrade = int(1)
            cost_to_upgrade = int(amount_to_upgrade) * 500
        if total_money >= int(cost_to_upgrade):
            upgrade_level = upgrade_level + int(amount_to_upgrade)
            total_money = total_money - cost_to_upgrade
            print(upgrade_level)
        elif total_money <= int(cost_to_upgrade):
            print('Not enough money')

    if c == 'collect' and upgrade_level == int(0):
        total_money = int(total_money) + int(money_to_give)

    elif c == 'collect' and upgrade_level != int(0):
        f = int(money_to_give) + (int(money_to_give) * (int(upgrade_level) * 0.1))
        total_money = int(total_money) + int(f)
    if c == 'balance':
        print(f'Your total balance is: {total_money}')
    if c == 'level':
        print(f'Your upgrade level is: {upgrade_level}')

