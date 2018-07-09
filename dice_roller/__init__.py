from secrets import randbelow


def get_input():
    dice_input = input('Please enter a DnD die notation, eg. 3d6\n')
    parse_dice_input(dice_input)


def parse_dice_input(dice_input):
    split_arr = dice_input.split('d')
    num_of_rolls = split_arr[0]
    num_of_sides = split_arr[1]
    roll_dice(num_of_rolls, num_of_sides)


def roll_dice(num_of_rolls, num_of_sides):
    total_roll = 0

    for i in range(int(num_of_rolls)):
        roll = randbelow(int(num_of_sides) + 1)
        total_roll += roll
        print(str(roll) + ' ', end='')

    print('= ' + str(total_roll) + '\n')

    roll_again()


def roll_again():
    is_roll_again = input('Do you want to roll again? yes/no\n')
    if is_roll_again == 'yes':
        get_input()
