# aoc_day2_p2.py
def get_common_letters_for_box_ids():
    import copy
    result = ''

    file_name = 'aoc_day2_pt1_input.txt'

    with open(file_name) as file_obj:
        content = file_obj.readlines()

    copied_content = copy.copy(content)

    first_box_id = None
    second_box_id = None
    for line in content:
        for copied_line in copied_content:
            count = sum(1 for a,b in zip(line, copied_line) if a != b)
            
            if count == 1:
                second_box_id = copied_line
                break
        
        if second_box_id:
            first_box_id = line
            break

    if first_box_id and second_box_id:
        result = ''.join(a for a,b in zip(first_box_id, second_box_id) if a == b)

    return result

def main():
    target = get_common_letters_for_box_ids()
    print 'Common letters for box ids are {}'.format(target)

if __name__ == '__main__':
    main()