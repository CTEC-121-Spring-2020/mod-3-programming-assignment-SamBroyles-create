# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Sam Broyles

def shippingCost(orderSubTotal):
    shippingCost = 2.99
    # enter code here to test for free
    
    if orderSubTotal >= 10.00:
        print("Shipping cost: 0.00!\n")
    elif orderSubTotal <= 10.00:
        print("Shipping cost: 2.99\n")


def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(2.99))
    print()
    # enter additional test code here
    shippingCost(5.00)
    shippingCost(15.00)

if __name__ == "__main__":
    unitTest()