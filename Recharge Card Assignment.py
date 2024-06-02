#Generate recharge card
recharge_card = ""
n = int(input("Input a number with an even number of length: "))
for i in range(4):
    n_str = str(n)
    if len(n_str)%2 == 1:
        while len(n_str)%2 != 0:
            print('You should input a number of even number of length')
            n = int(input("Input a number with an even number of length: "))
            n_str = str(n)
    n_square = n * n
    str_n_square = str(n_square) #string of square
    if len(str_n_square) != 2 * len(n_str):
        b = 2 * len(n_str)
        str_n_square = "0" + str_n_square
        c = len(n_str)/2
        d = len(str_n_square) - c
        int_c = int(c)
        int_d = int(d)
        ans = str_n_square[int_c:int_d]
        print(ans)
    else:
        c = len(n_str)/2
        d = len(str_n_square) - c
        int_c = int(c)
        int_d = int(d)
        ans = str_n_square[int_c:int_d]
        print(ans)
    recharge_card = recharge_card + str(ans)
    n = int(ans)
print(recharge_card)


