#! /usr/bin/env python3

numbers = 4
target = 24
threshold = .0000001

class chunk(object):
  def __init__(self, number, text = None):
    self.total = number
    if text is None:
      self.text = str(number)
    else:
      self.text = text

  # For sorting
  def __lt__(self, other):
    return self.total < other.total

  def __eq__(self, other):
    return self.text == other.text

  def __hash__(self):
    return hash(self.text)

  def __str__(self):
    return self.text


def add(a, b):
  newTotal = a.total + b.total
  newText = "(" + a.text + " + " + b.text + ")"
  return chunk(newTotal, newText)
  
def multiply(a, b):
  newTotal = a.total * b.total
  newText = "(" + a.text + " * " + b.text + ")"
  return chunk(newTotal, newText)

def subtract(a, b):
  newTotal = a.total - b.total
  newText = "(" + a.text + " - " + b.text + ")"
  return chunk(newTotal, newText)
  
def divide(a, b):
  newTotal = a.total / b.total
  newText = "(" + a.text + " / " + b.text + ")"
  return chunk(newTotal, newText)   
    
operations = [add, multiply, subtract, divide]



def operate(chunks, open):

  # Some divisions will not return integers, but let's assume that's okay.
  if len(chunks) == 1:
    # All compressed down to one chunk
    if (chunks[0].total - target < threshold) and \
       (target - chunks[0].total < threshold):
      # print(chunks[0])
      return chunks[0]

  else:
  # Some chunks still remain
    for chunk1 in chunks:
      chunksM1 = list(chunks) # Makes a copy
      chunksM1.remove(chunk1)
      for chunk2 in chunksM1:
        chunksM2 = chunksM1.copy()
        chunksM2.remove(chunk2)
        for operation in operations:
          try:
            newChunk = operation(chunk1, chunk2)
          except ZeroDivisionError:
            pass # Nothing specific to do; just don't make the recursive call.
          else:
            newChunks = chunksM2.copy()
            newChunks.append(newChunk)
            newChunks.sort() # Should be O(n) because it was already sorted
            open.add(tuple(newChunks))

  # return chunks[0]


def number_input(prompt):
  num = input(prompt)
  try:
    return int(num)
  except:
    return number_input("Not a valid number. Try again: ")
      

def solve(numbers):
  operations = (add, multiply, subtract, divide)
  closed = set()
  open = set()
  initial = []

  for number in sorted(list(numbers)):
    initial.append(chunk(int(number)))
  initial.sort()
  open.add(tuple(initial))

  # Execute the solution search
  results = []
  while len(open) > 0:
    #TODO remove debugging line input("open: {} closed: {}".format(len(open), len(closed)))
    chunks = open.pop()
    if chunks not in closed:
      result = operate(chunks, open)
      if result is not None:
        results.append(result)
    closed.add(chunks)

  return results


def fake_random():
  import numpy as np
  from IPython.display import clear_output, display, Markdown
  from time import sleep
  
  for i in range(40):
      question = np.random.randint(10, size=4)
      clear_output()
      question = ' '.join(map(str, question))
      display(Markdown('<center><h1 style=font-size:140px>Game 24<br>{}</center></h1>'.format(question)))
      sleep(0.05)


def get_question():
  import numpy as np
  from IPython.display import clear_output, display, Markdown
  from time import sleep

  fake_random()

  question = np.random.randint(10, size=4)
  answers = solve(question)
  
  while(len(answers) == 0 or len(answers) != 4):
      question = np.random.randint(10, size=4)
      answers = solve(question)
      clear_output()
      question = ' '.join(map(str, question))
      display(Markdown('<center><h1 style=font-size:140px>Game 24<br>{}</center></h1>'.format(question)))
      sleep(0.2)

  return answers
      

def display(answers):
  from IPython.display import clear_output, display, Markdown
  display(Markdown('<center><h1 style=font-size:55px>Answers<br></center></h1>'))
  for answer in answers:
    display(Markdown('<center><h1 style=font-size:40px>{}<br></center></h1>'.format(answer)))

if __name__ == "__main__":
  import numpy as np
  # numbers = np.random.randint(10, size=4)
  numbers = np.array([5,6,0,3])
  answers = solve(numbers)
  for answer in answers:
    print(answer)
  # Get the user input and initialize things
  # operations = (add, multiply, subtract, divide)
  # closed = set()
  # open = set()
  # initial = []
  # for i in range(numbers):
  #   initial.append(chunk(number_input("Enter a puzzle number: ")))
  # initial.sort()

  # open.add(tuple(initial))

  # # Execute the solution search
  # while len(open) > 0:
  #   #TODO remove debugging line input("open: {} closed: {}".format(len(open), len(closed)))
  #   chunks = open.pop()
  #   if chunks not in closed:
  #     operate(chunks)
  #   closed.add(chunks)
