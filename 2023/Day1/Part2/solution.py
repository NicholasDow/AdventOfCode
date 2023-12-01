# import re
import regex as re
def fix_number(s):
    translate = {'one':'1', 'two':'2', 'three':'3', 'four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    if s in translate.keys():
        return translate[s]
    else:
        return s

def main():
    total = 0
    
    with open('input.txt') as f:
        #fuck, I did not see this coming overlapped=True to fix 
        for line in f:
            nums = re.findall('\d|one|two|three|four|five|six|seven|eight|nine',line,overlapped=True)
            
            new_digit = int(fix_number(nums[0]) + fix_number(nums[-1]))
            total+= new_digit
    print(total)


if __name__ == "__main__":
    main()