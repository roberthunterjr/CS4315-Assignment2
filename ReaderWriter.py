import sys

class Reader:
  def __init__(self,path):
    self.data = []
    self.path = path
  def read(self):
    with open(self.path, 'rb') as txtfile:
      for line in txtfile:
        newline = line.rstrip().split(' ')
        self.data.append(newline)
    return self.data


class Writer:
  def __init__(self, path):
    self.path = path
  def write(self, data):
    file = open(self.path, 'w')
    for line in data:
      file.write(' '.join(line)+'\n')
    file.close()

# lines = Reader('./input.txt').read()
# print(lines)
# output = Writer('output.txt').write(lines)
# print(sys.argv)