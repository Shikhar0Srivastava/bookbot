def get_text_length(file_contents):
    return len(file_contents.split())

def get_char_dict(file_contents):
    char_dict = {}
    file_contents = file_contents.lower()
    for c in file_contents:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    
    return char_dict

def sort_char_dict(char_dict):
    values = []
    for i in char_dict:
        new_dict = {}
        new_dict["char"] = i
        new_dict["num"] = char_dict[i]
        values.append(new_dict)
    values.sort(reverse=True, key=sort_on)
    return values

def sort_on(values: tuple[str, int]) -> int:
    return values[1]

def chars_dict_to_sorted_list(chars: dict[str, int]) -> list[tuple[str, int]]:
    tuples = []
    for key in chars:
        tuples.append((key, chars[key]))
    sorted_tuples = sorted(tuples, reverse=True, key=sort_on)
    return sorted_tuples