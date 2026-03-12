# Simulating a Simple Grade System
# BCS13 - Ubungen

def compute_average(grades):
    return sum(grades) / len(grades)

def main():
    students = {
        'YourName': (97, 99, 98, 92, 88),
        'FriendsName': (79, 90, 88, 92, 95),
        'MyName': (95, 90, 98, 92, 98)
    }

    for name, scores in students.items():
        average = compute_average(scores)
        print(f"{name} : {scores}")
        print(f"Average: {average:.1f}\n")

# Run the program
main()