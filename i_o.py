def get_number(msg):
    is_num = False
    while not is_num:
        result = input(msg)
        if result.isdigit():
            is_num = True
    return int(result)

def get_str(msg):
    is_valid_str = False
    while not is_valid_str:
        result = input(msg).strip()
        if result.isalpha():
            is_valid_str = True
    return result.lower()


