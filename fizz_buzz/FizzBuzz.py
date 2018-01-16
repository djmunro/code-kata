def divisible_by_three(number):
    return number % 3 == 0


def divisible_by_five(number):
    return number % 5 == 0


class FizzBuzz(object):
    def of(self, number):
        self.verify_number(number)
        return self.compute_answer(number)

    def verify_number(self, number):
        if number <= 0:
            raise ValueError("number is less than or equal to 0")

    def compute_answer(self, number):
        if divisible_by_three(number) and divisible_by_five(number):
            number = 'FizzBuzz'
        elif divisible_by_three(number):
            number = 'Fizz'
        elif divisible_by_five(number):
            number = 'Buzz'
        return number
