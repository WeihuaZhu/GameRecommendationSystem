import csv

index = 0
with open('ign.csv') as csv_file:
    with open('output_ign.csv', mode='w') as output_ign:
        csv_reader = csv.reader(csv_file, delimiter=',')
        output_writer = csv.writer(output_ign, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
            if csv_reader.line_num == 1 or row[4] == 'iPad' or row[4] == 'iPhone':
                continue
            else:
                row[0] = index
                index += 1
                output_writer.writerow(row)
