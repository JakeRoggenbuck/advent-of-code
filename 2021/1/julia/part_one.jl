open("../input") do f
	line = 0
	last = 0
	num = -1

	while ! eof(f)
		s = readline(f)
		line += 1

		b = parse(Int64, chomp(s))
		if b > last
			num += 1
		end
		last = b
	end

	println(num)
end
