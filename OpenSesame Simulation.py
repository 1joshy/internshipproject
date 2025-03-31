import time
import os
from cryptography.fernet import Fernet

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def animated_intro():
    frames = [
        """
        
         
        """,
        """
        =======================================
         
        
        """,
        """
        =======================================
         WELCOME TO THE OPENSESAME RECRUIT SIM
        
        """,
        """
        =======================================
         WELCOME TO THE OPENSESAME RECRUIT SIM
        =======================================
        """
    ]
    for _ in range(1):
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(0.3)

def main():
    animated_intro()
    time.sleep(1)
    print("You have been selected to evaluate a new intern for the OpenSesame team: Me!")
    time.sleep(2)

    while True:
        print("\nWhere would you like to start?")
        print("1. Why I want to work at OpenSesame")
        print("2. Why I am interested in this internship?")
        print("3. What strengths and perspectives do I bring?")
        print("4. !!!Encryption Compliance Challenge!!!")
        print("5. Exit Simulation")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            why_opensesame()
        elif choice == "2":
            why_this_internship()
        elif choice == "3":
            my_strengths()
        elif choice == "4":
            encryption_challenge()
        elif choice == "5":
            print("\nMission Complete. Thank you for evaluating this recruit!")
            time.sleep(1)
            print("""
            ========================================
            | Security and compliance go hand in hand! |
            | I hope to contribute to these at OpenSesame. |
            ========================================
            """)
            time.sleep(4)
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
    
def why_opensesame():
    print("""
    [Why OpenSesame?]
    =================
    """)
    time.sleep(1)


    sentences = [
        "I want to work at OpenSesame because, you guys stand out as an innovator in learning and compliance solutions.",
        " ",
        "I watched your guys' video that was linked for inspiration on LinkedIn, and I really enjoyed the vibrant atmosphere and how everyone, and everything, radiated positivity.",
        "On top of that, your guys' main statement is that you HELP companies develop, which I think is something that is so important, yet many overlook.",
        " ",
        "So, when asked why I would want to work at OpenSesame, it is an easy answer, and all of these are reasons why.",
        "I have a lot of passion for my goals, and it seems like OpenSesame does as well."
    ]

    for sentence in sentences:
        print(sentence)
        time.sleep(4)

def why_this_internship():
    print("""
    [Why am I Interested in This Internship?]
    =========================================
    """)
    time.sleep(1)

    sentences = [
        "I think that most people on the side of tech often know how different it is when you go from school/studies to the real world. It can be a real pace change.",
        " ",
        "I am someone who is very invested in my learning and growing my skillset, and being able to apply that in a real-world setting is something that I really wish to do.",
        "Getting familiar with the ins-and-outs of what it is like to work with a company like yours is something that I am very, very interested in.",
        " ",
        "OpenSesame seems like a great place to do that, and I think that this internship would be a great opportunity for me to learn and grow from professionals and people I admire."
    ]

    for sentence in sentences:
        print(sentence)
        time.sleep(4)

def my_strengths():
    print("""
    [My Strengths and Perspectives I can bring to the Team]
    =======================================================
    """)
    time.sleep(1)

    sentences = [
        "I think of myself as someone who can adapt to any situation or environment.",
        "Do you need me to work on a task with a team? Perfect! I excel at teamwork, with constant communication and collaboration, I am a pro at working and bouncing off of others.",
        " ",
        "Do you need me to work on a task individually? Great! As much as I love working with others, I can also work independently just as well, as it gives me time and space to really focus on what's in front of me.",
        " ",
        "I am someone who is very open, and like anyone, I will make mistakes. However, what sets me apart from others is that I exponentially grow and learn from criticism, and I am someone who is not afraid to admit when I am wrong or need help.",
        " ",
        "Lastly, I am someone who is reliable, trustworty, and consistent. I know when to be serious and when to have fun, and I think that is a great balance to have."
    ]

    for sentence in sentences:
        print(sentence)
        time.sleep(4)

def encryption_challenge():
    key_phrase = "OpenSesame"
    cipher = Fernet(Fernet.generate_key())
    secret_message = "Data encryption is essential for compliance and security, and I'm ready to learn more about it!"
    encrypted_message = cipher.encrypt(secret_message.encode())

    print("""
    [Encryption Compliance Challenge]
    =================================
    You have received an encrypted message that must be decrypted to comply with
    data protection regulations (such as GDPR). Can you decrypt the message?
    """)
    time.sleep(4)
    print(f"Encrypted Message: {encrypted_message.decode()}")
    time.sleep(1)

    user_input = input("Enter the decryption key (Hint: What company is this position for?!?!): ")
    if user_input == key_phrase:
        print("\nCorrect! The decrypted message is:")
        print("\nDecrypting", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()
        time.sleep(1)
        print(secret_message)
    else:
        print("\nIncorrect key! Access denied.")

if __name__ == "__main__":
    main()