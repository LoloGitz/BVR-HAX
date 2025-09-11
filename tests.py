import time

def update_terminal_content():
    print("\033[H", end="")  # Move cursor to top-left corner
    print("\033[J", end="")  # Clear screen from cursor to end
    print("New content line 1")
    print("New content line 2")

while True:
    update_terminal_content()
    time.sleep(1) # Adjust for desired refresh rate