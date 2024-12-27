class ecommerce:
    def __init__(self,base_price,discount_price,tax_persentage):
        self.base_price=base_price
        self.discount_price=discount_price
        self.tax_persentage=tax_persentage
    def final_price(self):
        if base_price<0 or discount_percentage<0 or tax_percentage<0:
            raise ValueError("Invalid amount")
        else:
            discount_amount=(tax_persentage/100)*base_price
            tax_amount=(tax_persentage/100)*base_price
            total_price=(base_price+tax_amount)-discount_amount
            print(total_price)
base_price=float(int(input("Enter base price:")))
discount_price=float(int(input("Enter discount price:")))
tax_persentage=float(int(input("Enter tax persentage:")))
try:
    e_com=ecommerce(base_price,discount_price,tax_persentage)
    e=e_com.final_price()
    print(e)
except ValueError as error:
    print(error)


        
        
            
