"""
Basic Calc (With Extra Sass v1.0)
Author: Keshma Rampersad
Description: A CLI calculator that processes user input (with some sassy comments)
                and logs calculation history to a local file.
"""
import os
import time
import random 

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
ORANGE = "\033[38;5;208m"
YELLOW = "\033[93m"
PINK = "\033[95m"
RESET = "\033[0m"

history = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sassy_loading():
    
    loading_messages = [
        "Hmmmm, let's see...",
        "Analyzing your questionable choices...",
        "Consulting the math gods...",
        "Checking if you're actually a CS student...",
        "Don't rush me, I'm doing my best...",
        "Calculating the probability of passing 136...",
        "Asking a nearby goose for the answer...",
        "Processing... math is hard sometimes ok...",
        "Crunching numbers, unlike your fruit consumption...",
        "Wait for it... drama takes time..."
    ]
    # Displays a randomized loading message with a visual progress bar
    current_msg = random.choice(loading_messages)
    print(f"{CYAN}[ {current_msg} ]{RESET}")
    for i in range(10):
        time.sleep(0.075)
        print("■", end="", flush=True)
    print("\n")

# Dictionaries mapping operators to randomized "roast" responses

roast_map = {
    "+": [
        "Wow, 1+1 vibes. Groundbreaking!!",
        "Adding? How original.",
        "Stunning. 1+1 vibes.",
        "Basic addition. Moving on...",
        "Is this what you're doing instead of your actual work?",
        "Wow. You really needed a calculator for that?",
        "10/10 math. 0/10 for effort.",
        "Calculated. Now go touch some grass.",
        "I've seen smarter logic in a toaster, but sure.",
        "My battery is draining just looking at this math."
    ],
    "-": [
        "Subtracting? How original.",
        "Subtracting? Edgy.",
        "Taking things away... like your free time.",
        "Wow, subtraction. So deep.",
        "Is that the amount of sleep you got last night?",
        "Less is more, I guess.",
        "Negative energy only, apparently.",
        "Did you really need me for that tiny difference?",
        "Subtracting your productivity from the day, are we?",
        "Almost as impressive as a grade 2 math quiz."
    ],
    "*": [
        "Oooo multiplication! So edgy.",
        "Multiplication? Look at you go.",
        "Trying to be productive, I see.",
        "Big numbers, big ego.",
        "Exponentially boring.",
        "Just making things bigger for no reason.",
        "Calculated it. Are you impressed yet?",
        "Multiplying your problems, one click at a time.",
        "I hope you're using this for something useful. (Unlikely).",
        "Look at you, doing 'hard' math."
    ],
    "/": [
        "Division? Living on the edge, I see.",
        "Careful, don't break the universe.",
        "Dividing... hopefully not by zero.",
        "Breaking things down? Very therapeutic.",
        "Splitting hairs, are we?",
        "Dividing your attention between this and your degree.",
        "Shared math is better math? No.",
        "Slicing and dicing. Very chef-like."
    ],
    "%": [
        "Modulus? Fancy.",
        "Modulus? Okay, nerd.",
        "Ah, the remainder. Very sophisticated.",
        "Modulo? You definitely just googled what that does.",
        "The most 'CS student' operator choice ever.",
        "Remind me why we care about the remainder again?",
        "Quite a niche operator you chose there!.",
        "Searching for what's left behind? Moody."
    ]
}

div_zero_roasts = [
    "Try not to break the universe, okay?",
    "Even my puppy knows you can't do that.",
    "Division by zero? Groundbreaking error choice.",
    "I'm a calculator, not a magician. Pick a another number.",
    "Infinite math detected. My brain hurts."
]

stress_responses = {
    "low": ["Must be nice. Go do some LeetCode.", "Clearly you haven't seen the CS 136 final yet.", "Enjoy the peace while it lasts."],
    "mid": ["Typical Waterloo student vibe.", "You're in the 'Danger Zone'. Drink some coffee.", "Balanced, as all things should be... for now."],
    "high": ["Go touch some grass at Waterloo Park.", "The geese can smell your fear.", "Don't worry, the curve is a myth anyway."]
}

goodbye_messages = [
    "Well, less work for me :) Bye!",
    "Finally, I thought you'd never leave.",
    "Go touch some grass, I mean snow, at Waterloo Park. You need it.",
    "Leaving so soon? Coward.",
    "Safe travels. Watch out for the geese.",
    "Nice meeting you I guess. Don't forget to water your plants or something.",
    "Error 404: Motivation not found. Goodbye."
]

clear()
print(f"""{GREEN}
  ____             _          ______   ___          
 | __ )  __ _ ___ (_)  ____  /_|__ _|  | | ___ 
 |  _ \ / _` / __| | |/ __| | |   / _` | |/ __|
 | |_) | (_| \__ \ | | (__  | |__| (_| | | (__ 
 |____/ \__,_|___/_|_|\___|  \____\__,_|_|\___|
          (With Extra Sass v1.0)
{RESET}""")

# Main application loop
while True:

    print(f"\n{ORANGE} ~~~~~~ New Calculation ~~~~~~ {RESET}")
    print(f"[ Commands: '{PINK}q{RESET}' to quit, '{PINK}h{RESET}' for history, '{PINK}midterm{RESET}' for a reality check ]")
    user_choice = input("Enter first number or command: ").lower()

    # --- System Command Handling ---
    if user_choice == 'q':
        print(f"{RED}{random.choice(goodbye_messages)}{RESET}\n")
        break

    if user_choice == 'h':
        # Displays and manages the 'shame_log' file
        print(f"{CYAN}\n--- YOUR ENTIRE SHAMEFUL HISTORY ---{RESET}")
        try:
            with open("shame_log.txt", "r") as f:
                content = f.readlines()
                if not content:
                    print("The log is empty. Go do some math!")
                else:
                    for line in content:
                        print(f"> {line.strip()}")
                    # Optional history wipe
                    confirm = input(f"\n{PINK}Wipe the shame away? (type 'clear' to delete everything or enter to skip): {RESET}").lower()
                    if confirm == 'clear':
                        open("shame_log.txt", "w").close()
                        print(f"{GREEN}History purged. You're a clean slate now.{RESET}")
                    else:
                        print(f"{CYAN}History preserved. Your shame remains.{RESET}")
        except FileNotFoundError:
            print("No history file found yet.")
        continue
    
    if user_choice == 'midterm':
        # Prediction feature based on stress intensity level
        try:
            stress_input = input("On a scale of 1-10, how stressed are you? ")
            stress = int(stress_input)

            if stress < 0:
                print(f"{CYAN}How is this possible? Are you sure you're a uni student?{RESET}")
            elif stress > 10:
                print(f"{RED}ERROR: STRESS OVERLOAD. Please locate the nearest goose and apologize to it immediately.{RESET}")
            elif stress <= 3:
                print(f"{GREEN}Prediction: {random.choice(stress_responses['low'])}{RESET}")
            elif stress <= 7:
                print(f"{YELLOW}Prediction: {random.choice(stress_responses['mid'])}{RESET}")
            else:
                print(f"{RED}Prediction: {random.choice(stress_responses['high'])}{RESET}")
        except ValueError:
            print(f"{RED}That's not a number. Your stress is literally off the charts.{RESET}")
        continue

    # --- Math Calculation Handling ---
    try:
        # Validate that the first input is a number
        num1 = float(user_choice)
        op = input("Operator (+, -, *, /, %, or secret): ").lower()

        # Secret Easter Egg Commands
        if op == "goose":
            sassy_loading()
            print(f"{YELLOW}HONK! 🦢{RESET}")
            print(f"{GREEN}RESULT: Eternal Luck{RESET}")
            print("You have been blessed by a Waterloo Goose. Your next midterm is curved.")
            continue

        if op == "keshma":
            sassy_loading()
            print(f"{PINK}✨ HEYYYY THAT'S ME! ✨{RESET}")
            print(f"{CYAN}I built this calculator as my first official CS project (yes, I am aware that I'm behind).{RESET}")
            print(f"{YELLOW}Current Status: Trying to survive 1B and land a spring co-op...{RESET}")
            continue

        # Standard operator validation
        valid_ops = ["+", "-", "*", "/", "%"]
        if op not in valid_ops:
            print(f"{RED}\nThat's not even an operator, my friend. Try again.{RESET}")
            continue

        num2 = float(input("Second number: "))
        sassy_loading()

        # Perform calculation and handle division by zero error
        if op == "/": 
            if num2 == 0:
                print(f"{RED}RESULT: ERROR{RESET}")
                print(f"{RED}{random.choice(div_zero_roasts)}{RESET}")
                history.append(f"{num1} / {num2} = ERROR (Universe intact)")
                with open("shame_log.txt", "a") as f:
                    f.write(f"{num1} / {num2} = ERROR (Universe intact)\n")
                continue
            result = num1 / num2
        elif op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "%": result = num1 % num2

        # Display final result with left-alignment formatting for UI consistency
        print(f"{GREEN}╔═══════════════════════════════════╗")
        print(f"║  RESULT: {result:<24} ║")
        print(f"╚═══════════════════════════════════╝{RESET}")
        print(f"{YELLOW}{random.choice(roast_map[op])}{RESET}")

        # Update local history and append to the 'shame_log.txt' file
        history.append(f"{num1} {op} {num2} = {result}")
        with open("shame_log.txt", "a") as f:
            f.write(f"{num1} {op} {num2} = {result}\n")
        print("-----------------------------------")
    
    except ValueError:
        print(f"{RED}\nUm... that wasn't an option 💀{RESET}")
        print("-----------------------------------")