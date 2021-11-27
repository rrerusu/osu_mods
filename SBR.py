import os

# Move images into another folder and change name
def modify_image(folder_name):
    song_path = songs_path + "\\{}".format(folder_name)
    image = [i for i in os.listdir(song_path) if i[-4:] == ".jpg" or i[-4:] == ".png" or i[-5:] == ".jpeg"]
    image_path = song_path + "\\" + image[0]
    os.rename(image_path, move_imgs + "\\{} _ {}".format(folder_name, image[0]))


# Vars
songs_path = __file__[:-6] + "Songs"                        # Path for folders that contains songs
move_imgs = __file__[:-6] + "old_image"                     # Backup: Path for folder that will contain copies of images

# Collect list of songs (folders in Songs folder)
songs = [i for i in os.listdir(songs_path) if i != "1011011 nekodex - new beginnings"]

# Copy each image file into backup folder
for file in songs:
    modify_image(file)