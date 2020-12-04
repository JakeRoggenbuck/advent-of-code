class Line
  def initialize(raw_line)
    @raw_line = raw_line
    separate_vals()
  end
  def separate_vals()
    nums, letter, @password = @raw_line.split(" ")
    @letter = letter[0]
    first, second = nums.split("-")
    @first = first.to_i
    @second = second.to_i
  end
  def check()
    if @password[@first-1] == @letter and @password[@second-1] != @letter
      return true
    elsif @password[@first-1] != @letter and @password[@second-1] == @letter
      return true
    else
      return false
    end
  end
end

valid = 0
File.readlines("./input").each do |raw_line|
  line = Line.new(raw_line)
  if line.check()
    valid += 1
  end
end
puts valid
