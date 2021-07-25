inp = int(input("Nhập vào số nguyên: "))
def dechexbin(inp):
  print("Chuyển sang BIN: " + bin(inp)[2:])
  print("Chuyển sang HEX: "+ hex(inp))
  print("Chuyển sang OCT: " + oct(inp))
dechexbin(inp)