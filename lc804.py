def solve(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    resSet = set()
    for s in words:
        res = ""
        for c in s:
            res += morse[ord(c) - 97]
        resSet.add(res)
    return len(resSet)


tc = ["gin", "zen", "gig", "msg", "a"]
print(solve(tc))
