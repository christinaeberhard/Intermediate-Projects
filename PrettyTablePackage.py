import prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pickachu", "Glurak", "Enton"])
table.add_column("Type", ["Elecricity", "Fire", "Earth"])

table.align = "l"

print(table)