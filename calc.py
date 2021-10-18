class Calculator:
  def __init__(self,numb_1,numb_2):
    self.numb_1 = numb_1
    self.numb_2 = numb_2

  def addition(self):
    return self.numb_1 + self.numb_2
  def subtraction(self):
    return self.numb_1 - self.numb_2
  def multiplication(self):
    return self.numb_1 * self.numb_2
  def division(self):
    return self.numb_1 // self.numb_2    

numb= Calculator(20,20)

print(f'Value--->>>> {numb.addition()}')
print(f'Value--->>>> {numb.subtraction()}')
print(f'Value--->>>> {numb.multiplication()}')
print(f'Value--->>>> {numb.division()}')
