from tkinter import *
from tkinter import messagebox
import random

from PIL import Image, ImageTk
import pygame

pygame.mixer.init()

sound_rock = pygame.mixer.Sound('sounds/rock.aiff')
sound_paper = pygame.mixer.Sound('sounds/paper.wav')
sound_scissors = pygame.mixer.Sound('sounds/scissors.wav')
sound_win = pygame.mixer.Sound('sounds/tada.flac')
sound_lose = pygame.mixer.Sound('sounds/lose.wav')



def start_game():
    start_window.withdraw()


    game_window = Toplevel()
    game_window.geometry('500x600')
    game_window.title('Rock Paper Scissors')
    game_window.resizable(False, False)
    game_window.config(bg='black')

    user_score = 0
    computer_score = 0

    def update_score():
        score_label.config(text=f'Your Score: {user_score}\n Computer Score: {computer_score}')

    def play_round(user_choice):
        nonlocal user_score, computer_score
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        if user_choice == "rock":
            sound_rock.play()
        elif user_choice == "paper":
            sound_paper.play()
        elif user_choice == "scissors":
            sound_scissors.play()

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif(user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You Win!"
            user_score += 1
            sound_win.play()
        else:
            result = "You Lose!"
            computer_score += 1
            sound_lose.play()

        result_label.config(text=f"You chose {user_choice.capitalize()},\n\n and the Computer chose {computer_choice.capitalize()}.\n\n {result}")
        update_score()


    result_label = Label(game_window, text="", font=("Helvetica", 16), fg="white", bg="black")
    result_label.pack(pady=20)

    score_label = Label(game_window, text=f"Your Final score: {user_score} | Computer: {computer_score}", font=("Helvetica", 16), fg="white", bg="black" )
    score_label.pack(pady=10)


    prompt_label = Label(game_window, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 16), bg="black", fg="white")
    prompt_label.pack(pady=10)


    button_frame2 = Frame(game_window, bg="black")
    button_frame2.pack(pady=10)

    rockImg = ImageTk.PhotoImage(Image.open('images/rock.jpeg').resize((140,70)))
    paperImg = ImageTk.PhotoImage(Image.open('images/paper.jpeg').resize((140,70)))
    scissorsImg = ImageTk.PhotoImage(Image.open('images/scissors.jpeg').resize((140,70)))

    rock_btn = Button(button_frame2, image=rockImg, bd=0, bg="black", cursor="hand2", fg="black", command=lambda: play_round(user_choice="rock"))
    rock_btn.image = rockImg
    rock_btn.grid(row=0, column=0, padx=10, pady=10)

    paper_btn = Button(button_frame2, image=paperImg, bd=0, bg="black", cursor="hand2", fg="black", command=lambda: play_round(user_choice="paper"))
    paper_btn.image = paperImg
    paper_btn.grid(row=0, column=1, padx=10, pady=10)

    scissors_btn = Button(button_frame2, image=scissorsImg, bd=0, bg="black", cursor="hand2", fg="black", command=lambda: play_round(user_choice="scissors"))
    scissors_btn.image = scissorsImg
    scissors_btn.grid(row=0, column=3, padx=10, pady=10)

    def play_again():
        result_label.config(text="")

    play_btn = Button(game_window, text="Play Again", font=("Helvetica", 14), command=play_again, cursor="hand2", fg="black")
    play_btn.pack(pady=10)

    def back_to_main():
        game_window.destroy()
        start_window.deiconify()

    back_btn = Button(game_window, text="Back to Main Menu", font=("Helvetica", 14), command=back_to_main)
    back_btn.pack(pady=10)

    update_score()


start_window = Tk()
start_window.geometry('500x500')
start_window.resizable(False, False)
start_window.title('Rock Paper Scissors')
start_window.iconbitmap('images/icon-rock.png')

title_label = Label(start_window, text="Welcome to Rock Paper Scissors!", font=("Helvetica", 20), fg="white", bg="black")
title_label.pack(pady=20)


intro_img = ImageTk.PhotoImage(Image.open('images/rps.jpeg').resize((500, 300)))
img = Label(start_window, bd=0, bg="black", fg="black", image=intro_img)
img.pack(pady=10)

button_frame = Frame(start_window, bg='black')
button_frame.pack(pady=10)

startImage = Image.open('images/start.jpeg')
resize_start = startImage.resize((100, 60))
start_photo = ImageTk.PhotoImage(resize_start)
Button(button_frame, image=start_photo, text="AC", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: start_game()).grid(row=0, column=0, columnspan=2, padx=1, pady=1)

def confirm_exit():
    if messagebox.askyesno("Confirmation", "Do you want to exit?"):
        start_window.destroy()

exitImage = Image.open('images/exit.jpeg')
resize_exit = exitImage.resize((110, 60))
exit_photo = ImageTk.PhotoImage(resize_exit)
Button(button_frame, image=exit_photo, text="AC", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: confirm_exit()).grid(row=0, column=2,columnspan=2, padx=1, pady=1)


start_label= Label(button_frame, text='Start', fg="white", bg="black")
start_label.grid(row=1, column=0, columnspan=2, padx=1, pady=1)

exit_label= Label(button_frame, text='Exit', fg="white", bg="black")
exit_label.grid(row=1, column=2, columnspan=2, padx=1, pady=1)

start_window.config(bg='black')
start_window.mainloop()