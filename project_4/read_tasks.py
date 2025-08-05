with open("tasks.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")

message = input("\nEnter your task or type 'quit': ")
if message.lower() != 'quit':
    with open("tasks.txt", "a") as af:
        af.write(message + "\n")
