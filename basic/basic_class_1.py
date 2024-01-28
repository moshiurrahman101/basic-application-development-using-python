"""
1. Variable
2. List
3. Condition
4. Loop
5. Function
"""
shop_name = "Moshiur Sir er khabar hotel"
print("Shop Name: ", shop_name)


vat = 12
dal_khaise_kina = False

plate = int(input("vat khaise koy plate: "))

dal_khaise_kina_status = int(input("Dal khaile 1 chapun, na khaile 0 chapun: "))

if dal_khaise_kina_status == 1:
    dal_khaise_kina = True
else:
    dal_khaise_kina = False

if dal_khaise_kina == True:
    print("Taka wala customer, dal khay")
    total_bill = (vat * plate) + 20
else:
    print("Kipta customer, dal khay na")
    total_bill = (vat * plate)
    

print("Vat: ", vat, "TK")
print("Total bill: ", total_bill, "TK")

