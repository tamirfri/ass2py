def B():
  print("B.")
  for i in range(1, 6):
    print("iteration number", i)

def D():
  print("D.")
  count = 1
  while count < 11:
    print(count)
    count += 1
  print("last print and how many times:", 10)

def E():
  age = 29
  lname = 'F'
  currency = 3.51 # one dollar to shekels
  is_flew = True
  apart = 3
  print("E.")
  for key, val in locals().items():
    print(key, "=", val)
  age += currency
  print("new age =", age)

def K():
  print("K.")
  for i in range(1, 6):
    print('#' * i)
  
def L():
  size = 7
  print("L.")
  line_indexes = tuple(range(size))
  for line in line_indexes:
    main_diag = (i-line==0 for i in line_indexes)
    anti_diag = (i+line==size-1 for i in line_indexes)
    print(''.join('#' if m or s else ' '
          for m,s in zip(main_diag, anti_diag)))

def M():
  def scan_number():
    return input("Please enter a number: ")
  def scan_sum_digits():
    return sum(map(int, scan_number()))
  print("M.")
  print(scan_sum_digits())

if __name__ == '__main__':
  B()
  D()
  E()
  K()
  L()
  M()
