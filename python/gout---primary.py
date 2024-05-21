# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"C345.00","system":"readv2"},{"code":"6693.00","system":"readv2"},{"code":"6696.00","system":"readv2"},{"code":"C342.00","system":"readv2"},{"code":"C34..00","system":"readv2"},{"code":"6697.00","system":"readv2"},{"code":"6695.00","system":"readv2"},{"code":"1443.00","system":"readv2"},{"code":"C344.00","system":"readv2"},{"code":"C34y300","system":"readv2"},{"code":"C34z.00","system":"readv2"},{"code":"C34y400","system":"readv2"},{"code":"11462.0","system":"readv2"},{"code":"12594.0","system":"readv2"},{"code":"57334.0","system":"readv2"},{"code":"52117.0","system":"readv2"},{"code":"2857.0","system":"readv2"},{"code":"94539.0","system":"readv2"},{"code":"49775.0","system":"readv2"},{"code":"45465.0","system":"readv2"},{"code":"14996.0","system":"readv2"},{"code":"709.0","system":"readv2"},{"code":"36481.0","system":"readv2"},{"code":"72471.0","system":"readv2"},{"code":"3759.0","system":"readv2"},{"code":"59344.0","system":"readv2"},{"code":"50067.0","system":"readv2"},{"code":"27521.0","system":"readv2"},{"code":"97539.0","system":"readv2"},{"code":"9874.0","system":"readv2"},{"code":"35660.0","system":"readv2"},{"code":"68209.0","system":"readv2"},{"code":"58064.0","system":"readv2"},{"code":"93677.0","system":"readv2"},{"code":"52101.0","system":"readv2"},{"code":"17284.0","system":"readv2"},{"code":"10080.0","system":"readv2"},{"code":"21687.0","system":"readv2"},{"code":"34006.0","system":"readv2"},{"code":"29658.0","system":"readv2"},{"code":"93689.0","system":"readv2"},{"code":"16475.0","system":"readv2"},{"code":"52969.0","system":"readv2"},{"code":"58746.0","system":"readv2"},{"code":"4440.0","system":"readv2"},{"code":"24153.0","system":"readv2"},{"code":"28999.0","system":"readv2"},{"code":"44566.0","system":"readv2"},{"code":"60541.0","system":"readv2"},{"code":"61145.0","system":"readv2"},{"code":"35664.0","system":"readv2"},{"code":"M10","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('gout-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["gout---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["gout---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["gout---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
