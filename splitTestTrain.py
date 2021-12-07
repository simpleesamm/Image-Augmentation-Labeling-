import os
import random
import shutil

os.chdir("F:/augmentImages/Loose Silky-bent")
cwd = os.getcwd()
#cwd = "c:/Users/samue/OneDrive/Documents/Samuel_Studies/Y3 Sem 1/Machine Learning/Project/plant-seedlings-classification/Loose Silky-bent/Loose Silky Bent"
#print(cwd)
test_dir = 'train'
val_dir = 'valid'
os.mkdir(os.path.join(cwd,test_dir))
os.mkdir(os.path.join(cwd,val_dir))

file_list = []
train_test_split = (8, 2)  # define split
for file in os.listdir(cwd):
    if file.endswith('.png'):
        file_list.append(file)
random.shuffle(file_list)
num_files_train = 0
if 10 - train_test_split[0] == train_test_split[1]:
    num_files_train = (train_test_split[0] / 10) * len(file_list)

else:
    print('Pls split correctly!')

count = 0
if num_files_train != 0:
    while count < num_files_train:
        filename = file_list[count]
        file_dest = 'train/'+ filename
        shutil.copy2(filename,file_dest)
        count += 1
        print(count)
        
    print('done with training set')
    while count < len(file_list):
        filename = file_list[count]
        file_dest = 'valid/'+filename
        shutil.copy2(filename, file_dest)
        count += 1
        print(count)

    print('done with valid set')
