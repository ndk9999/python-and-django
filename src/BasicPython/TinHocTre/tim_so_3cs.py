so = 0
dem = 0

for tram in range(1, 10):
	for chuc in range(0, 10):
		for dv in range(1, 10):
			tong = tram + chuc + dv
			if dv % 2 == 1 and tram % 2 == 1 and chuc % 2 == 0 and tong % 6 == 0:
				so = tram * 100 + chuc * 10 + dv
				print(so)
				dem += 1

if dem == 0:
	print(0)
