type employeeData = dict[str, int | str]
type employeeResult = dict[str, str]

def is_present(days: int) -> bool:

    """ #DocString
    Takes the number of days attended as input.
    Returns True if attendance is at least 20 days, else False.
    """
    return days >= 20


def process_employee(employee: employeeData) -> employeeResult:
    """
    Processes a single employee.

    Determines the attendance status, prints the employee's
    name and status, and returns a dictionary containing
    the employee's name and attendance status.
    """

    status = "Present" if is_present(employee["days"]) else "Absent"

    print(employee["name"], status)

    return {
        "name": employee["name"],
        "status": status
    }


def calculate_average(total_days: int, total_employees: int) -> float:
    """
    Calculates and returns the average attendance days
    of all employees.
    """

    return total_days / total_employees


def process_all_employees(
    employees: list[employeeData],
) -> tuple[list[employeeResult], float, int, int]:
    """
    Processes all employees.

    Determines attendance status for each employee,
    calculates the average attendance days,
    counts present and absent employees,
    and returns all the results.
    """

    total_days = 0
    present_count = 0
    result = []

    for employee in employees:

        total_days += employee["days"]

        employee_result = process_employee(employee)

        if is_present(employee["days"]):
            present_count += 1

        result.append(employee_result)

    average = calculate_average(total_days, len(employees))

    absent_count = len(employees) - present_count

    return result, average, present_count, absent_count



employees = [
    {"name": "Arun", "days": 22},
    {"name": "Priya", "days": 18},
    {"name": "Rahul", "days": 25},
]



result, average, present_count, absent_count = process_all_employees(employees)


for employee in result:
    print(
        f"Employee {employee['name']} is marked as {employee['status']}"
    )

print(f"Average attendance days: {average:.2f}")
print("Present employees:", present_count)
print("Absent employees:", absent_count)