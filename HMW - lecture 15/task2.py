import csv

def filtered_survivors(titanic_csv= "titanic.csv"):
    with open(titanic_csv, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        survivors = [row for row in reader if row["Survived"] == "1"]
        return survivors




def save_filtered_survivors_to_csv(survivors_data,  output_csv="survivived.csv"):
    if not survivors_data:
        print("No survivors data available.")
        return
    with open(output_csv, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=survivors_data[0].keys())
        writer.writeheader()
        writer.writerows(survivors_data)
    print(f"Filtered survivors saved to '{output_csv}'.")

survivors = filtered_survivors()
save_filtered_survivors_to_csv(survivors)