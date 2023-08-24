# https://stackoverflow.com/questions/12399803/how-to-check-if-a-key-in-kwargs-exists
# https://itecnote.com/tecnote/python-how-to-check-if-a-key-in-kwargs-exists/
def my_print(*args, **kwargs):
  #print(*args, **kwargs)
  #print( dir(kwargs))

  print(kwargs)

  if 'test' in kwargs:
    print("found")
    print("kwargs test:", kwargs.get('test'))

def main():
  my_print(test="testme")

if __name__ == '__main__':
  main()