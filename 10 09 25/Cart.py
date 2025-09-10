'''Expected Output Example:
------ INVOICE ------
Laptop          : ₹55000
Phone           : ₹30000Headphones      : ₹2000
---------------------
Subtotal: ₹87000
After 10% discount: ₹78300.0
After 18% GST: ₹92454.00
---------------------
Thank you for shopping with us'''
import Module
cart={'Laptop':55000,'Phone':30000,'Headphones':2000}
Module.generate_invoice(cart,10,18)