def start_liangs_algorithm():
    process_words()


def process_words():
    with open('liangs_algorithm/liang_pattern.txt') as f:
        patterns = [word for line in f for word in line.split()]

    with open('liangs_algorithm/liang_word_list.txt') as f1:
        words = [word for line in f1 for word in line.split()]

    for word in words:
        final_dict = {}

        for pattern in patterns:
            pattern_without = ''.join(c for c in pattern if not c.isdigit())
            pattern_dot_index = pattern_without.find('.')
            pattern_without_dot = pattern_without.replace('.', '')
            pattern_with_num_without_dot = pattern.replace('.', '')
            found_index = False

            if pattern_dot_index != -1:
                if pattern_dot_index == 0:
                    found_index = word.startswith(pattern_without_dot)
                else:
                    found_index = word.endswith(pattern_without_dot)
            else:
                found = word.find(pattern_without_dot)
                if found != -1:
                    found_index = True

            if found_index:
                pattern_index = word.find(pattern_without_dot)

                for idx, letter in enumerate(pattern_with_num_without_dot):
                    if letter.isdigit():
                        index_to_add = 0
                        numbers_to_add = ''

                        if pattern_with_num_without_dot.startswith(letter):
                            index_to_add = pattern_index-1
                            numbers_to_add = letter
                            # print(pattern_with_num_without_dot)
                        elif pattern_with_num_without_dot.endswith(letter):
                            index_to_add = pattern_index + len(pattern_without_dot) - 1
                            numbers_to_add = letter
                            # print(pattern_with_num_without_dot)
                        else:
                            search_string = pattern_with_num_without_dot[idx-1] + pattern_with_num_without_dot[idx+1]
                            search_string_index = word.find(search_string, pattern_index)
                            index_to_add = search_string_index
                            numbers_to_add = letter
                            # print(pattern_with_num_without_dot)

                        if str(index_to_add) in final_dict:
                            if final_dict[str(index_to_add)] < int(numbers_to_add):
                                final_dict[str(index_to_add)] = int(numbers_to_add)
                        else:
                            final_dict[str(index_to_add)] = int(numbers_to_add)

        # print(final_dict)

        final_word = []
        for idx, value in enumerate(word):
            final_word.append(value)
            if str(idx) in final_dict:
                if is_odd(final_dict[str(idx)]):
                    final_word.append('-')

        print(''.join([str(x) for x in final_word]))

    print('Finished')


def is_odd(num):
    return num & 0x1
