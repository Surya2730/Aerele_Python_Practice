from dataclasses import dataclass
from enum import Enum


@dataclass
class Invoice:
    invoice_id : int
    customer_name : str
    Amount : float
    Status : str

i = Invoice(
    invoice_id = 21,
    customer_name = "Surya",
    Amount = 1000.00,
    Status = "Paid"
)

print(i)

class Status(Enum):
    PAID = "Paid"
    UNPAID = "Unpaid"


class InvoiceController:
    def validate_invoice(self, i):
        if i.invoice_id <= 0:
            raise ValueError("Invoice ID must be positive")
        elif i.customer_name == "":
            raise ValueError("Customer Name cannot be empty")
        elif i.Amount < 0:
            raise ValueError("Amount cannot be negative")
        elif i.Status not in ["Paid", "Unpaid"]:
            raise ValueError("Status must be either 'Paid' or 'Unpaid'")
        else:
            print("Invoice is Valid")


controller = InvoiceController()
controller.validate_invoice(i)

print(Status.PAID.value)


class Employee:
    def __init__(self, name):
        self.name = name

    @property
    def get_name(self):
        return self.name
    
    @get_name.setter
    def set_name(self, name):
        self.name = name
    
surya=Employee("Surya")
surya.set_name = "Surya Kumar"

print(surya.get_name)