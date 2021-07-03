from math import sqrt
# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(n):
  if n == 1:
    return "Not prime"

  for i in range(2, int(sqrt(n) + 1)):
    if n % i == 0:
      return "Not prime"
  return "Prime"

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    n = int(input())
    print(isPrime(n))
