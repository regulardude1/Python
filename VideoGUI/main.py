import os
import json
import tkinter as tk
from tkinter import filedialog, Frame, Label, Button, Canvas, Scrollbar
from media_helper import get_thumbnail, load_metadata, save_metadata, load_last_directory, save_last_directory, load_thumbnail
from video_player import VideoPlayer
from PIL import Image, ImageTk

# JSON files to store video metadata and last directory
METADATA_FILE = 'video_metadata.json'
DIRECTORY_FILE = 'last_directory.json'

# Play the selected video or open an image
def play_or_open_media(file_path):
    if file_path.endswith(('.mp4', '.avi', '.mkv', '.mov')):
        play_video(file_path)
    elif file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        open_image(file_path)

# Play the selected video using VLC
def play_video(video_path):
    VideoPlayer(root, video_path)

# Open the selected image in a new window
def open_image(image_path):
    image_window = tk.Toplevel(root)
    image_window.title("Image Viewer")

    img = Image.open(image_path)
    img = img.resize((600, 400))
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(image_window, image=img_tk)
    label.image = img_tk
    label.pack()

# Load videos and images from a folder
def load_media(directory):
    """Load media files from the specified directory."""
    # Clear existing buttons or media items from the UI
    clear_media_display()  # Implement this function to clear old media items
    
    for media_file in os.listdir(directory):
        media_path = os.path.join(directory, media_file)
        
        # Only process image files for thumbnails (modify as needed)
        if media_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            thumbnail = generate_thumbnail(media_path)  # Use the new function
            if thumbnail:
                btn = tk.Button(canvas_frame, image=thumbnail, command=lambda p=media_path: play_or_open_media(p), bd=0)
                btn.image = thumbnail  # Keep a reference to avoid garbage collection
                btn.pack(side=tk.LEFT)  # Adjust as needed for your layout
        else:
            # Handle other media types or skip
            continue

        # Clear existing thumbnails
        for widget in canvas_frame.winfo_children():
            widget.destroy()

        # Add media thumbnails in a grid layout
        row, col = 0, 0
        for media in media_files:
            media_path = os.path.join(directory, media)
            thumbnail = get_thumbnail(media_path)
            if thumbnail:
                btn = tk.Button(canvas_frame, image=thumbnail, command=lambda p=media_path: play_or_open_media(p), bd=0)
                btn.image = thumbnail
                btn.grid(row=row, column=col, padx=5, pady=5)

                media_name_label = tk.Label(canvas_frame, text=media, wraplength=100, bg='#4A4A4A', fg='white')
                media_name_label.grid(row=row + 1, column=col, padx=5, pady=(0, 5))

                col += 1
                if col > 4:
                    col = 0
                    row += 2

        # Update the canvas to fit the new content
        canvas_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

# Window manipulation functions
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_move(event):
    x = (event.x_root - root.x)
    y = (event.y_root - root.y)
    root.geometry(f"+{x}+{y}")

def start_resize(event):
    root.start_x = event.x
    root.start_y = event.y
    root.start_width = root.winfo_width()
    root.start_height = root.winfo_height()

def resize_window(event):
    new_width = root.start_width + (event.x - root.start_x)
    new_height = root.start_height + (event.y - root.start_y)
    root.geometry(f"{new_width}x{new_height}")

# Edit tags for the selected video
def edit_tags():
    selected_video = video_listbox.get(tk.ACTIVE)
    if not selected_video:
        return
    
    current_tags = metadata.get(selected_video, {}).get('tags', '')

    tag_window = tk.Toplevel(root)
    tag_window.title(f"Edit Tags for {selected_video}")
    
    tk.Label(tag_window, text="Tags:").pack()
    
    tag_entry = tk.Entry(tag_window, width=50)
    tag_entry.insert(0, current_tags)
    tag_entry.pack()
    
    def save_tags():
        new_tags = tag_entry.get()
        metadata[selected_video] = {'tags': new_tags}
        save_metadata(metadata)
        tag_window.destroy()

    tk.Button(tag_window, text="Save", command=save_tags).pack()

metadata = load_metadata()
directory = load_last_directory() or os.getcwd()

# GUI setup
root = tk.Tk()
root.title("Media Manager")
root.geometry("800x600")
root.configure(bg='#4A4A4A')
root.overrideredirect(True)  # Custom title bar

# Frame for the title bar and custom buttons
title_bar = Frame(root, bg='black', relief='raised', bd=0)
title_bar.pack(fill='x')

title_label = Label(title_bar, text="Media Manager", bg='black', fg='white', font=("Arial", 14))
title_label.pack(side="left", padx=10)

close_button = Button(title_bar, text='X', command=root.destroy, bg='black', fg='white', bd=0, font=("Arial", 14))
close_button.pack(side="right", padx=5)

maximize_button = Button(title_bar, text='□', command=lambda: root.state('zoomed'), bg='black', fg='white', bd=0, font=("Arial", 14))
maximize_button.pack(side="right")

minimize_button = Button(title_bar, text='–', command=root.iconify, bg='black', fg='white', bd=0, font=("Arial", 14))
minimize_button.pack(side="right")

# Bind hover effects
def on_enter(button):
    button['bg'] = '#8A8A8A'

def on_leave(button):
    button['bg'] = 'black'

for button in [close_button, minimize_button, maximize_button]:
    button.bind("<Enter>", lambda e, b=button: on_enter(b))
    button.bind("<Leave>", lambda e, b=button: on_leave(b))

# Bind window movement to the title bar
title_bar.bind("<Button-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", on_move)

# Resize grips
resize_grip = Frame(root, bg='gray', cursor="bottom_right_corner")
resize_grip.pack(side="bottom", anchor="se", fill="none")

resize_grip.bind("<Button-1>", start_resize)
resize_grip.bind("<B1-Motion>", resize_window)

# Frame for the buttons
button_frame = Frame(root, bg='#4A4A4A')
button_frame.pack(side="top", fill="x")

load_button = tk.Button(button_frame, text="Load Media", command=load_media, bg='#6A6A6A', fg='white', font=("Arial", 12))
load_button.pack(side="left", padx=5, pady=5)

edit_button = tk.Button(button_frame, text="Edit Tags", command=edit_tags, bg='#6A6A6A', fg='white', font=("Arial", 12))
edit_button.pack(side="left", padx=5, pady=5)

# Create a canvas with a scrollbar for thumbnails
canvas = Canvas(root, bg='#4A4A4A')
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

canvas_frame = Frame(canvas, bg='#4A4A4A')  # Ensure this is defined before any references
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Bind the canvas frame configuration to update the scroll region
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas_frame.bind("<Configure>", configure_canvas)

# Function for scrolling using mouse wheel
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

root.mainloop()
