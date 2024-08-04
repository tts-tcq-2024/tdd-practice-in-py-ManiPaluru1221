class StringCalculator:
    MAX_NUMBER = 1000

    def add(self, numbers):
        if not numbers:
            return 0

        delimiters = [",", "\n"]
        numbers = self.process_custom_delimiter(numbers, delimiters)

        split_numbers = self.split_numbers(numbers, delimiters)
        self.validate_numbers(split_numbers)

        return sum(n for n in split_numbers if n <= self.MAX_NUMBER)

    def process_custom_delimiter(self, numbers, delimiters):
        if numbers.startswith("//"):
            delimiter_end_index = numbers.index('\n')
            custom_delimiter = numbers[2:delimiter_end_index]
            delimiters.append(custom_delimiter)
            numbers = numbers[delimiter_end_index + 1:]

        return numbers

    def split_numbers(self, numbers, delimiters):
        import re
        delimiters_pattern = '|'.join(map(re.escape, delimiters))
        return list(map(int, re.split(delimiters_pattern, numbers)))

    def validate_numbers(self, numbers):
        negative_numbers = [n for n in numbers if n < 0]
        if negative_numbers:
            raise Exception("Negatives not allowed: " + ", ".join(map(str, negative_numbers)))
