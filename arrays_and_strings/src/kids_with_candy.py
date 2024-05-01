#STATS
#   Runtime         Memory
#   O(n) beats 52%  O(n) beats 12%
# Kids With Greatest Number of Candies #1431
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    #find local max
    local_max = 0
    for candy in candies:
        if candy > local_max:
            local_max = candy
    most_candy = []

    for candy in candies:
        candy += extraCandies
        if candy >= local_max:
            most_candy.append(True)
        else:
            most_candy.append(False)
    return most_candy
