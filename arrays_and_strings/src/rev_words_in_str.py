#STATS
#   Runtime         Memory
#   O(n) beats 98%  O(n) beats 80%

#Reverse Words in a String  #151
def reverseWords(s: str) -> str:
    res = s.split()
    begin = 0
    end = len(res) - 1

    while begin != end and end - begin > 0:
        swapWords(begin, end, res)
        begin += 1
        end -= 1
    res = ' '.join(res)
    return res

def swapWords(b: int, e: int, res: list):
    temp = res[b]
    res[b] = res[e]
    res[e] = temp
