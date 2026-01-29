#!/usr/bin/env python3
"""
Multiplication Master - Fun Times Tables Practice!
A colorful, encouraging way for kids to practice multiplication
"""

import random
import time
import sys

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_color(text, color):
    """Print colored text"""
    print(f"{color}{text}{Colors.END}")

def print_banner():
    """Display welcome banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║           🌟  MULTIPLICATION MASTER!  🌟                ║
    ║                                                          ║
    ║              Let's Practice Times Tables!                ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print_color(banner, Colors.CYAN + Colors.BOLD)

def get_child_name():
    """Get the child's name"""
    print_color("\n👋 Hello there, young mathematician!", Colors.YELLOW)
    name = input(f"{Colors.BOLD}What's your name? {Colors.END}").strip()
    if not name:
        name = "Champion"
    return name

def greet_child(name):
    """Give an enthusiastic greeting"""
    greetings = [
        f"🎉 Awesome to meet you, {name}! Ready to become a multiplication master?",
        f"🚀 Hey {name}! Let's make math FUN today!",
        f"⭐ Welcome {name}! You're going to do AMAZING!",
        f"🎯 Hi {name}! Time to show those numbers who's boss!",
        f"🌈 Hello {name}! Let's turn you into a times tables superhero!"
    ]
    print_color("\n" + random.choice(greetings), Colors.GREEN + Colors.BOLD)
    time.sleep(1)

def get_table_choice():
    """Ask which times table to practice"""
    print_color("\n" + "="*60, Colors.CYAN)
    print_color("Which times table would you like to practice?", Colors.YELLOW + Colors.BOLD)
    print_color("You can choose any number from 1 to 12!", Colors.YELLOW)
    print_color("="*60, Colors.CYAN)
    
    while True:
        try:
            choice = input(f"\n{Colors.BOLD}Enter a number (1-12): {Colors.END}").strip()
            number = int(choice)
            if 1 <= number <= 12:
                return number
            else:
                print_color("⚠️  Oops! Please choose a number between 1 and 12.", Colors.RED)
        except ValueError:
            print_color("⚠️  That's not a number! Try again.", Colors.RED)

def get_encouragement(correct, streak):
    """Return encouraging message based on performance"""
    if correct:
        if streak >= 5:
            messages = [
                "🔥 ON FIRE! You're unstoppable!",
                "⭐ BRILLIANT! You're a math wizard!",
                "🚀 INCREDIBLE! Keep this streak going!",
                "💫 PHENOMENAL! You're crushing it!",
                "🌟 SUPERB! You're on a roll!"
            ]
        elif streak >= 3:
            messages = [
                "🎯 Perfect! You're getting really good at this!",
                "✨ Excellent work! Keep it up!",
                "👏 Great job! You're on a streak!",
                "🎉 Fantastic! You're doing awesome!",
                "💪 Strong work! You've got this!"
            ]
        else:
            messages = [
                "✅ Correct! Well done!",
                "👍 Yes! That's right!",
                "🌟 Good job! Keep going!",
                "😊 Exactly! You got it!",
                "🎈 Right answer! Nice!"
            ]
    else:
        messages = [
            "💡 Not quite, but you're learning! Let's keep going!",
            "🤔 Close! Don't worry, practice makes perfect!",
            "💭 Oops! That's okay, mistakes help us learn!",
            "🌱 Not this time, but you're growing stronger with each try!",
            "🎯 Almost! You'll get the next one!"
        ]
    
    return random.choice(messages)

def practice_table(number, name):
    """Practice the chosen times table"""
    print_color(f"\n{'='*60}", Colors.CYAN)
    print_color(f"🎯 Great choice! Let's practice the {number} times table!", Colors.GREEN + Colors.BOLD)
    print_color(f"{'='*60}\n", Colors.CYAN)
    
    # Create list of numbers 1-12 and shuffle them
    multipliers = list(range(1, 13))
    random.shuffle(multipliers)
    
    correct_count = 0
    total_questions = 12
    streak = 0
    
    print_color(f"I'm going to ask you {total_questions} questions in random order.", Colors.YELLOW)
    print_color("Take your time and think carefully! 🤔\n", Colors.YELLOW)
    time.sleep(1.5)
    
    for i, mult in enumerate(multipliers, 1):
        correct_answer = number * mult
        
        # Display question
        print_color(f"\n📝 Question {i} of {total_questions}", Colors.CYAN)
        print_color(f"{'─'*30}", Colors.CYAN)
        
        while True:
            try:
                question = f"{Colors.BOLD}{Colors.BLUE}What is {number} × {mult}? {Colors.END}"
                user_answer = input(question).strip()
                answer = int(user_answer)
                break
            except ValueError:
                print_color("⚠️  Please enter a number!", Colors.RED)
        
        # Check answer
        if answer == correct_answer:
            correct_count += 1
            streak += 1
            print_color(get_encouragement(True, streak), Colors.GREEN + Colors.BOLD)
        else:
            streak = 0
            print_color(get_encouragement(False, streak), Colors.YELLOW)
            print_color(f"💡 The correct answer is {number} × {mult} = {correct_answer}", Colors.CYAN)
        
        time.sleep(0.5)
    
    # Final results
    show_results(correct_count, total_questions, number, name)

def show_results(correct, total, number, name):
    """Display final results with celebration"""
    percentage = (correct / total) * 100
    
    print_color(f"\n\n{'='*60}", Colors.CYAN)
    print_color("🎊  RESULTS TIME!  🎊", Colors.YELLOW + Colors.BOLD)
    print_color(f"{'='*60}\n", Colors.CYAN)
    
    print_color(f"Great work, {name}! Here's how you did on the {number} times table:", Colors.BLUE)
    print_color(f"\n✓ Correct answers: {correct} out of {total}", Colors.GREEN + Colors.BOLD)
    print_color(f"📊 Score: {percentage:.0f}%", Colors.CYAN + Colors.BOLD)
    
    # Performance feedback
    if percentage == 100:
        print_color("\n🏆 PERFECT SCORE! You're a MULTIPLICATION MASTER! 🏆", Colors.YELLOW + Colors.BOLD)
        print_color("🌟 You absolutely CRUSHED it! Amazing work!", Colors.GREEN)
    elif percentage >= 90:
        print_color("\n⭐ EXCELLENT! You're almost perfect!", Colors.GREEN + Colors.BOLD)
        print_color("🎯 Just a bit more practice and you'll have it mastered!", Colors.GREEN)
    elif percentage >= 75:
        print_color("\n👍 GREAT JOB! You're doing really well!", Colors.GREEN + Colors.BOLD)
        print_color("💪 Keep practicing and you'll be a master in no time!", Colors.GREEN)
    elif percentage >= 60:
        print_color("\n😊 GOOD EFFORT! You're on the right track!", Colors.YELLOW + Colors.BOLD)
        print_color("🌱 Keep practicing - you're getting stronger!", Colors.YELLOW)
    else:
        print_color("\n💪 Keep going! Every practice makes you better!", Colors.YELLOW + Colors.BOLD)
        print_color("🌟 You're learning! That's what matters most!", Colors.YELLOW)
    
    print_color(f"\n{'='*60}\n", Colors.CYAN)

def play_again():
    """Ask if they want to practice another table"""
    print_color("Would you like to practice another times table?", Colors.YELLOW + Colors.BOLD)
    while True:
        choice = input(f"{Colors.BOLD}(yes/no): {Colors.END}").strip().lower()
        if choice in ['yes', 'y', 'yeah', 'yep', 'sure']:
            return True
        elif choice in ['no', 'n', 'nope']:
            return False
        else:
            print_color("Please enter 'yes' or 'no'", Colors.RED)

def main():
    """Main program loop"""
    print_banner()
    name = get_child_name()
    greet_child(name)
    
    while True:
        number = get_table_choice()
        practice_table(number, name)
        
        if not play_again():
            break
    
    # Final goodbye
    print_color(f"\n{'='*60}", Colors.CYAN)
    print_color(f"👋 Goodbye, {name}! You did AWESOME today! 👋", Colors.GREEN + Colors.BOLD)
    print_color("🌟 Keep practicing and you'll be a math superstar! 🌟", Colors.YELLOW)
    print_color(f"{'='*60}\n", Colors.CYAN)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_color("\n\n👋 Thanks for practicing! See you next time! 🌟", Colors.YELLOW)
        sys.exit(0)