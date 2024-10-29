b_shirt = int(input())
r_shirt = int(input())
b_socks = int(input())
r_socks = int(input())

min_with_red_socks = b_socks + 1
min_with_blue_socks = r_socks + 1

min_with_red_shirts = b_shirt + 1
min_with_blue_shirts = r_shirt + 1

min_both_socks = max(b_socks, r_socks) + 1
min_both_shirts = max(b_shirt, r_shirt) + 1

red = min_with_red_socks + min_with_red_shirts
blue = min_with_blue_socks + min_with_blue_shirts
socks = min_both_socks + 1
shirts = min_both_shirts + 1

minimized_value = min(red, blue, socks, shirts)
if b_socks == 0:
    print(b_shirt+1, 1)
elif r_socks == 0:
    print(r_shirt+1, 1)
elif b_shirt == 0:
    print(1, b_socks+1)
elif r_shirt == 0:
    print(1, r_socks+1)
elif red == minimized_value:
    print(min_with_red_shirts, min_with_red_socks)
elif blue == minimized_value:
    print(min_with_blue_shirts, min_with_blue_socks)
elif socks == minimized_value:
    print(1, min_both_socks)
elif shirts == minimized_value:
    print(min_both_shirts, 1)
