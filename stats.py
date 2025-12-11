def get_num_words(text):
    return len(text.split())

def char_count(text):
    txt = text.lower()

    char_dict = {}

    for letter in txt:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1

    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_of_dicts = []

    for i in dict:
        if i.isalpha():
            list_of_dicts.append({
                "char": i,
                "num": dict[i]
            })

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts