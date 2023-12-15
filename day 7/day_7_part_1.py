loan_amount = float(input("Please enter the amount of credit: "))

monthly_rate_year1 = 0.02
monthly_rate_year2 = 0.04

months_to_pay = [12, 60]

for months in months_to_pay:

    balance = loan_amount
    interest_paid = 0
    years = int(months/12)

    print(f"\nRepayment in {months} months | {years} year(s):")
    print()
    print(f"{'Month':^10} {'Payment':^10} {'Persent':^10}")

    monthly_payment = loan_amount / months

    for i in range(1, months + 1):
        interest = monthly_rate_year1 / 12 * balance if i <= 24 else monthly_rate_year2 / 12 * balance
        interest_paid += interest
        balance -= monthly_payment
        balance += interest

        print(f"{i:^10} {monthly_payment:^10.2f} {interest:^10.2f}")

    print(f"\nCredit body {loan_amount}")
    print(f"Total interest paid: {interest_paid:.2f}")
    print(f"\nTotal value: {(interest_paid + loan_amount):.2f} ")