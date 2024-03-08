import csv


def calculate_total_expenses(filename):
    total_expenses = {"Взрослый": 0.0, "Пенсионер": 0.0, "Ребенок": 0.0}

    with open(filename, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # category = row['Категория потребителей']
            expenses_adult = float(row["Взрослый"])
            expenses_pensioner = float(row["Пенсионер"])
            expenses_child = float(row["Ребенок"])

            total_expenses["Взрослый"] += expenses_adult
            total_expenses["Пенсионер"] += expenses_pensioner
            total_expenses["Ребенок"] += expenses_child

    for category, expenses in total_expenses.items():
        total_expenses[category] = f"{expenses:.2f}"

    return total_expenses
