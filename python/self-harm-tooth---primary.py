# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathrym M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"SLX..00","system":"readv2"},{"code":"SyuFH00","system":"readv2"},{"code":"SyuFJ00","system":"readv2"},{"code":"SyuFL00","system":"readv2"},{"code":"SyuFc00","system":"readv2"},{"code":"TK02.00","system":"readv2"},{"code":"TK3y.00","system":"readv2"},{"code":"TK71.00","system":"readv2"},{"code":"U207.00","system":"readv2"},{"code":"U207000","system":"readv2"},{"code":"U207100","system":"readv2"},{"code":"U207200","system":"readv2"},{"code":"U207300","system":"readv2"},{"code":"U207400","system":"readv2"},{"code":"U207500","system":"readv2"},{"code":"U207600","system":"readv2"},{"code":"U207700","system":"readv2"},{"code":"U207y00","system":"readv2"},{"code":"U207z00","system":"readv2"},{"code":"U208000","system":"readv2"},{"code":"U208100","system":"readv2"},{"code":"U208200","system":"readv2"},{"code":"U208300","system":"readv2"},{"code":"U208400","system":"readv2"},{"code":"U208500","system":"readv2"},{"code":"U208600","system":"readv2"},{"code":"U208700","system":"readv2"},{"code":"U208y00","system":"readv2"},{"code":"U208z00","system":"readv2"},{"code":"U21y.00","system":"readv2"},{"code":"U22y.00","system":"readv2"},{"code":"U232.00","system":"readv2"},{"code":"U23y.00","system":"readv2"},{"code":"U24y.00","system":"readv2"},{"code":"U250.00","system":"readv2"},{"code":"U251.00","system":"readv2"},{"code":"U252.00","system":"readv2"},{"code":"U253.00","system":"readv2"},{"code":"U254.00","system":"readv2"},{"code":"U255.00","system":"readv2"},{"code":"U256.00","system":"readv2"},{"code":"U257.00","system":"readv2"},{"code":"U25y.00","system":"readv2"},{"code":"U25z.00","system":"readv2"},{"code":"U26y.00","system":"readv2"},{"code":"U27y.00","system":"readv2"},{"code":"U28y.00","system":"readv2"},{"code":"U292.00","system":"readv2"},{"code":"U29y.00","system":"readv2"},{"code":"U2A2.00","system":"readv2"},{"code":"U2Ay.00","system":"readv2"},{"code":"U2B2.00","system":"readv2"},{"code":"U2By.00","system":"readv2"},{"code":"U2Cy.00","system":"readv2"},{"code":"U2Dy.00","system":"readv2"},{"code":"U2y0.00","system":"readv2"},{"code":"U2y1.00","system":"readv2"},{"code":"U2y2.00","system":"readv2"},{"code":"U2y3.00","system":"readv2"},{"code":"U2y4.00","system":"readv2"},{"code":"U2y5.00","system":"readv2"},{"code":"U2y6.00","system":"readv2"},{"code":"U2y7.00","system":"readv2"},{"code":"U2yy.00","system":"readv2"},{"code":"U2yz.00","system":"readv2"},{"code":"U2zy.00","system":"readv2"},{"code":"U407000","system":"readv2"},{"code":"U407100","system":"readv2"},{"code":"U407200","system":"readv2"},{"code":"U407300","system":"readv2"},{"code":"U407400","system":"readv2"},{"code":"U407500","system":"readv2"},{"code":"U407600","system":"readv2"},{"code":"U407700","system":"readv2"},{"code":"U407y00","system":"readv2"},{"code":"U407z00","system":"readv2"},{"code":"U408000","system":"readv2"},{"code":"U408100","system":"readv2"},{"code":"U408200","system":"readv2"},{"code":"U408300","system":"readv2"},{"code":"U408400","system":"readv2"},{"code":"U408500","system":"readv2"},{"code":"U408600","system":"readv2"},{"code":"U408700","system":"readv2"},{"code":"U408y00","system":"readv2"},{"code":"U408z00","system":"readv2"},{"code":"U412.00","system":"readv2"},{"code":"U41y.00","system":"readv2"},{"code":"ZX1L900","system":"readv2"},{"code":"ZX1L911","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-tooth---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-tooth---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-tooth---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
