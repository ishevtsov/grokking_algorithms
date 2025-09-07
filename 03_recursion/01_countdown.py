def countdown(i):
    # base case
    if i <= 0:
        return 0
    # recursive case
    else:
        print(i)
        countdown(i-1)


if __name__ == '__main__':
    countdown(5)
