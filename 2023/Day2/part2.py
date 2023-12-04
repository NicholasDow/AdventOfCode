import re

if __name__ == '__main__':
    constraints = {'blue':14,'green':13, 'red':12}
    
    total = 0
    with open('input.txt') as f:
        for line in f:
            flag = False
            games = line.split(':')
            max_cubes = {'blue':0, 'green':0,'red':0}
            for values in games[1].split(';'):
                for cubes in values.split(','):
                    num = int(re.findall('\d+',cubes)[0])
                    color = re.findall('[A-Za-z]+',cubes)[0]
                    if constraints[color] < num:
                        flag = True
                    max_cubes[color] = max(max_cubes[color], num)
            total += max_cubes['blue'] * max_cubes['green'] * max_cubes['red']
    print(total)