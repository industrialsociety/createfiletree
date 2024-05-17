import os
import re

def list_music_albums(directory):
    albums = []

    for root, dirs, _ in os.walk(directory):
        for dir_name in dirs:
            match = re.match(r'\[(\d{4})\]\s*(.*)', dir_name)
            if match:
                year = int(match.group(1))
                album_name = match.group(2)
                albums.append((year, album_name, dir_name))

    return sorted(albums, key=lambda x: x[0])

def save_to_file(albums, output_file):
    with open(output_file, 'w') as f:
        for i, (year, album_name, dir_name) in enumerate(albums, 1):
            f.write(f"{i}. [{year}] {album_name}\n")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    output_file = "albums_chronological.txt"
    
    albums = list_music_albums(current_directory)
    save_to_file(albums, output_file)
    
    print(f"Albums list saved to {output_file}")
