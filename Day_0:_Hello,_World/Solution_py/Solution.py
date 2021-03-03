def concat (input_string):
  # Print a string literal saying "Hello, World." to stdout.
  # print('Hello, World.')

  # TODO: Write a line of code here that prints the contents of input_string to stdout.
  # print(input_string)
  return 'Hello, World. ' + '\n' + input_string

if __name__ == "__main__":
  # Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
  input_string = input()
  print(concat(input_string))
