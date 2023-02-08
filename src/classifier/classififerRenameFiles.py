import os

def rename_files():
    folder = '/Users/laurentvergoz/Documents/GitHub/04_projet_afpar/BRIEF 2B/src/classifier/images/Train/tiramisu'
    counter = 1

    #for filename in os.listdir(folder):
        #if not filename.endswith(".jpg"):
            #os.rename(os.path.join(folder, filename), os.path.join(folder, filename + ".jpg"))

    for filename in os.listdir(folder):
        if filename.endswith('.jpg'):
            old_name = os.path.join(folder, filename)
            new_name = os.path.join(folder, 'tiramisu ({}).jpg'.format(counter))
            os.rename(old_name, new_name)
            counter += 1

if __name__ == '__main__':
    rename_files()

