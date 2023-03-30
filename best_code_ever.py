def multiple_of(number, num):
    if number % num == 0:
        return True
    else:
        return False

def is_even(number):
    return multiple_of(number, 2)

def complex_algo(songs:list):
    why_not = []
    sure = []
    num_list = []
    val_dict = {}
    for song in songs:
        val = 0
        average = ((1/65)+(1/122))/2
        for i in song:
            if i.isdigit():
                num_list.append(song)
                why_not.append(song)
            val += (1/ord(i))
        val_dict[song] = val
        ord_value = ord(song[0])
        for j in range(5, 10, 2):
            if multiple_of(ord_value, j):
                for k in range(3, 8, 2):
                    if k != j:
                        if multiple_of(ord_value, k):
                            if is_even(ord_value) and not multiple_of(ord_value, 10):
                                why_not.append(song)
    if why_not:
        if len(num_list) == 1:
            item = num_list[0]
            if item in val_dict.keys():
                print(item, val_dict[item])
                if val_dict[item] > average:
                    sure.append(song)
        elif is_even(len(item)):
            sure.append(item)

    if sure:
        return f"Sure: {item}"
    return "Nope"

liste = ["Black & Mortimer", "Tricheur", "Je t'aime", "Numéro Deep", "Rei", "Salem Witch", "Everyday Normal Guy 2", "Mégadose", "Je vous aime"]
print(complex_algo(liste))