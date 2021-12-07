import os

def rename():
    full_path = 'F:/augmentImages/Loose silky-bent/valid/'
    rename_type = 'valid' # or valid
    for count,filename in enumerate(os.listdir(full_path)):
        if filename.endswith('.png'):
            dst = rename_type + "_CommonWheat_" + str(count) + ".png"
            src = full_path + filename
            dst = full_path + dst

            # rename() function will
            # rename all the files
            os.rename(src, dst)
    print('rename done!')
rename()