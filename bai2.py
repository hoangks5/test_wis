def string():
  inp = int(input("Tạo chuỗi Fibonacci có bao nhiêu số: "))
  if inp == 1:
    string_a = [1]
  if inp ==2:
    string_a = [1,1]
  else:
    string_a = [1,1]
    for i in range(inp-2):
      next_number = string_a[-1] + string_a[-2]
      string_a.append(next_number)
  print(string_a)
string()