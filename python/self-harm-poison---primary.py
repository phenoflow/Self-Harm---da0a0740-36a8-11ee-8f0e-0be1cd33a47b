# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathrym M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"K048.00","system":"readv2"},{"code":"SL...97","system":"readv2"},{"code":"SL50400","system":"readv2"},{"code":"SL50500","system":"readv2"},{"code":"SL50600","system":"readv2"},{"code":"SL50700","system":"readv2"},{"code":"SL51100","system":"readv2"},{"code":"SL52200","system":"readv2"},{"code":"SL53100","system":"readv2"},{"code":"SL54300","system":"readv2"},{"code":"SL54400","system":"readv2"},{"code":"SL5y000","system":"readv2"},{"code":"SL83200","system":"readv2"},{"code":"SL90100","system":"readv2"},{"code":"SL90300","system":"readv2"},{"code":"SL91000","system":"readv2"},{"code":"SL91100","system":"readv2"},{"code":"SL91200","system":"readv2"},{"code":"SL91300","system":"readv2"},{"code":"SL91400","system":"readv2"},{"code":"SL92000","system":"readv2"},{"code":"SL92100","system":"readv2"},{"code":"SL92200","system":"readv2"},{"code":"SL94000","system":"readv2"},{"code":"SL94300","system":"readv2"},{"code":"SL94400","system":"readv2"},{"code":"SL95000","system":"readv2"},{"code":"SLC0200","system":"readv2"},{"code":"SLC0400","system":"readv2"},{"code":"U20C.11","system":"readv2"},{"code":"U20C.12","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-poison---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-poison---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-poison---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
