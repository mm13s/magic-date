the following codes will include a variety of different while loops, if statements, and things covered in the previous chapters all combined in one ####

# 6 magic date
def get_user_input():
    try:
        month = int(input("Enter the month (numeric form): "))
        day = int(input("Enter the day: "))
        year = int(input("Enter the two-digit year: "))
        
        if not (1 <= month <= 12) or not (1 <= day <= 31) or not (0 <= year <= 99):
            raise ValueError("Invalid input. Month, day, and year must be within valid ranges.")
        
        return month, day, year
    except ValueError as error:
        print(f"Input error: {enter a valid month, day, year}")
        return None

def is_magic_date(month, day, year):
    return month * day == year

def main():
    user_input = get_user_input()
    
    if user_input is not None:
        month, day, year = user_input
        if is_magic_date(month, day, year):
            print("The date is magic!")
        else:
            print("The date is not magic.")

if __name__ == "__main":
    main()
