import random
import time


def minigame():
  s = random.randint(999,10000)
  inp = 0
  print('Chào mừng đến với trò chơi Cows and Bulls')
  while int(inp) != s:
    cout = 0
    inp = int(input("Nhập vào con số bạn dự đoán: "))
    for i in range(0,4):
      if str(inp)[i] == str(s)[i]:
        cout += 1
    print(str(cout)+'Cows, '+str(int(4-cout))+' Bulls')
  print('Con số cần tìm là: '+str(s))
minigame()