inp = input("Nhập vào dãy số: ")
inp.split(',')
string = ''
for i in inp.split(','):
  if int(i, 2) % 5 == 0:
    string +=  str(i)+','
print(string[:-1])