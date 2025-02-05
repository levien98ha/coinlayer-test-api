from config import end_point, private_key, api_url
from middleware import handle_request, handle_response
import csv

def export_csv(rates):
  csv_file = 'crypto_rates.csv'
  with open(csv_file, mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Currency', 'Rate'])
      
      for currency, rate in rates.items():
          writer.writerow([currency, rate])

def fectch_live():
  endpoint = end_point['live']
  result = handle_request(endpoint)
  rates = result['rates']
  export_csv(rates)
  print(f"{'Currency':<10} {'Rate':<15}")
  print("-" * 25)
  for currency, rate in rates.items():
      print(f"{currency:<10} {rate:<15}")

def show_menu():
    print("Menu:")
    print("1. Fetch Live")
    print("2. Option 2")
    print("3. Option 3")
    print("10. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Calling------------------------------------------------")
            fectch_live()
        elif choice == '2':
            print("Option 2 selected.")
        elif choice == '3':
            print("Option 3 selected.")
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()