import re
from typing import Callable, Generator


# generator from extract numbers from str
def generator_numbers(content_text: str) -> Generator[float, None, None]:
    regex = r'\b\d+\.\d+\b'
    for number in re.findall(regex, content_text):
        yield float(number)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))


context = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(context, generator_numbers)
print(f"Total income: {total_income}")
