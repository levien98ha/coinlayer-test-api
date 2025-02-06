from config import end_point, private_key, api_url
from middleware import handle_request, handle_response

def fectch_live():
  endpoint = end_point['live']
  result = handle_request(endpoint)

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