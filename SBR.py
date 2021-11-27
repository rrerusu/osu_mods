import shutil
import os


# Replace old images with new image and rename new image
def copy_new_image(new_image_path, old_image_path):
    shutil.copy(new_image_path, old_image_path)
    print("Changed image of {} to {}".format(old_image_path.split("\\")[-2], new_image_path.split("\\")[-1]))


# Check to see if image is modified or not
def is_image_modified(songs_folder, song_folder):
    return len([i for i in os.listdir(songs_folder) if i.rindex(song_folder) > 0 and i != "1011011 nekodex - new beginnings"]) > 0


# Move images into another folder and change name
def move_images(folder_name):
    song_path = songs_path + "\\{}".format(folder_name)
    image = [i for i in os.listdir(song_path) if i[-4:] == ".jpg" or i[-4:] == ".png" or i[-5:] == ".jpeg"]
    image_path = song_path + "\\" + image[0]
    os.rename(image_path, move_imgs + "\\{} _ {}".format(folder_name, image[0]))
    print("Moved image of song: {}".format(folder_name))
    return image_path



choice = input("Enter 1 to replace, 2 to restore, and anything else to exit: ")

# Vars for both methods
# TODO: Get user input for song and image locations
songs_path = __file__[:-6] + "Songs"                                                                                # Path of folders that contains songs
move_imgs = __file__[:-6] + "old_image"                                                                             # Path of folder that contains backup of images
input_img = "C:\\Users\\rrerusu\\Downloads\\Testing Folder\\change_image\\louis.jpg"                                # Path of image to use to change song images

if choice == "1":
    # Vars
    songs = [i for i in os.listdir(songs_path) if i != "1011011 nekodex - new beginnings"]                          # Collect list of songs (folders in Songs folder)

    # Change each image
    for file in songs:
        original_img_path = move_images(file)
        copy_new_image(input_img, original_img_path)
        print("")
elif choice == "2":
    pass

print("Exiting")