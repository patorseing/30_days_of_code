require "rspec/autorun"

$i = 4
$d = 4.0
$s = 'HackerRank '

class Solution

  def initialize(str, double, integer)
    @str = str
    @double = double
    @integer = integer
  end

  def concat
    return $s + @str
  end

  def plusInt
    return $i + @integer
  end

  def plusFloat
    return $d + @double
  end

end

describe Solution, ".plusInt" do
  it "it returns random total within expected range" do
    result = Solution.new('is the best place to learn and practice coding!', 4.0, 12).plusInt
    expect(result).to eq(16)
  end
end

describe Solution, ".plusFloat" do
  it "it returns random total within expected range" do
    result = Solution.new('is the best place to learn and practice coding!', 4.0, 12).plusFloat
    expect(result).to eq(8.0)
  end
end

describe Solution, ".concat" do
  it "it returns random total within expected range" do
    result = Solution.new('is the best place to learn and practice coding!', 4.0, 12).concat
    expect(result).to eq("HackerRank is the best place to learn and practice coding!")
  end
end

# Declare second integer, double, and String variables.
i_in = readline.to_i
d_in = readline.to_f
s_in = readline

# Print the sum of both integer variables on a new line.
puts Solution.new(s_in, d_in, i_in).plusInt

# Print the sum of the double variables on a new line.
puts Solution.new(s_in, d_in, i_in).plusFloat

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
puts Solution.new(s_in, d_in, i_in).concat
