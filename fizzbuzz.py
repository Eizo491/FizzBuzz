import other_code

def run_application():
    print("Welcome to the FizzBuzz Application!")
    allow_negative = input("Allow negative numbers? (yes/no): ").strip().lower() == "yes"
    
    while True:
        user_input = input("Enter a number (type 'q' to quit): ")
        if user_input.lower() == "q":
            print("Congrats you did well!!!")
            break
        try:
            number = int(user_input)
            result = other_code.fizzbuzz(number, allow_negative)
            print(f"Result: {result}")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    run_application()
