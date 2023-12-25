import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io
import base64

class LogoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Logo Guessing Game")
        self.logos = {
            "E:\logo quize\logos\Amazon.png": "Amazon",
            "E:\logo quize\logos\Google.png": "Google",
            "E:\logo quize\logos\Facebook.png": "Facebook",
            "E:\logo quize\logos\IBM.png": "IBM",
            "E:\logo quize\logos\Mercedes.png": "Mercedes",
            "E:\logo quize\logos\Meta.png": "Meta",
            "E:\logo quize\logos\Patym.png": "Patym",
            "E:\logo quize\logos\Spotify.png": "Spotify",
            "E:\logo quize\logos\Starbucks.png": "Starbucks",
            "E:\logo quize\logos\Twitter.png": "Twitter",
            "E:\logo quize\logos\Wipro.png": "Wipro",
            "E:\logo quize\logos\Tesla.png": "Tesla",
            "E:\logo quize\logos\Apple.png": "Apple"
        }
        self.score = 0
        self.current_logo = None

        self.logo_label = tk.Label(root)
        self.logo_label.pack(pady=20)

        self.company_name_entry = tk.Entry(root, font=("Helvetica", 14))
        self.company_name_entry.pack(pady=20)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Logo", command=self.load_next_logo)
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.load_next_logo()

    def load_next_logo(self):
        logo_path = random.choice(list(self.logos.keys()))
        self.current_logo = logo_path
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((300, 200), Image.ANTIALIAS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        self.logo_label.config(image=logo_photo)
        self.logo_label.image = logo_photo

    def check_answer(self):
        user_answer = self.company_name_entry.get().strip().lower()
        correct_answer = self.logos[self.current_logo].lower()

        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Wrong answer. Correct answer is: {correct_answer}")

        self.score_label.config(text=f"Score: {self.score}")

root = tk.Tk()
game = LogoGame(root)
root.mainloop()

def main():
    score = 0
    num_questions = 5

    print("Welcome to the Logo Quiz Game!")
    print("Guess the company name based on the logo.")

    for _ in range(num_questions):
        logo_name = display_random_logo()

        user_guess = input("Enter your guess: ").strip().lower()

        if user_guess == logos[logo_name].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {logos[logo_name]}")

    print(f"Game Over! Your final score is: {score}/{num_questions}")

if __name__ == "__main__":
    main()
