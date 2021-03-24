import csv,sys
# CSV should have portalId,tenantId as rows
def readAuto(fileName):
    portalTen = {}
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                portalTen[row[0].strip().lower()] = row[1]
                line_count += 1
        return portalTen

def readAct(fileName):
    portalTen = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        line_count = 0
        for row in csv_reader:
            portalTen.append(row)
        return portalTen

def main():
    # read
    csv.field_size_limit(sys.maxsize)
    inputs = readAuto('WA_AUTOWNS.csv')
    #print(inputs)
    to_merge = readAct('wa_suburb.csv')

    with open('WA_output.csv', mode='w',newline='') as output_file:
        output_writer = csv.writer(output_file, delimiter='|',quoting=csv.QUOTE_NONE)

        for i,row in enumerate(to_merge):
            name = row[1].strip().lower()

            if i == 0:
                row = row[:2] + ['location'] + row[2:]
                print(row)
            else:
                row = row[:2] + [inputs.get(name, '')] + row[2:]

            output_writer.writerow(row)

main()