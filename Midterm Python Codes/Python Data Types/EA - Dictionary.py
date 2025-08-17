#EA - Dictionary
#BCS13 - Ubungen
#Feb 5, 2025
def record_keep_app():
    dictionary = {}
    
    while True:
        print("Menu:")
        print("[a]: Add Data")
        print("[b]: Delete Data")
        print("[c]: End")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'a':
            key = input("Enter Key: ").strip()
            value = input("Value: ").strip()
            dictionary[key] = value
            print(dictionary)
            
        elif choice == 'b':
            key = input("Enter Key: ").strip()
            if key in dictionary:
                del dictionary[key]
            print(dictionary)
        
        elif choice == 'c':
            print("THANK YOU")
            retry = input("Try again? yes/no: ").strip().lower()
            if retry == 'yes':
                continue
            else:
                break
        else:
            print("Invalid choice, please try again.")
            continue
        
        retry = input("Try again? yes/no: ").strip().lower()
        if retry != 'yes':
            break
        
    print(dictionary)
        
record_keep_app()
