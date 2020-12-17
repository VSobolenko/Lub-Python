ignore = ['duplex', 'alias', 'Current configuration']
f = open('config_sw1_cleared.txt','w')
with open('config_sw1.txt','r') as f, open('config_sw1_cleared.txt','w+') as d:
    for line in f:
        Ku = True
        for i in range(3):
            if ignore[i] in line:
                Ku = False
                break
        if not '\n' in line == line[0] and Ku:
            print(line[:-1])
            d.write(line)


