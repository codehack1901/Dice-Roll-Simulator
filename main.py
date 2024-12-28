import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# Initialize the Tkinter window
root = tk.Tk()
root.title("Dice Roll Simulator")
root.geometry("800x1000")

# List of dice images (relative to the script directory)
dice = [
    "images/dice1.png", "images/dice2.png", "images/dice3.png",
    "images/dice4.png", "images/dice5.png", "images/dice6.png"
]

# Verify all dice images exist
missing_images = [img for img in dice if not os.path.exists(img)]
if missing_images:
    print("Error: Missing image files:", missing_images)
    print("Make sure the images folder contains dice1.png to dice6.png.")
    root.destroy()
    exit()

# Load initial images for both dice
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Create labels to display the dice images
label1 = tk.Label(root, image=image1)
label2 = tk.Label(root, image=image2)

# Position the labels
label1.place(x=100, y=200)
label2.place(x=400, y=200)

# Add labels for Player 1 and Player 2
player1_label = tk.Label(root, text="Player 1", font=("Helvetica", 16), bg="lightgray")
player2_label = tk.Label(root, text="Player 2", font=("Helvetica", 16), bg="lightgray")

# Position the player labels above the dice images
player1_label.place(x=180, y=150)
player2_label.place(x=480, y=150)

# Label to display the result
result_label = tk.Label(root, text="Who will win?", font=("Helvetica", 16))
result_label.place(x=320, y=550)

# Define the dice roll function
def dice_roll():
    # Roll two dice
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    
    # Load new images based on the rolled numbers
    new_image1 = ImageTk.PhotoImage(Image.open(f"images/dice{roll1}.png"))
    new_image2 = ImageTk.PhotoImage(Image.open(f"images/dice{roll2}.png"))
    
    # Update the images in the labels
    label1.configure(image=new_image1)
    label1.image = new_image1  # Keep a reference to avoid garbage collection
    
    label2.configure(image=new_image2)
    label2.image = new_image2  # Keep a reference to avoid garbage collection
    
    # Determine the winner based on the dice roll
    if roll1 > roll2:
        result_label.config(text="Player 1 Wins!", fg="green")
    elif roll2 > roll1:
        result_label.config(text="Player 2 Wins!", fg="red")
    else:
        result_label.config(text="It's a Tie!", fg="blue")

# Create the roll button with corrected font specification
button = tk.Button(root, text="Click To Roll", bg="grey", fg="black", font=("Times", 20, "bold"), command=dice_roll)
button.place(x=330, y=60)

# Run the Tkinter event loop
root.mainloop()
