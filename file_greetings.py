# Step 1: Create a sample file with names (so the script works standalone)
with open("names.txt", "w") as file:
    file.write("Alice\n")
    file.write("Bruno\n")
    file.write("Carla\n")
    file.write("Diego\n")

# Step 2: Read the names from the file
with open("names.txt", "r") as file:
    names = file.readlines()

# Step 3: Clean up each name (remove the newline character) and print a greeting
with open("greetings.txt", "w") as output_file:
    for name in names:
        name = name.strip()  # removes "\n" and extra spaces
        greeting = f"Hello, {name}! Welcome!"
        print(greeting)
        output_file.write(greeting + "\n")

print("\nGreetings have been saved to greetings.txt")