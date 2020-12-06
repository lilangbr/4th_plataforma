def accepted_values(char):
    list_values = [' ','0','1','2','3','4','5','6','7','8','9'] 
    if char in list_values:
        return 1
    else:
        return 0

def convert_str_list(s):
    list_lake = list(s)
    list_new = []
    previous = 0
    not_blank = 0
    for element in list_lake:
        if accepted_values(element): 
            if element != ' ':
                not_blank = 1
                previous = previous*10 + int(element)
            else:
                not_blank = 0
                list_new.append(previous)
                previous = 0
        else:
            list_new.append(1000)
    if not_blank:
        list_new.append(previous)

    return list_new

