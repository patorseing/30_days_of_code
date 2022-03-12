# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = gets

# Print a string literal saying "Hello, World." to stdout.
puts 'Hello, World.'

# TODO: Write a line of code here that prints the contents of input_string to stdout.
puts input_string

require "rspec/autorun"

class Solution
  # Initializes with the number of dice to use.
  #
  # @param str [String] the number of dice to use
  def initialize(str = '')
    @str = str
  end
  # Rolls all the dice and returns the total rolled.
  #
  # @return [String] containing the total rolled.
  def concat
    return 'Hello, World. ' + "\n" + @str
  end

end

describe Solution, ".concat" do
  it "it returns random total within expected range" do
    result = Solution.new('Welcome to 30 Days of Code!').concat
    expect(result).to eq("Hello, World. \nWelcome to 30 Days of Code!")
  end
end

input_string = gets
puts Solution.new(input_string).concat
