if __name__ == '__main__':

    from salary_employee import SalaryEmployee
    from hourly_employee import HourlyEmployee
    from comission_employee import CommissionEmployee
    from payroll_system import PayrollSystem

    salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
    hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
    commission_employee = CommissionEmployee(3, "Николай Хорольский", 1000, 250)

    payroll_system = PayrollSystem()
    payroll_system.calculate([
        salary_employee,
        hourly_employee,
        commission_employee
    ])


