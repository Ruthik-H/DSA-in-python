#adding two binary numbers
a = "11"
b = "1"
c=int(a,2)+int(b,2) # 2 as base the python syntax will be int(number,base) so for 11 it becomes as 1X2^1+1X2^o =3
print(bin(c)[2:]) #so here bin(c) gives soemthing like 0b100 so to remove "ob" we use [2:] to get the values from indx 2