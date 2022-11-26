import os
import numpy as np

try:
  # Array of value.
  values = []

  print('**************************INPUTS**************************')
  num_1 = int(input('Enter 1st number : '))
  values.append(num_1)

  num_2 = int(input('Enter 2nd number : '))
  values.append(num_2)

  num_3 = int(input('Enter 3rd number : '))
  values.append(num_3)

  num_4 = int(input('Enter 4th number : '))
  values.append(num_4)

  num_5 = int(input('Enter 5th number : '))
  values.append(num_5)

  # Clear terminal after entering the values.
  os.system('cls||clear')

  print('\n')
  print('**************************OUTPUTS**************************')
  print('Values           : ', values)
  print('Mean             : ', np.mean(values))
  print('Median           : ', np.median(values))
  print('25th Percentile  : ', np.percentile(values, 25))
  print('50th Percentile  : ', np.percentile(values, 50))
  print('75th Percentile  : ', np.percentile(values, 75))
  print('\n')
except:
  print('Only numbers are allowed.')
