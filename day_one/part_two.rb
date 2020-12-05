nums = []
(File.readlines("./input")).each() do |item|
  nums << item.to_i
end

num = 0
(nums).each() do |num_one|
  (nums).each() do |num_two|
    (nums).each() do |num_three|
	  if num_one + num_two + num_three == 2020
	    num = num_one * num_two * num_three
	  end
    end
  end
end
puts num
