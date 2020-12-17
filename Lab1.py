# Task 3.1
print("Task 3.1")
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT.replace('Fast', 'Gigabit'))

# Task 3.2
print("\nTask 3.2")
MAC = 'AAAA:BBBB:CCCC'
print(MAC.replace(':', '.'))

# Task 3.3
print("\nTask 3.3")
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
array = CONFIG.split()
print(array[-1].split(','))

# Task 3.4
print("\nTask 3.4")
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
command1 = command1.strip().split()
command2 = command2.strip().split()
vlan1 = command1[-1].split(',')
vlan2 = command2[-1].split(',')
vlan1 = set(vlan1)
vlan2 = set(vlan2)
print(list(vlan1 & vlan2))

# Task 3.5
print("\nTask 3.5")
vlans = '10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10'
vlansList = list(set((vlans).split(','))).sort()

# Task 3.6
print("\nTask 3.6")
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
rezult = """ 
Protocol: 		OSPF
Prefix: 		10.0.24.0/24
AD/Metrix: 		110/41
Next-Hop: 		10.0.13.3
Last update: 	3d18h
Outbound: 		Interface: FastEthernet0/0 """
print(rezult)

# Task 3.7
print("\nTask 3.7")
MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(":","")
MAC = int(MAC, 16)
MAC = bin(MAC)
print(MAC)

# Task 3.8
print("\nTask 3.8")
IP = '192.168.3.1'
ip_temple = """{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b} """
print(ip_temple.format(192,168,3,1))

# Task 3.9
print("\nTask 3.9")
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
print(num_list)
num_list.reverse()
var1 = input('Your value = ')
var1 = int(var1)
index = num_list.index(var1)
print('Last index {}'.format(len(num_list)-index))
print('_'*50)
print(word_list)
word_list.reverse()
var2 = input('Your word = ')
index = word_list.index(var2)
print('Last index{}'.format(len(word_list)-index))