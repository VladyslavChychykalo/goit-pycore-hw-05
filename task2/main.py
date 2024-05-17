"""
I dont fully understand how to use correct generators for this task.
Generators make this task much more complicated here and I dont see any benefits of using them in this task.
I am not sure that my variant with generators is fully correct.

Why should we use generators in this task, if in the end we get list with floats and we can just sum then or use cycle for and sum them too
"""

from typing import Callable, Generator
import re

# Variant 1 - generators


def generator_numbers(text: str) -> Generator[float, None, None]:
    # numbers = re.findall(r"\d+\.\d+", text)
    # total_income = 0
    # while len(numbers) > 0:
    #     total_income += float(numbers.pop())
    #     yield total_income

    matches = re.finditer(r"\d+\.\d+", text)
    total_income = 0
    for match in matches:
        current_value = float(match.group())
        total_income += current_value
        yield total_income


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> int:
    # return list(func(text))[-1]
    all_totals = list(func(text))
    return int(all_totals[-1]) if all_totals else 0


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


# =====================================================================================================================


# Variant 2 - is better way to solve this task in my opinion

# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# pattern = r"\d*\.\d+"
# total_income = sum([float(i) for i in re.findall(pattern, text)])
# print(f"Загальний дохід: {total_income}")
