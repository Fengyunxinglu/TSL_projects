# Created with Python AI

"""
======================================
TSL-SYSTEM checkcode : Metasploit V1.0
======================================

本工具破解成功率:0.001%
Autor:XV101

探索实验室系统科技部版权所有©️

"""

import random

for i in range(20):
  checkcode = ''
  
  for i in range(6):
    index = random.randrange(0,9)
    if index != i and index + 1 != i:
      checkcode += chr(random.randint(97,122))
    elif index + 1 == i:
      checkcode += chr(random.randint(65,90))
    else:
      checkcode += str(random.randint(1,9))

  #print(checkcode)


  dic_list = ''

  for i in range(6):
      index = random.randrange(0,9)
      if index != i and index + 1 != i:
        dic_list += chr(random.randint(97,122))
      elif index + 1 == i:
        dic_list += chr(random.randint(65,90))
      else:
        dic_list += str(random.randint(1,9))

  def brokecode():
    for i in range(1):
      while dic_list == checkcode:
        print('True:',dic_list,',','True:',checkcode,'--> 破解成功！')
        break
      else:
        print('Wrong:',dic_list,',','True:',checkcode,'--> 破解失败！')

  for i in range(1):
    brokecode()

