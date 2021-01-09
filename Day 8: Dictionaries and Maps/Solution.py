# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
myMap = {}
for i in range(0,n):
  arg = input()
  arg = arg.split()
  myMap[arg[0]] = arg[1]

search = input()
while search != "":
  try:
    if search in myMap.keys():
      print(search+"="+myMap[search])
    else:
      print("Not found")
    search = input()
  except EOFError as e:
    search = ""
