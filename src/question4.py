from dataclasses import dataclass
from datetime import date


@dataclass
class TerminationResult:
    vacation: float
    thirteenth_salary: float
    total: float


def calculate_termination(salary: float, hire_date: date, termination_date: date) -> TerminationResult:
    vacation = calculate_vacation(salary, hire_date, termination_date)    
    thirteenth_salary = calculate_thirteenth_salary(salary, termination_date)    
    total =  vacation + thirteenth_salary
    return TerminationResult(vacation, thirteenth_salary, total)


def calculate_vacation(salary: float, hire_date: date, termination_date: date) -> float:
    last_anniversary = get_last_anniversary(hire_date, termination_date)
    vacation_months = get_total_months(last_anniversary, termination_date)
    base_vacation = (salary / 12) * vacation_months
    vacation_with_bonus = base_vacation + (base_vacation / 3)
    return vacation_with_bonus


def get_last_anniversary(hire_date: date, termination_date: date) -> date:
    last_anniversary = date(termination_date.year, hire_date.month, hire_date.day)
    if last_anniversary > termination_date:
        last_anniversary = date(termination_date.year - 1, hire_date.month, hire_date.day)
    return last_anniversary    


def get_total_months(initial_date: date, final_date: date):
    diff_year = final_date.year - initial_date.year
    diff_month = final_date.month - initial_date.month
    total_months = diff_year * 12 + diff_month
    return total_months


def calculate_thirteenth_salary(salary: float, termination_date: date) -> float:
    thirteenth_months = termination_date.month
    result = (salary / 12) * thirteenth_months
    return result



if __name__ == "__main__":
    salary = 3000.00
    hire = date(2020, 5, 10) 
    termination = date(2025, 8, 26)

    print(
        f"With salary {salary} from 10/05/2020 until 26/8/2025: ",
        calculate_termination(salary, hire, termination)
    )