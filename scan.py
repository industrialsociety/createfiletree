import os

def list_music_directory(directory):
    music_structure = []

    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            album_path = os.path.join(root, dir_name)
            album_tracks = []
            
            for file_name in os.listdir(album_path):
                if os.path.isfile(os.path.join(album_path, file_name)):
                    album_tracks.append(file_name)
            
            # Sort tracks
            album_tracks.sort()
            music_structure.append((dir_name, album_tracks))
    
    return music_structure

def save_to_file(music_structure, output_file):
    with open(output_file, 'w') as f:
        for album, tracks in music_structure:
            f.write(f"[{album}]\n")
            for i, track in enumerate(tracks, 1):
                f.write(f"{i}. {track}\n")
            f.write("\n")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    output_file = "music_hierarchy.txt"
    
    music_structure = list_music_directory(current_directory)
    save_to_file(music_structure, output_file)
    
    print(f"Music hierarchy saved to {output_file}")
