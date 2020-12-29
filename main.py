import csv
import sys

email_map = {}

EMAIL_COL = raw_input("Type in the email column header (case sensitive): ")

with open(sys.argv[1], "r") as f:
    csvreader = csv.reader(f)
    headers = csvreader.next()
    print("Found headers", headers)
    for line in csvreader:

        if EMAIL_COL not in headers:
            raise RuntimeError("Couldn't find column header.")
        email = line[headers.index(EMAIL_COL)]


        if email in email_map:

            # for each email in the map
            for key in email_map[email]:
                # for each column in the schema
                for col in headers:
                    # If the email object value is none for that column
                    if email_map[email][col] is None:
                        # update it with the value in the row
                        email_map[email][col] = line[headers.index(col)]

        else:
            obj = {}
            for header in headers:
                obj[header] = line[headers.index(header)]
            email_map[email] = obj


# for email in email_map:
#     print email
#     print email_map[email]

print "Finished!"

with open("new_file.csv", "w") as f:
    csvwriter = csv.writer(f)
    for email in email_map:
        email_obj = email_map[email]
        new_row = [email_obj[k] for k in headers]
        csvwriter.writerow(new_row)