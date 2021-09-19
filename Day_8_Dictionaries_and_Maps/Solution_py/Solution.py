# Enter your code here. Read input from STDIN. Print output to STDOUT
def search_phone_book(phone_book, name):
  result = ""
  if name in phone_book.keys():
    result = name+"="+str(phone_book[name])
  else:
    result = "Not found"
  return result

if __name__ == '__main__':
    n = int(input())
    myMap = {}
    for i in range(0, n):
        arg = input()
        arg = arg.split()
        myMap[arg[0]] = arg[1]

    search = input()
    while search != "":
        try:
            print(search_phone_book(myMap, search))
            search = input()
        except EOFError as e:
            search = ""
