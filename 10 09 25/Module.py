'''You are asked to build a simple E-commerce Billing System using Python modules.
Create a module file named ecommerce_utils.py that contains the following functions:
apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
generate_invoice(cart, discount_percent=0, gst_percent=18) → accepts a dictionary cart (with product names as keys and prices as values) and prints a detailed invoice.
Create a main program file named main.py that:
Imports the ecommerce_utils module.
Creates a shopping cart (dictionary) with at least 3 products.
Calls the module functions to generate an invoice.
Expected Output Example:
------ INVOICE ------
Laptop          : ₹55000
Phone           : ₹30000Headphones      : ₹2000
---------------------
Subtotal: ₹87000
After 10% discount: ₹78300.0
After 18% GST: ₹92454.00
---------------------
Thank you for shopping with us!
 '''
def apply_discount(price,discount_percent):
     dprice=price-(price*(discount_percent/100))
     return dprice
 
def  add_gst(price,gst_percent):
    gprice=price+(price*(gst_percent/100))
    return gprice

def generate_invoice(cart,discount_percent,gst_percent):
    for key in cart:
        print(key,':',cart[key])
    print("Subtotal: ",sum(cart.values()))
    after_discount=apply_discount(sum(cart.values()),discount_percent)
    print("After 10% discount: ",after_discount)
    after_gst=add_gst(after_discount,gst_percent)
    print("After 18% GST: ",after_gst)
    print("Thank you for shopping with us!")
          
    
    
    