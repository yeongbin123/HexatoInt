"""
File Name   : Int_to_Hexa.py
"""

import numpy, random
import sys

def get_hex(value, fmt="{:04x}"):
   if value < 0:
      c = 2**16 + value
      #c = c * 0.1
   else:
      c = value
   return fmt.format(c.astype(int))

def dump_coe(filename, x):
   with open(filename, "w") as f:
      # f.write("; Hex equivalent of test input for FFT 32\n")
      # f.write("memory_initialization_radix=16;\n")
      # f.write("memory_initialization_vector=\n")
      for val in x[:-1]:
         dr = get_hex(val.real*(2**8))
         di = get_hex(val.imag*(2**8))
         dr = dr[:4]
         f.write(di+dr+"\n")
      val = x[-1]
      dr = get_hex(val.real*(2**8))
      dr = dr[:4]
      di = get_hex(val.imag*(2**8))
      f.write(di+dr+"\n")
'''
def dump_mem(filename, x):
   with open(filename, "w") as f:
      for val in x:
         dr = get_hex(val.real*(2**8))
         di = get_hex(val.imag*(2**8))
         f.write(di+dr+"\n")
'''
if __name__ == "__main__" :
   
   # N = int(sys.argv[1])
   file_name = input('Input a file name : ')
   inf = open(file_name,'r',encoding='UTF8') 
   res = inf.read()
   # numpy.random.seed(0)   # start from known state
   #data = numpy.array([(numpy.random.randn()+1j*numpy.random.randn()) for i in range(N)])
   new = ""
   '''
   for i in range(len(res)):
      for j in res[i]:
          print(j)
   '''
   new = "".join(map(str, res))
   #print(new)
   res = new.split()
   #print(res)

   data = numpy.array([complex(float(res[i])) for i in range(len(res))])
   result = numpy.fft.fft(data)

   #numpy.savetxt("inp_cpp.txt", data, fmt = "%f %f")
   #numpy.savetxt("out_cpp.txt", result, fmt = "%f %f")

   dump_coe("inp_hex.mem", data)
   dump_coe("out_hex.mem", result) # apply fft
