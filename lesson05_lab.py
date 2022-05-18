# Write your code here :-)
def alarm_clock(day, vacation):
    # conditional to determine if we're on vacation
    if vacation:
        # determine if it's the weekend
        if day == 0 or day == 6:
            return 'off'
        # on vacation, but a week day
        else:
            return '10:00'
    # not on vacation, execute below
    else:
        # not on vacation but the weekend
        if day == 0 or day == 6:
            return '10:00'
        # not on vacation and a week day
        else:
            return '7:00'


# validate input
# weekend and vacation - 'off'
alarm_clock(0, True)
# weekend not vacation - '10:00'
alarm_clock(6, False)
# week day and vacation - '10:00'
alarm_clock(4, True)
# week day not vacation - '7:00'
alarm_clock(2, False)


def check_guess(guess, target):
    # conditional: is guess less than target
    if guess < target:
        return 'too low'
    # conditional: is guess equal to target
    elif guess == target:
        return 'correct'
    # conditional: is guess greater than target
    else:
        return 'too high'

# validate input
check_guess(5, 7)
check_guess(7, 7)
check_guess(9, 7)
