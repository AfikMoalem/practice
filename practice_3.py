#3
Str1 = str('abcdefghijklmnopqrstuvwxyz')
Str2 = str('012123234345456567678789')
Str3 = str('010203040506070809')
Str4 = []

Str4.append(Str1[1:-1])
Str4.append(Str1[1::3])
Str4.append(Str3[-2::-2])


print(Str4)