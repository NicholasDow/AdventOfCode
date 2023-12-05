if __name__ == '__main__':
    inputs = [] 
    with open('input.txt') as f:
        for i, line in enumerate(f):
            inputs.append([])
            for j, val in enumerate(line):
                inputs[-1].append(val)
    not_symbols = ['0','1','2','3','4','5','6','7','8','9','.']
    valid_nums = []
    for line_num in range(len(inputs)):
        line = inputs[line_num]
        char_num = 0
        current_num = ''
        while char_num < len(inputs[0]):
            valid_num = False
            while char_num < len(inputs[0]) -1 and line[char_num] in ['0','1','2','3','4','5','6','7','8','9']:
                # we need to check above
                can_go_right = char_num < len(inputs[0]) -1
                can_go_left = char_num > 0
                if line_num > 0:
                    row_below = inputs[line_num-1]
                    if row_below[char_num] not in not_symbols:
                        valid_num = True
                    if can_go_left and row_below[char_num-1] not in not_symbols:
                        valid_num = True
                    if can_go_right and row_below[char_num+1] not in not_symbols:
                        valid_num = True
                
                if line_num < len(inputs)-1:
                    row_above = inputs[line_num+1]
                    if row_above[char_num] not in not_symbols:
                        valid_num = True
                    if can_go_left and row_above[char_num-1] not in not_symbols:
                        valid_num = True
                    if can_go_right and row_above[char_num+1] not in not_symbols:
                        valid_num = True
                
                if can_go_left and inputs[line_num][char_num-1] not in not_symbols:
                    valid_num = True
                if can_go_right and inputs[line_num][char_num+1] not in not_symbols:
                    valid_num = True
                current_num += line[char_num]
                char_num+=1
            if valid_num:
                valid_nums.append(current_num)
            current_num = ''
            char_num+=1
    print(valid_nums)
    print(sum([int(num) for num in valid_nums]))