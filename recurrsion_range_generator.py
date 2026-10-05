def range_of_numbers(start_num, end_num):
    if end_num < start_num:
        return []
    
    num_list = range_of_numbers(start_num, end_num - 1)
    num_list.append(end_num)
    return num_list

print(range_of_numbers(1, 9))