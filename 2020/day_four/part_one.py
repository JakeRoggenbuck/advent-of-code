class Passport:
    def __init__(self, raw_passport: str):
        self.raw_passport = raw_passport
        self.parsed_passport = self.parse_passport()

    def parse_passport(self):
        parsed_passport = {}
        passport_items = self.raw_passport.split()
        for passport_item in passport_items:
            key, value = passport_item.split(":")
            parsed_passport[key] = value
        return parsed_passport

    def main(self):
        passport = self.parsed_passport
        if len(passport) == 8:
            return True
        if len(passport) == 7 and "cid" not in passport:
            return True


amount = 0
for raw_passport in open("./input").read().split("\n\n"):
    passport = Passport(raw_passport)
    if passport.main():
        amount += 1
print(amount)
