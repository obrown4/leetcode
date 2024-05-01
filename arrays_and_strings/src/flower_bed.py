#STATS
#   Runtime         Memory
#   O(n) beats 34%  O(1) beats 73%
# Can Place Flowers #605
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    planted = True
    num_spaces = 1
    if flowerbed[0] == 1:
        num_spaces = 0
    for i in range(1, len(flowerbed)):
        if flowerbed[i] == 0 and not planted:
            num_spaces += 1
            planted = True
        elif flowerbed[i] == 1 and planted:
            num_spaces -= 1
        else:
            planted = not planted
    if num_spaces - n >= 0:
        return True
    return False
