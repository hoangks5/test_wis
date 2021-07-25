inp = int(input("Nhập số cần tính giai thừa: "))
 
def giaithua(inp):
    if inp == 0:
        return 1
    return inp * giaithua(inp - 1)
print (str(inp) + '! = ' + str(giaithua(inp)))