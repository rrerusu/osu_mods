import shutil
import os


# Version: 1.0
# Capabilities:
#   * Change all song images in "Songs" folder to a single image
#   * Revert all song images to original image files


# Replace old images with new image and rename new image
def copy_new_image(new_image_path, old_image_path):
    shutil.copy(new_image_path, old_image_path)
    print("Changed image of {} to {}".format(old_image_path.split("\\")[-2], new_image_path.split("\\")[-1]))


# Determine path of image file
def determine_image_path(folder_name):
    song_path = songs_path + "\\{}".format(folder_name)
    image = [i for i in os.listdir(song_path) if i[-4:] == ".jpg" or i[-4:] == ".png" or i[-5:] == ".jpeg"]
    return song_path + "\\" + image[0]



# Single method to modify all images for all songs
def modify_songs_images(song_list):
    try:
        os.mkdir(move_imgs)
    except FileExistsError:
        pass
    input_img = "C:\\Users\\rrerusu\\Downloads\\Testing Folder\\change_image\\louis.jpg"                                # Path of image to use to change song images
    for song in song_list:
        try:
            old_img_path = determine_image_path(song)
            move_images(old_img_path, move_imgs)
            copy_new_image(input_img, old_img_path)
        except(FileExistsError):
            print("Image for {} is already modified.\n".format(song))


# Move images into another folder and change name
def move_images(old_image_path, backup_dir):
    folder_name = old_image_path.split("\\")[-2]
    os.rename(old_image_path, backup_dir + "\\{} _ {}".format(folder_name, old_image_path.split("\\")[-1]))
    print("Moved image of song: {}".format(folder_name))


# Revert changes to song's images
def revert_songs_images(song_list):
    image_list = os.listdir(move_imgs)
    if len(image_list) == 0:
        print("No images to revert")
    else:
        for image in image_list:
            indx = 0
            while song_list[indx] not in image:
                indx += 1
            if indx != -1:
                os.remove(determine_image_path(song_list[indx]))
                os.rename("{}\\{}".format(move_imgs, image), "{}\\{}\\{}".format(songs_path, song_list[indx], image[len(song_list[indx]) + 3:]))
                print("Image of {} reverted.".format(song_list[indx]))
            else:
                print("Image for {} was not changed".format(song_list[indx]))
        

choice = input("Enter 1 to replace, 2 to restore, and anything else to exit: ")
print("")

# Vars for both methods
# TODO: Get user input for song and image locations
# TODO: Check to make sure osu.exe is in folder (Safety)
move_imgs = __file__[:-6] + "old_image"                                                                             # Path of folder that contains backup of images
songs_path = __file__[:-6] + "Songs"                                                                                # Path of folders that contains songs
songs = [i for i in os.listdir(songs_path) if i != "1011011 nekodex - new beginnings"]                              # Collect list of songs (folders in Songs folder)

# Update ALL images to given image
if choice == "1":
    modify_songs_images(songs)
# Check each folder and return image back to location
elif choice == "2":
    revert_songs_images(songs)

print("Exiting")