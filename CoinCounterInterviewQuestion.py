"""
Question: Find the amount of coins required to give the amount of cents given
The second function gets the types of coins whereas the first one only gives the total amount.
"""
def coin_number(cents):
    coinlist = [25, 10, 5, 1]
    coinlist.sort(reverse=True)
    """
        list must be in descending order
    """
    cointotal = 0
    while cents != 0:
        for coin in coinlist:
            if coin <= cents:
                cents -= coin
                cointotal += 1
                break
    return cointotal


def cointype(cents):
    coinlist = [25, 10, 5, 1]
    coinlist.sort(reverse=True)
    coincount = [[25,0],
                 [10,0],
                 [5,0],
                 [1,0]]

    while cents != 0:
        for coin in coinlist:
            if coin <= cents:
                cents -= coin
                coincount[coinlist.index(coin)][1] += 1
                break
    return coincount


print(coin_number(50))
