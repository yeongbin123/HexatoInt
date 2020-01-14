from bitstring import Bits

file_name = input('Input a file name : ')

try:
  inf = open(file_name,'r',encoding='UTF8')
except IOError as e:
  print("IOError: {0}".format(e))

try:
  f = open("output.txt",'w')
except IOError as e:
  print("IOError: {0}".format(e))

res = inf.readlines()

new = ""
new = "".join(map(str, res))
res = new.split()

res_list = []

for i in range(len(res)):
  res_list.append(res[i][:4])
  res_list.append(res[i][4:])

flag = 0

for i in range(0,len(res_list),2):
  num1 = Bits(hex = res_list[i])
  if num1.int >= 0 :
    flag = 1 
  num2 = Bits(hex = res_list[i + 1])
  num1 = str(num1.int)
  num2 = str(num2.int)
  if flag:
    result = num2+"+"+num1+"i"
    print(result, file=f)
  else:
    result = num2+num1+"i"
    print(result, file=f)
  flag = 0

inf.close()
f.close()
