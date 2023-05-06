import csv
import random

def read_names_from_csv(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        names = [row[0] for row in reader]
    return names

def generate_random_name(first_names, last_names):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def main():
    first_names_file = "first_names.csv"
    last_names_file = "last_names.csv"

    first_names = read_names_from_csv(first_names_file)
    last_names = read_names_from_csv(last_names_file)

    random_name = generate_random_name(first_names, last_names)
    print(random_name)

if __name__ == "__main__":
    main()
