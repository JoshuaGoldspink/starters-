import xlsxwriter

purchases = open("Purchases_list", "a")





# create file (tracker) and sheet
tracker = xlsxwriter.Workbook("tracker.xlsx")
sheet = tracker.add_worksheet()

# declare data
purchases = ["food", "electricity", "spending"]
values = [300, 100, 400]



#add data
purchases.append(input("Add a purchase: "))
values.append(input(str("How much did it cost?")))


def add_data():
    purchases.append(input("Add a purchase: "))
    values.append(input("How much did it cost?" ))
    repeat = bool(input("you done?"))


while input("you done?") == "no":
    add_data()


# write headers
sheet.write("A1", "purchases")
sheet.write("B1", "cost")

# write data to file
for item in range(len(purchases)):
    sheet.write(item+1, 0, purchases[item])
    sheet.write(item+1, 1, values[item])

sheet.write("D1", "Total")
sheet.write_formula("D2", "=SUM(B2:B20)")



tracker.close()
