from dataclasses import dataclass

@dataclass
class Invoice:
    invoice_id : int
    customer_name : str
    Amount : float
    Status : str

i = Invoice(
    invoice_id = 21,
    customer_name = "",
    Amount = 1000.00,
    Status = "Paid"
)

print(i)

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

