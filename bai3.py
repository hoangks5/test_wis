def __number__(n):
  step = 0
  for i in range(2, n):
    if n % i == 0:
      print(str(n)+ " không phải là số nguyên tố")
      break
    else:
      print(str(n)+ " là số nguyên tố")
      break
n = int(input("Nhập số cần kiểm tra: "))
__number__(n)