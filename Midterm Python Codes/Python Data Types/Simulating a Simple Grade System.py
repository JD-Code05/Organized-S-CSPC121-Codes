#Simulating a Simple Grade System
#BCS13 - Ubungen

def calculate_average(scores):
    return sum(scores) / len(scores)


students = {
    'YourName': (97, 99, 98, 92, 88),
    'FriendsName': (79, 90, 88, 92, 95),
    'MyName': (95, 90, 98, 92, 98)
}

for name, scores in students.items():
    average = sum(scores) / len(scores)
    print(f"{name} : {scores}")
    print(f"Average: {average:.1f}\n")