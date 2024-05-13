#STATS
#   Runtime         Memory
#   O(n) beats 60%  O(n) beats 87%

#Reverse Vowels of a String #345
def reverseVowels(s: str) -> str:
    begin = 0
    end = len(s) - 1
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    res = list(s)

    while begin != end and end - begin > 0:
        if res[begin] in vowels and res[end] in vowels:
            swapChars(begin, end, res)
            begin += 1
            end -= 1
        elif res[begin] not in vowels and res[end] not in vowels:
            begin += 1
            end -= 1
        elif res[begin] not in vowels:
            begin += 1
        else:
            end -= 1

    res = ''.join(res)
    return res

def swapChars(b: int, e: int, r: list):
    temp = r[b]
    r[b] = r[e]
    r[e] = temp
