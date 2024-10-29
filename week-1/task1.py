x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

xh = x1
yh = y2
xl = x2
yl = y1
string = ""
if y <= yh and y >= yl and x > xh:
    string = "E"
elif y <= yh and y >= yl and x < xl:
    string = "W"
elif x >= xh and x <= xl and y > yh:
    string = "N"
elif x >= xh and x <= xl and y < yh:
    string = "S"
elif y < yl and x > xl:
    string = "SE"
elif y < yl and x < xl:
    string = "SW"
elif y > yl and x < xl:
    string = "NW"
elif y > yl and x > xl:
    string = "NE"
print(string)
