# 1: Creating 'admin.txt' and 'viesis.txt'
admin_data = """Marija,Krilova,admin,45
Jane,Smith,admin,30
Indiana,Jones,admin,50"""

viesis_data = """Alice,Brown,viesis,25
Matvejs,Volkovs,viesis,35
Charlie,Black,viesis,28"""

with open('admin.txt', 'w') as admin_file:
    admin_file.write(admin_data)

with open('viesis.txt', 'w') as viesis_file:
    viesis_file.write(viesis_data)

# 2: Combining files and process data
combined_data = []
with open('admin.txt', 'r') as admin_file:
    for line in admin_file:
        combined_data.append(line.strip().split(','))

with open('viesis.txt', 'r') as viesis_file:
    for line in viesis_file:
        combined_data.append(line.strip().split(','))

# 3: Calculating administrator age statistics
admin_ages = [int(person[3]) for person in combined_data if person[2] == 'admin']
average_admin_age = sum(admin_ages) / len(admin_ages)
oldest_admin_age = max(admin_ages)
youngest_admin_age = min(admin_ages)

# 4: Printing counts of admins and guests
admin_count = sum(1 for person in combined_data if person[2] == 'admin')
viesis_count = sum(1 for person in combined_data if person[2] == 'viesis')

print("Apvienotie dati:")
for person in combined_data:
    print(person)

print(f"\nVidējais administratora vecums: {average_admin_age}")
print(f"Vecākais administrators: {oldest_admin_age}")
print(f"Jaunākais administrators: {youngest_admin_age}")

print(f"\nAdministratoru skaits: {admin_count}")
print(f"Viesu skaits: {viesis_count}")