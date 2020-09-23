a=True
print(type(a))

a=70

if a >= 80:
    print("pass")
else:
    print("not")

if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else:
    print("점수아님")

a=11

if 13 <= a <= 18:
    print("1300")

j="901223-4234567"

if j[j.index("-") + 1] == "1" or j[j.index("-") + 1] == "3":
    print("남")
else:
    print("여")