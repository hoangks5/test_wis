string_tetx = input("Nhập vào chuỗi: ")
env_string = string_tetx[::-1]
if env_string == string_tetx:
  print(string_tetx + " là chuỗi palindrome")
else:
  print(string_tetx + " không phải là chuỗi palindrome")

