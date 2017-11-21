# Tuple
nama_pahlawan = ('Mohammad Yasin', 'I Gusti Ngurah Made Agung',
  'Jamin Ginting', 'Lambertus Nicodemus Palar', 'Idham Chalid', 'Mas Isman')

for x in nama_pahlawan:
  print x

# Tuple Items
orang = { 'nama' : 'Guido van Rossum',
  'umur' : 60,
  'kewarganegaraan': 'Belanda',
  'tempat tinggal': 'Amerika' }

print orang.items()

for key, item in orang.items():
	print "{}: {}".format(key, item)

# Range
kubik = [a**2 for a in range (1, 11) if a % 2 == 1 and a % 5 != 0]

print kubik


