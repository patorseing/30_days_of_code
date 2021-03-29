def concat(input_string):
    # Print a string literal saying "Hello, World." to stdout.
    # print('Hello, World.')

    # TODO: Write a line of code here that prints the contents of input_string to stdout.
    # print(input_string)
    s = 'HackerRank '
    return s + input_string


def plusInt(input_int):
    i = 4
    return input_int + i


def plusFloat(input_float):
    d = 4.0
    return input_float + d


if __name__ == "__main__":
    # Declare second integer, double, and String variables.
    # Read and save an integer, double, and String to your variables.
    input_i = input()
    input_d = input()
    input_s = input()

    # Print the sum of both integer variables on a new line.
    print(plusInt(int(input_i)))

    # Print the sum of the double variables on a new line.
    print(plusFloat(float(input_d)))

    # Concatenate and print the String variables on a new line
    # The 's' variable above should be printed first.
    print(concat(input_s))
