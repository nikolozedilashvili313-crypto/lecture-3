import csv

def load_ssl_companies(input_csv="ssl_companies.csv"):
    filtered_companies = []
    with open(input_csv, "r", encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                emp_str = row.get("Number of employees", row.get("Number of Employees", "0"))
                if int(emp_str) > 1000:
                    company_info = {
                        "Name": row.get("Name", ""),
                        "Industry": row.get("Industry", ""),
                        "Number of employees": row.get("Number of employees", "")
                    }
                    filtered_companies.append(company_info)
            except (ValueError, KeyError):
                continue
    return filtered_companies

def save_filtered_ssl_companies_to_csv(excepted_data, output = "sorted_companies.csv"):
    if not excepted_data:
        print("No data available to save.")
        return

    fieldnames = ["Name", "Industry", "Number of employees"]

    with open(output, "w", newline="", encoding = "utf-8") as file:
       writer = csv.DictWriter(file, fieldnames=fieldnames)
       writer.writeheader()
       writer.writerows(excepted_data)
    print(f"Filtered SSL companies saved to '{output}'.")


loaded_companies = load_ssl_companies()
save_filtered_ssl_companies_to_csv(loaded_companies)