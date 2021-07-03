# Enter your code here. Read input from STDIN. Print output to STDOUT
def CalculateFin(returned, due):
    fine = 0
    # year
    if due[2] < returned[2]:
        fine = 10000
    # month
    elif due[2] == returned[2]:
        if due[1] < returned[1]:
            fine = 500 * (returned[1] - due[1])
        # day
        elif due[2] == returned[2] and due[1] == returned[1] and due[0] < returned[0]:
            fine = 15 * (returned[0] - due[0])

    return fine


if __name__ == "__main__":
    date1 = input().split()
    date2 = input().split()
    print(CalculateFin(list(map(int, date1)), list(map(int, date2))))
