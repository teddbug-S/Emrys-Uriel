# importing the needed modules
import os
import sys

# printing some banner and options
print('{:-^167}'.format('Welcome To Oz Files Master'))
print('\nAuthor: Tedd Bug\tUnicorn Code ©2020 All Rights Reserved.\n')
print("\nSelect a file type to search\n[1]--MP4 files"
      "\t[2]--MP3 files\n[3]--PDF files\t[4]--Text files".expandtabs(8))
print("[5]--MKV files\t[6]--Exe files\n[7]--Apk files\t[8]--Zip files\n[9]--ISO files\t[0]--Exit".expandtabs(8))

# prompting for file types to search
file_type = input('\noz_files>_ ')
# this is my storage path actually you can change it to fit yours
root_storage = "D:\\"
# if option 1
if file_type == '1':
     # list for storing the mp4 files for counting
    mp4_check = []
     # printing some title
    print('\n{:_^35}\n'.format('Information On MP4 Files'))
    print('File Name\tFile Size'.expandtabs(28))
    # using os.walk to walk through the whole sorage path
    # it's actually slow, do you have a faster alternative?
    result = list(os.walk(root_storage))
    # it returns a lot of lists of three items, current dir path(list), subdirs in that dir(list) and files in the current dir(tuple)
    # so I'm looping through all the lists
    for paths in result:
        # looping through all files in each list returned 
        for file in paths[2]:
            # since the os.path.get_size doesn't accept back slashes I'm changing them to forward slashes at same time concatenating with file name
            full_path = paths[0].replace('\\', '/') + '/' + file
            # making sure we take only '.mp4' files as that is the first option
            if full_path.endswith('.mp4'):
                # appending them to the list
                mp4_check.append(file)
                 # calling os.path.get_size on the full path, returns size in bytes
                file_size_b = os.path.getsize(full_path)
                 # converting size to kb
                file_size_kb = file_size_b / 1024
                  # converting size to mb
                file_size_mb = file_size_b / 1024 / 1024
                # doing some simple logic as to what size of measurement to use for each file
                # and also I've shortened the file names to 18 chars in printing it so that it can match the display 
                if file_size_mb >= 0.10:
                    print("{}...mp4\t{:.2f} MB".format(file[:18].strip('.mp4'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}...mp4\t{:.2f} KB".format(file[:18].strip('.mp4'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}...mp4\t{:.2f} B".format(file[:18].strip('.mp4'), file_size_b).expandtabs(28))
    # if mp4 list not empty
    if mp4_check:
        print(f'\nTotal number of Mp4 files is {len(mp4_check)}.')
    else:
        print('There are no mp4 files.')

 # actually, same applies to all the other file types
# try optimizing the code maybe there are some simple steps better than what I used
            
elif file_type == '2':
    mp3_check = []
    print('\n{:_^35}\n'.format('Information On MP3 Files'))
    print('File Name\tFile Size'.expandtabs(28))
    result = list(os.walk(root_storage))
    for paths in result:
        for file in paths[2]:
            full_path = paths[0].replace('\\', '/') + '/' + file
            if full_path.endswith('.mp3'):
                mp3_check.append(file)
                file_size_b = os.path.getsize(full_path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                if file_size_mb >= 0.10:
                    print("{}...mp3\t{:.2f} MB".format(file[:18].strip('.mp3'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}...mp3\t{:.2f} KB".format(file[:18].strip('.mp3'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}...mp3\t{:.2f} B".format(file[:18].strip('.mp3'), file_size_b).expandtabs(28))

    if mp3_check:
        print(f'\nTotal number of MP3 files is {len(mp3_check)}.')
    else:
        print('There are no mp3 files.')

elif file_type == '3':
    pdf_check = []
    print('\n{:_^35}\n'.format('Information On PDF Files'))
    print('File Name\tFile Size'.expandtabs(28))
    result = list(os.walk(root_storage))
    for paths in result:
        for file in paths[2]:
            full_path = paths[0].replace('\\', '/') + '/' + file
            if full_path.endswith('.pdf'):
                pdf_check.append(file)
                file_size_b = os.path.getsize(full_path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                if file_size_mb >= 1.00:
                    print("{}...pdf\t{:.2f} MB".format(file[:18].strip('.pdf'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:  # if megabytes is less than or equal to 0.10 use kb
                    print("{}...pdf\t{:.2f} KB".format(file[:18].strip('.pdf'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:  # if kb too is less that 0.10 then use bytes
                    print("{}...pdf\t{:.2f} B".format(file[:18].strip('.pdf'), file_size_b).expandtabs(28))

    if pdf_check:
        print(f'\nTotal number of PDF files is {len(pdf_check)}.')
    else:
        print('There are no pdf files.')

elif file_type == '4':
    txt_check = []
    print('\n{:_^35}\n'.format('Information On Text Files'))
    print('File Name\tFile Size'.expandtabs(28))
    result = list(os.walk(root_storage))
    for paths in result:
        for file in paths[2]:
            full_path = paths[0].replace('\\', '/') + '/' + file
            if full_path.endswith('.txt'):
                file_size_b = os.path.getsize(full_path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                txt_check.append(file)
                if file_size_mb >= 0.10:
                    print("{}...txt\t{:.2f} MB".format(file[:18].strip('.txt'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}...txt\t{:.2f} KB".format(file[:18].strip('.txt'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}...txt\t{:.2f} B".format(file[:18].strip('.txt'), file_size_b).expandtabs(28))
    if txt_check:
        print(f'Total number of text files is {len(txt_check)}')
    else:
        print('There are no text files here')

elif file_type == '5':
    mkv_check = []
    print('\n{:_^35}\n'.format('Information On MKV Files'))
    print('File Name\tFile Size'.expandtabs(28))
    result = list(os.walk(root_storage))
    for paths in result:
        for file in paths[2]:
            full_path = paths[0].replace('\\', '/') + '/' + file
            if full_path.endswith('.mkv'):
                file_size_b = os.path.getsize(full_path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                mkv_check.append(file)
                if file_size_mb >= 0.10:
                    print("{}...mkv\t{:.2f} MB".format(file[:18].strip('.mkv'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}...mkv\t{:.2f} KB".format(file[:18].strip('.mkv'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}...mkv\t{:.2f} B".format(file[:18].strip('.mkv'), file_size_b).expandtabs(28))
    if mkv_check:
        print(f'Total number of MKV files is {len(mkv_check)}')
    else:
        print('There are no MKV files here')

elif file_type == '6':
    exe_check = []
    print('\n{:_^35}\n'.format('Information On Exe Files'))
    print('File Name\tFile Size'.expandtabs(28))
    result = list(os.walk(root_storage))
    for paths in result:
        for file in paths[2]:
            full_path = paths[0].replace('\\', '/') + '/' + file
            if full_path.endswith('.exe'):
                file_size_b = os.path.getsize(full_path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                exe_check.append(file)
                if file_size_mb >= 0.10:
                    print("{}...exe\t{:.2f} MB".format(file[:18].strip('.exe'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}...exe\t{:.2f} KB".format(file[:18].strip('.exe'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}...exe\t{:.2f} B".format(file[:18].strip('.exe'), file_size_b).expandtabs(28))
    if exe_check:
        print(f'Total number of exe files is {len(exe_check)}')
    else:
        print('There are no exe files here')

elif file_type == '7':
    apk_check = []
    print('\n{:_^35}\n'.format('Information On APK Files'))
    print('File Name\tFile Size'.expandtabs(28))
    result = list(os.walk(root_storage))
    for paths in result:
        for file in paths[2]:
            full_path = paths[0].replace('\\', '/') + '/' + file
            if full_path.endswith('.apk'):
                file_size_b = os.path.getsize(full_path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                apk_check.append(file)
                if file_size_mb >= 0.10:
                    print("{}...apk\t{:.2f} MB".format(file[:18].strip('.apk'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}...apk\t{:.2f} KB".format(file[:18].strip('.apk'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}...apk\t{:.2f} B".format(file[:18].strip('.apk'), file_size_b).expandtabs(28))
    if apk_check:
        print(f'Total number of APK files is {len(apk_check)}')
    else:
        print('There are no APK files here')

elif file_type == '8':
    zip_check = []
    print('\n{:_^35}\n'.format('Information On Zip Files'))
    print('File Name\tFile Size'.expandtabs(28))
    result = list(os.walk(root_storage))
    for paths in result:
        for file in paths[2]:
            full_path = paths[0].replace('\\', '/') + '/' + file
            if full_path.endswith('.zip'):
                file_size_b = os.path.getsize(full_path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                zip_check.append(file)
                if file_size_mb >= 0.10:
                    print("{}...zip\t{:.2f} MB".format(file[:18].strip('.zip'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}...zip\t{:.2f} KB".format(file[:18].strip('.zip'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}...zip\t{:.2f} B".format(file[:18].strip('.zip'), file_size_b).expandtabs(28))
    if zip_check:
        print(f'Total number of Zip files is {len(zip_check)}')
    else:
        print('There are no Zip files here')

elif file_type == '9':
    iso_check = []
    print('\n{:_^35}\n'.format('Information On Iso Files'))
    print('File Name\tFile Size'.expandtabs(28))
    result = list(os.walk(root_storage))
    for paths in result:
        for file in paths[2]:
            full_path = paths[0].replace('\\', '/') + '/' + file
            if full_path.endswith('.iso'):
                file_size_b = os.path.getsize(full_path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                iso_check.append(file)
                if file_size_mb >= 0.10:
                    print("{}...iso\t{:.2f} MB".format(file[:18].strip('.iso'), file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}...iso\t{:.2f} KB".format(file[:18].strip('.iso'), file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}...iso\t{:.2f} B".format(file[:18].strip('.iso'), file_size_b).expandtabs(28))
    if iso_check:
        print(f'Total number of iso files is {len(iso_check)}.')
    else:
        print('There are no iso files here.')

elif file_type == '0':
    sys.exit('!!{:-^36}!!'.format('GoodBye'))
