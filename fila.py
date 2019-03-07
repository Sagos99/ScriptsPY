pos_real = [0,1,2,3,4,5]
pos_virtual = []

dif = 3

show = 2

for item in pos_real:
	pos_virtual.append(pos_real[item]+dif)

print("\nPosição real: %s" % (pos_real[show]))
print("Posição virtual: %s\n" % (pos_virtual[show]))