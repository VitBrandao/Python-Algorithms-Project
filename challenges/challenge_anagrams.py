def order_string(string):
    string_list = list(string)
    str_len = len(string)

    for index in range(1, str_len):
        key = string_list[index]
        new_position = index - 1

        while new_position >= 0 and string_list[new_position] > key:
            string_list[new_position + 1] = string_list[new_position]
            new_position = new_position - 1

        string_list[new_position + 1] = key

    return string_list


def is_anagram(first_string, second_string):
    low_first_string = first_string.lower()
    low_second_string = second_string.lower()

    order_first = order_string(low_first_string)
    order_second = order_string(low_second_string)

    return order_first == order_second


# print(is_anagram('Amor', 'rOmA'))
