import pygame.mixer
import time
import os

def play_music(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        print(f"Playing: {os.path.basename(filepath)}")
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except pygame.error as e:
        print(f"Error playing music: {e}")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def pause_music():
    pygame.mixer.music.pause()
    print("Music paused.")

def unpause_music():
    pygame.mixer.music.unpause()
    print("Music unpaused.")

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

if __name__ == "__main__":
    print("--- Simple Music Player (requires pygame: pip install pygame) ---")
    print("Commands: play <filepath>, pause, unpause, stop, exit")
    print("Note: For 'play', provide a full path to an MP3 file.")

    while True:
        command_input = input("> ").split(maxsplit=1)
        cmd = command_input[0].lower()

        if cmd == "play":
            if len(command_input) == 2:
                filepath = command_input[1]
                play_music(filepath)
            else:
                print("Usage: play <filepath>")
        elif cmd == "pause":
            pause_music()
        elif cmd == "unpause":
            unpause_music()
        elif cmd == "stop":
            stop_music()
        elif cmd == "exit":
            stop_music()
            print("Exiting music player.")
            break
        else:
            print("Unknown command.")
