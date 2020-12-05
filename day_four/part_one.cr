class Passport
	@parsed_passport : Hash(String, String)

	def initialize(raw_passport : String)
		@raw_passport = raw_passport
		@parsed_passport = parse_passport()
	end

	def parse_passport
		parsed_passport = {} of String => String
		(@raw_passport.split()).each() do |item|
			key, value = item.split(":")
			parsed_passport[key] = value
		end
		return parsed_passport
	end

	def check
		if @parsed_passport.size == 8
			return true
		end
		if @parsed_passport.size == 7 && ! @parsed_passport.has_key?("cid")
			return true
		end
	end
end


valid = 0
File.read("./input").split("\n\n").each do |raw_line|
	passport = Passport.new raw_line
  	if passport.check()
    	valid += 1
  	end
end
puts valid
