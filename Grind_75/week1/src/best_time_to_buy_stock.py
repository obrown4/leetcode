#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Best Time to Buy and Sell Stock #121

#Top Down
def maxProfit(prices: list[int]) -> int:
    max_p = 0
    max_sell_price = 0
    return max(max_p, topDownP(prices, max_p, max_sell_price, len(prices) - 1))

def topDownP(prices: list[int], mp: int, msp: int, n: int) -> int:
    print(msp, mp)
    if n == 0:
        return msp - prices[n]
    msp = max(prices[n], msp)
    mp = max(msp - prices[n], max(mp, topDownP(prices, mp, msp, n - 1)))
    return mp

#Bottom Up (Fatser Runtime)
#STATS
#   Runtime         Memory
#   O(n)            O(1)
def bottomProfit(prices: list[int]):
    min_buy = prices[0]
    max_sell = 0

    for stock in prices[1:]:
        max_sell = max(max_sell, stock - min_buy)
        min_buy = min(min_buy, stock)
    return max_sell
