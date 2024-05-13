#STATS
#   Runtime         Memory
#   O(n)            O(1)
# String Compression #443

def compress(chars: list[str]) -> int:
    curr = chars[0]
    char_count= 1
    to_place = 0

    if len(chars) == 1:
        return 1

    for i, char in enumerate(chars[1:], 1):
        if char != curr:
            chars[to_place] = curr
            to_place += 1
            if char_count> 1:
                appendDigit(char_count, to_place, chars)
                to_place += updatePlace(to_place, char_count)
            curr = char
            char_count= 1
        else:
            char_count+= 1

    chars[to_place] = curr
    to_place += 1
    if char_count> 1:
        appendDigit(char_count, to_place, chars)
        to_place += updatePlace(to_place, char_count)
    return to_place


def appendDigit(n: int, range: int, chars: list[str]):
    digit = str(n)

    for i, c in enumerate(digit):
        chars[range + i] = c

def updatePlace(to_place: int, char_count: int) -> int:
    if char_count< 10:
        return 1
    elif char_count< 100:
        return 2
    elif char_count< 1000:
        return 3
    else:
        return 4
