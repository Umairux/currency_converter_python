import requests

print("\nCurrency Converter")
print("-" * 20)
    
amount = float(input("Enter amount: "))
from_currency = input("Enter from Currency: ").upper()
to_currency = input("Enter to Currency: ").upper()

url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}"

response = requests.get(url)
data = response.json()

rate = data["rates"][to_currency]

converted_amount = rate * amount

print(f"{amount} {from_currency} = {converted_amount} {to_currency} ")