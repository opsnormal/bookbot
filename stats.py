#stats file for functions to be called in main

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def get_characters(text):
    char_dict = {}
    for ch in text.lower():
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    return char_dict

def sort_dict(char_dict):
    list_of_dicts = []
    for key, value in char_dict.items():
        list_of_dicts.append({"char": key, "num": value})

    def get_num(char_dict_item):
        return char_dict_item["num"]
    
    list_of_dicts.sort(key=get_num, reverse=True)
    return list_of_dicts

