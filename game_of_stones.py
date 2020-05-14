"""
I noticed that there is a pattern in the results of the second player.
So, I solved it by means of a formula.
The second player only wins if "n" is a multiple of 7 or its predecessor.
"""


def gameOfStones(n):
    if (n % 7 == 0) or ((n - 1) % 7 == 0):
        return 'Second'
    else:
        return 'First'


if __name__ == '__main__':
    fptr = open('game_of_stones_result.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
