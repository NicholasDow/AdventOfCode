import re

if __name__ == '__main__':
    constraints = {'blue':14,'green':13, 'red':12}
    total = 0
    with open('input.txt') as f:
        for line in f:
            flag = False
            games = line.split(':')
            for values in games[1].split(';'):
                for cubes in values.split(','):
                    num = re.findall('\d+',cubes)
                    color = re.findall('[A-Za-z]+',cubes)
                    if constraints[color[0]] < int(num[0]):
                        flag = True
            if not flag:
                total += int(re.findall('\d+',games[0])[0])
    print(total)
            
