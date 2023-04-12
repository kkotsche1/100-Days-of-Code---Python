from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Age", "Male", "Female"]
table.align = "r"
table.add_row(["0-10", 3, 10])
table.add_row(["11-20", 5, 5])
table.add_row(["21-30", 17, 10])
table.add_row(["31-40", 2, 2])

print(table)
