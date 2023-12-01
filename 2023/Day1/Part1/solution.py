import re
def main():
    total = 0
    with open('input.txt') as f:
        for line in f:
            nums = re.findall('\d',line)
            new_digit = int(nums[0] + nums[-1])
            total+= new_digit
    print(total)


if __name__ == "__main__":
    main()