tunnel = """ 
Protocol:{}Prefix:{}AD/Metrix: {}Next-Hop:{}Last update:{}Outbound: {}
		"""

with open('ospf.txt', 'r') as f:
    for line in f:
        a = line.split('\n')[0].replace(',','').replace('[','').replace(']','').replace('O','OSPF').split()
        a.remove('via')
        Protocol,Prefix,Metrix,Next,update,outbound = a
        print(tunnel.format(Protocol,Prefix,Metrix,Next,update,outbound))
        #
with open('config_sw1.txt','r') as f:
    for line in f:
        if not '!' in line and not '\n' == line[0]:
            print(line[:-1])
            #
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
            #
ignore = ['duplex', 'alias', 'Current configuration']
with open('config_sw1.txt','r') as f:
    for line in f:
        Ku = True
        for i in range(3):
            if ignore[i] in line:
                Ku = False
                break
        if not '!' in line and not '\n' == line[0] and Ku:
            print(line[:-1])