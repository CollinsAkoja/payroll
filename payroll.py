# here we will enter the employee details and then we will save it in the database

# Employee classes
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20


class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.15


# Payment classes
class Payment:
    def process_payment(self, employee):
        raise NotImplementedError("Subclasses must implement this method.")


class CreditCardPayment(Payment):
    def process_payment(self, employee):
        total = employee.salary + employee.calculate_bonus()
        print(f"Processing credit card payment for {employee.name}. Amount: ₦{total:.2f}")


class PayPalPayment(Payment):
    def process_payment(self, employee):
        total = employee.salary + employee.calculate_bonus()
        print(f"Processing PayPal payment for {employee.name}. Amount: ₦{total:.2f}")


class BankTransferPayment(Payment):
    def process_payment(self, employee):
        total = employee.salary + employee.calculate_bonus()
        print(f"Processing bank transfer for {employee.name}. Amount: ₦{total:.2f}")


# Payroll integration
class PayrollSystem:
    def __init__(self):
        self.payments = []

    def add_employee_payment(self, employee, payment_method):
        self.payments.append((employee, payment_method))

    def run_payroll(self):
        for employee, payment_method in self.payments:
            print(f"\nPaying {employee.name}:")
            payment_method.process_payment(employee)



if __name__ == "__main__":
    # Create employees
    Collins = Manager("Collins", 90000)
    Israel = Developer("Israel", 70000)
    Odiase = Employee("Odiase", 50000)

    # Assign payment methods
    Collins_payment = CreditCardPayment()
    Israel_payment = PayPalPayment()
    Odiase_payment = BankTransferPayment()

    # Here i will create a payroll system
    payroll = PayrollSystem()
    payroll.add_employee_payment(Collins, Collins_payment)
    payroll.add_employee_payment(Israel, Israel_payment)
    payroll.add_employee_payment(Odiase, Odiase_payment)

    # Run payroll to get output
    payroll.run_payroll()
