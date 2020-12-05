nums = [] of Int32
(File.read_lines("./input")).each() do |item|
  nums << item.to_i
end

num = Int32
(nums).each() do |num_one|
	(nums).each() do |num_two|
		if num_one + num_two == 2020
	  		num = num_one * num_two
		end
  	end
end
puts num
