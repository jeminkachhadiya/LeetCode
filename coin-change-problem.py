import time


def get_nums_of_coins(coins, amount):
    new_coins = sorted(coins)
    dp = [amount for _ in range(amount + 1)]
    dp[0] = 0
    for each_amo in range(1, amount + 1):
        for coin in new_coins:
            if coin <= each_amo:
                dp[each_amo] = min(dp[each_amo], 1 + dp[each_amo - coin])
            else:
                break
    return dp[amount] if dp[amount] <= amount else -1


def greedy(exchange):
    rupee10 = 0
    rupee5 = 0
    rupee2 = 0
    rupee1 = 0
    while(exchange != 0):
        if(exchange>=10):
            exchange = exchange-10
            rupee10 = rupee10+1
        elif(exchange>=5):
            exchange = exchange-5
            rupee5 = rupee5+1
        elif(exchange>=2):
            exchange = exchange-2
            rupee2 = rupee2+1
        else:
            exchange = exchange-1
            rupee1 = rupee1+1
    print(" Rupee coin 10 :",rupee10)
    print(" Rupee coin 5 :",rupee5)
    print(" Rupee coin 2 :",rupee2)
    print(" Rupee coin 1 :",rupee1)


if __name__ == "__main__":
    coins = [1, 2, 5, 10]
    sum = int(input("Enter Rupee amount to change in coin: "))    
    print(f" Coins : {coins}\n Sum : {sum}")
    print("========= Brute Force Solution ==========")
    begin = time.perf_counter()
    print(" Minimum coins:",get_nums_of_coins(coins,sum))
    end = time.perf_counter()
    print(" Time execution : ",end-begin)
    print("\n=========== Greedy Solution =============")
    begin = time.perf_counter()
    greedy(sum)
    end = time.perf_counter()
    print(" Time execution : ",end-begin)
