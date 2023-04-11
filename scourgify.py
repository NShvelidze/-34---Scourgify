import sys
import csv

def main():
    command_line_argument_check()
    list = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name_split = row["name"].split(",")
                list.append({"first": name_split[1].strip(), "last": name_split[0], "house": row["house"]})
    except:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        for row in list:
             writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def command_line_argument_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
