class Pointer
  def initialize(start_x, start_y)
    @x = start_x
    @y = start_y
  end
  def up(amount=1)
    @y -= amount
  end
  def down(amount=1)
    @y += amount
  end
  def right(amount=1)
    @x += amount
  end
  def left(amount=1)
    @x -= amount
  end
  def get(line)
    if @x >= line.length() - 1
      @x = @x - (line.length() - 1)
    end
    return line[@x]
  end
end


class Frame
  def initialize()
    @lines = File.readlines("./input").each
  end
  def main()
    pointer = Pointer.new(0, 0)
    trees = 0
    @lines.each() do |line|
      item = pointer.get(line)
      if item == "#"
        trees += 1
      end
      pointer.down(1)
      pointer.right(3)
    end
    return trees
  end
end

frame = Frame.new()
trees = frame.main()
puts trees
