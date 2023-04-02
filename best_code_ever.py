from math import pi, sqrt
from numpy import log as ln
from numpy import rad2deg

def multiple_of(number: int, num: int) -> bool:
    if number % num == 0:
        return True
    else:
        return False

def is_even(number: int):
    return multiple_of(number, 2)

def vowel_num(word: str) -> int:
    count = 0
    vowels = ("a", "e", "i", "o", "u", "y")
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

def following_letters(word: str) -> bool:
    for i in range(1, len(word)-1):
        prev = word[i-1]
        if prev == word[i]:
            return True
    return False

def complex_algo(songs: list[str]):
    why_not = []
    num_list = []
    val_dict = {}
    for song in songs:
        # blessed letters
        ord_value = ord(song[0])
        for i in range(5, 10, 2):
            if multiple_of(ord_value, i):
                for j in range(3, 8, 2):
                    if j != i:
                        if multiple_of(ord_value, j):
                            if is_even(ord_value) and not multiple_of(ord_value, 10):
                                why_not.append(song)
        # number = good
        val = 0
        average = ((1/65)+(1/122))/2
        for k in song:
            if k.isdigit():
                num_list.append(song)
                why_not.append(song)
            val += (1/ord(k))
        if val > average:
            val_dict[song] = val
        # blessed chars
        chars = ("&", "!", "?", "~", "/")
        for l in song:
            if l in chars:
                why_not.append(song)
                val_dict[song] += 1/sqrt(ord(l))
        # maths
        if vowel_num(song) == int(rad2deg(ln(len(song)) / pi) / 10):
            why_not.append(song)
        # letters
        if following_letters(song):
            why_not.append(song)

    if why_not:
        higher = 0
        for m in val_dict.keys():
            item = val_dict[m]
            if item > higher:
                higher = item
        why_not.append(list(val_dict.keys())[list(val_dict.values()).index(higher)])
        weight = {}
        for i in why_not:
            count = why_not.count(i)
            if count > 1:
                weight[i] = count
    weight_values = list(weight.values())
    weight_sorted = []
    for n in weight_values:
        weight_sorted.append(n)
    weight_sorted.sort()
    return list(weight.keys())[list(weight.values()).index(weight_sorted[-1])]

liste = ["ME / U", "You and You", "Burning Bright", "Exil", "LE SANG"]
print(complex_algo(liste))