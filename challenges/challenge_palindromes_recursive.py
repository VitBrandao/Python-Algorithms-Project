def is_palindrome_recursive(word, low_index, high_index):
    lower_word = word.lower()

    if (len(lower_word) == 0):
        return False
    elif (len(lower_word) == 1 or (len(lower_word) == 2 and lower_word[0] == lower_word[1])):
        return True
    else:
        if lower_word[low_index] == lower_word[high_index]:
            rest_of_the_word = lower_word[1:-1]
            new_higher_index = len(rest_of_the_word) - 1

            return is_palindrome_recursive(rest_of_the_word, 0, new_higher_index)
        else:
            return False


# word = 'Anana'
# print(is_palindrome_recursive(word, 0, len(word) - 1))

# O algoritmo deve ser feito utilizando a solução recursiva;

# Não se preocupe com a análise da complexidade desse algoritmo;

# Se for passado uma string vazia, retorne False;

