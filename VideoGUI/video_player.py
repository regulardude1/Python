# video_player.py

import vlc
import tkinter as tk
from tkinter import Toplevel, Frame, Button

class VideoPlayer:
    def __init__(self, master, video_path):
        self.master = master
        self.video_path = video_path

        # Create a new window for the video player
        self.player_window = Toplevel(master)
        self.player_window.title("Video Player")

        # Create VLC player
        self.player = vlc.MediaPlayer(self.video_path)

        # Frame for video and controls
        self.video_frame = Frame(self.player_window)
        self.video_frame.pack()

        # Add video to frame
        self.player.set_fullscreen(True)  # Optional: Set to fullscreen if desired
        self.player.play()

        # Add controls
        self.setup_controls()

        # Close the player when window is closed
        self.player_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_controls(self):
        control_frame = Frame(self.player_window)
        control_frame.pack(fill="x")

        play_button = Button(control_frame, text="Play", command=self.play_video)
        play_button.pack(side="left")

        pause_button = Button(control_frame, text="Pause", command=self.pause_video)
        pause_button.pack(side="left")

        stop_button = Button(control_frame, text="Stop", command=self.stop_video)
        stop_button.pack(side="left")

        volume_up_button = Button(control_frame, text="Vol +", command=self.volume_up)
        volume_up_button.pack(side="left")

        volume_down_button = Button(control_frame, text="Vol -", command=self.volume_down)
        volume_down_button.pack(side="left")

    def play_video(self):
        self.player.play()

    def pause_video(self):
        self.player.pause()

    def stop_video(self):
        self.player.stop()

    def volume_up(self):
        volume = self.player.audio_get_volume()
        self.player.audio_set_volume(min(volume + 10, 100))

    def volume_down(self):
        volume = self.player.audio_get_volume()
        self.player.audio_set_volume(max(volume - 10, 0))

    def on_closing(self):
        self.player.stop()
        self.player_window.destroy()
