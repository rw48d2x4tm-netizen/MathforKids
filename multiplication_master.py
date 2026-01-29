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
    ║           🌟  MATH MASTER!  🌟                          ║
    ║                                                          ║
    ║        Let's Practice Multiplication & Division!         ║
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

def get_operation_choice():
    """Ask whether to practice multiplication or division"""
    print_color("\n" + "="*60, Colors.CYAN)
    print_color("What would you like to practice today?", Colors.YELLOW + Colors.BOLD)
    print_color("="*60, Colors.CYAN)
    
    print_color("\n✖️  Type 'M' for MULTIPLICATION (times tables)", Colors.GREEN)
    print_color("➗ Type 'D' for DIVISION", Colors.BLUE)
    
    while True:
        choice = input(f"\n{Colors.BOLD}Enter your choice (M or D): {Colors.END}").strip().upper()
        if choice in ['M', 'MULTIPLICATION', 'MULTIPLY', 'TIMES']:
            print_color("\n🎯 Excellent! Let's work on MULTIPLICATION!", Colors.GREEN + Colors.BOLD)
            return 'M'
        elif choice in ['D', 'DIVISION', 'DIVIDE']:
            print_color("\n🎯 Awesome! Let's work on DIVISION!", Colors.BLUE + Colors.BOLD)
            return 'D'
        else:
            print_color("⚠️  Please enter 'M' for Multiplication or 'D' for Division.", Colors.RED)

def get_table_choice():
    """Ask which times table to practice"""
    print_color("\n" + "="*60, Colors.CYAN)
    print_color("Which number would you like to practice with?", Colors.YELLOW + Colors.BOLD)
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

def celebrate_correct_answer(streak):
    """Display big celebration for correct answers"""
    if streak >= 5:
        celebrations = [
            """
    🔥🔥🔥 AMAZING STREAK! 🔥🔥🔥
    ⭐ You're ON FIRE! ⭐
    Keep up this INCREDIBLE work!
            """,
            """
    ✨✨✨ WOW! WOW! WOW! ✨✨✨
    🚀 You're a MATH SUPERSTAR! 🚀
    This is OUTSTANDING!
            """,
            """
    🌟🌟🌟 SPECTACULAR! 🌟🌟🌟
    💫 You're UNSTOPPABLE! 💫
    What a BRILLIANT streak!
            """,
            """
    🏆🏆🏆 CHAMPION MODE! 🏆🏆🏆
    ⚡ You're CRUSHING IT! ⚡
    Keep this AWESOME streak going!
            """
        ]
    elif streak >= 3:
        celebrations = [
            """
    🎯🎯 EXCELLENT! 🎯🎯
    ⭐ That's THREE in a row! ⭐
    You're doing FANTASTIC!
            """,
            """
    ✨✨ WONDERFUL! ✨✨
    🎉 You're on a GREAT streak! 🎉
    Keep up the AMAZING work!
            """,
            """
    💪💪 TERRIFIC! 💪💪
    🌟 Three correct! You're AWESOME! 🌟
    You've really got this!
            """,
            """
    👏👏 SUPERB! 👏👏
    🚀 You're getting SO good at this! 🚀
    What a GREAT streak!
            """
        ]
    else:
        celebrations = [
            """
    ✅ YES! That's CORRECT! ✅
    🌟 You got it RIGHT! 🌟
    Excellent work!
            """,
            """
    👍 PERFECT! 👍
    ⭐ You nailed it! ⭐
    Great job!
            """,
            """
    🎉 CORRECT! 🎉
    😊 You're doing GREAT! 😊
    Keep it up!
            """,
            """
    ⚡ RIGHT ANSWER! ⚡
    🎯 You've got this! 🎯
    Well done!
            """,
            """
    🌈 EXACTLY RIGHT! 🌈
    ✨ Fantastic work! ✨
    You're awesome!
            """
        ]
    
    celebration = random.choice(celebrations)
    print_color(celebration, Colors.GREEN + Colors.BOLD)

def show_incorrect_answer_generic(problem, correct_answer):
    """Display supportive feedback for incorrect answers"""
    
    print_color("\n❌ That's not quite right, but that's okay! ❌", Colors.RED + Colors.BOLD)
    print_color(f"\n📚 The correct answer is: {problem} = {correct_answer}", Colors.CYAN + Colors.BOLD)
    
    encouragements = [
        """
    💪 Don't worry! Mistakes help us LEARN and grow!
    🌱 You're becoming smarter with every try!
    🌟 Keep going - you're doing GREAT!
        """,
        """
    🤗 It's totally okay! Everyone makes mistakes!
    💡 That's how we become multiplication masters!
    ⭐ You've got this - keep trying!
        """,
        """
    😊 No problem! Practice makes perfect!
    🎯 You're learning and that's AWESOME!
    🚀 Next one will be even better!
        """,
        """
    🌈 That's alright! You're doing wonderfully!
    💫 Every mistake is a step closer to success!
    ✨ Keep up the great effort!
        """,
        """
    👍 Good try! You're working so hard!
    🌟 Learning takes time, and you're doing AMAZING!
    🎉 I know you'll get the next one!
        """,
        """
    💖 It's okay! You're being so brave by trying!
    🌻 Mistakes are just proof you're learning!
    ⭐ Keep that positive attitude - you rock!
        """
    ]
    
    encouragement = random.choice(encouragements)
    print_color(encouragement, Colors.YELLOW + Colors.BOLD)

def practice_table(number, name, operation):
    """Practice the chosen operation (multiplication or division)"""
    operation_name = "MULTIPLICATION" if operation == 'M' else "DIVISION"
    operation_symbol = "×" if operation == 'M' else "÷"
    
    print_color(f"\n{'='*60}", Colors.CYAN)
    print_color(f"🎯 Great choice! Let's practice {operation_name} with {number}!", Colors.GREEN + Colors.BOLD)
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
        if operation == 'M':
            # Multiplication: number × mult = ?
            question_text = f"What is {number} × {mult}?"
            correct_answer = number * mult
            problem_display = f"{number} × {mult}"
        else:
            # Division: (number × mult) ÷ number = ?
            dividend = number * mult
            question_text = f"What is {dividend} ÷ {number}?"
            correct_answer = mult
            problem_display = f"{dividend} ÷ {number}"
        
        # Display question
        print_color(f"\n📝 Question {i} of {total_questions}", Colors.CYAN)
        print_color(f"{'─'*30}", Colors.CYAN)
        
        while True:
            try:
                question = f"{Colors.BOLD}{Colors.BLUE}{question_text} {Colors.END}"
                user_answer = input(question).strip()
                answer = int(user_answer)
                break
            except ValueError:
                print_color("⚠️  Please enter a number!", Colors.RED)
        
        # Check answer
        if answer == correct_answer:
            correct_count += 1
            streak += 1
            celebrate_correct_answer(streak)
        else:
            streak = 0
            show_incorrect_answer_generic(problem_display, correct_answer)
        
        time.sleep(0.8)
    
    # Final results
    show_results(correct_count, total_questions, number, name, operation)

def show_results(correct, total, number, name, operation):
    """Display final results with celebration"""
    percentage = (correct / total) * 100
    operation_name = "MULTIPLICATION" if operation == 'M' else "DIVISION"
    
    print_color(f"\n\n{'='*60}", Colors.CYAN)
    print_color("🎊  RESULTS TIME!  🎊", Colors.YELLOW + Colors.BOLD)
    print_color(f"{'='*60}\n", Colors.CYAN)
    
    print_color(f"Great work, {name}! Here's how you did on {operation_name} with {number}:", Colors.BLUE)
    print_color(f"\n✓ Correct answers: {correct} out of {total}", Colors.GREEN + Colors.BOLD)
    print_color(f"✗ Incorrect answers: {total - correct} out of {total}", Colors.RED + Colors.BOLD)
    print_color(f"📊 Score: {percentage:.0f}%", Colors.CYAN + Colors.BOLD)
    
    # Performance feedback
    if percentage == 100:
        print_color("\n🏆 PERFECT SCORE! You're a MATH MASTER! 🏆", Colors.YELLOW + Colors.BOLD)
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
    print_color("Would you like to practice more math?", Colors.YELLOW + Colors.BOLD)
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
        operation = get_operation_choice()
        number = get_table_choice()
        practice_table(number, name, operation)
        
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