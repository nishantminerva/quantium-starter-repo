import csv

with open('./data/daily_sales_data_1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, escapechar = "$")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["product"]} sales {float(row["price"]) * float(row["quantity"])} on {row["date"]} region {row["region"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

    