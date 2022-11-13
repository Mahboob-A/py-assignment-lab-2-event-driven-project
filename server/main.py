
""" 
Py week 06 | Exam Event Driven Programme
Copy only txt file, and run the py file
Exam no 05 | 121122, Saturday, 10.00 am 
"""


import glob
import shutil
from os import remove, path, rmdir, mkdir



source_path = '../source/*'
destination_path = '../destination/'
postfix_numbers = [1, 2, 3]

# writing the lines
# with open(source_object[0], 'a') as file:
#         for line in range(0, 30):
#                 file.write(f'This is line {str(line)}.')

while True:

        source_object = glob.glob(source_path)
        if source_object:
                for object in range(len(source_object)):
                        object_path = source_object[object]   # str  ../source\source_file.txt
                        object_name = object_path.split('\\')[1].split('.')
                        
                        # using os.path
                        # file_path, object_name = path.split(object_path)  
                        # print("4. File Path: ",file_path)
                        # print("5. Object Name2: ", object_name.split('.'))

                        prefix_name = object_name[0]
                        postfix_name = object_name[1]
                        # print("File Name: ", prefix_name)   # source_file path 
                        # print("File Extension: ", postfix_name, "\n")  # txt / py 
                        
                        # handling txt files 
                        if postfix_name == 'txt':
                                # only create temp folders when the txt files have >= 30 lines 
                                with open(object_path, 'r') as file:
                                        if len(file.readlines()) >= 30:
                                                # temp folder to hold the txt file 
                                                mkdir('storeFile')  
                                                # temp folder to make all the files zip using shuilt make_archive
                                                mkdir('ziptemp')    

                                                # copying the file to temp folder
                                                shutil.copy(object_path, './storeFile/demo.txt')   
                                                # copied txt file in server
                                                copied_txt_file_in_server = './storeFile/demo.txt'  
                                                # temp zip folder path
                                                internal_zip_temp_path = './ziptemp'    
                                                
                                                # rename the files 
                                                for postfix_value in range(len(postfix_numbers)):
                                                        file_name = prefix_name + '_' + str(postfix_numbers[postfix_value]) + '.' + postfix_name

                                                        # copying the copied file in server's temp zip folder 
                                                        shutil.copy(copied_txt_file_in_server, f'{internal_zip_temp_path}/{file_name}')   

                                                # reading the copied file from server's storeFile folder 
                                                with open(copied_txt_file_in_server, 'r') as file:
                                                        lines = file.readlines()

                                                # distributing the file contents with i * 10 lines per file 
                                                for textfile_num in range(len(postfix_numbers)):
                                                        # opening the file
                                                        with open(f'{internal_zip_temp_path}/{prefix_name}_{textfile_num+1}.{postfix_name}', 'r+') as file:  
                                                                # deleting the old data
                                                                file.truncate()   
                                                                for line in range((textfile_num+1)*10): # taking i*10 lines 
                                                                        file.write(lines[line])  # wrinting i * 10 lines to each textfile_num'th file 

                                                # making zip the entire file 
                                                shutil.make_archive('zippedfile', 'zip', internal_zip_temp_path)

                                                # copying the zipped file to destination path
                                                shutil.copy(f'./zippedfile.zip', destination_path)   
                                                # unzipping the file in destination folder
                                                shutil.unpack_archive('zippedfile.zip', destination_path)  

                                                # removing the zip file from destionation folder
                                                remove(f'{destination_path}zippedfile.zip')  
                                                # removing zip file from server folder
                                                remove('./zippedfile.zip')   
                                                # deleting ziptemp folder from server folder
                                                shutil.rmtree(internal_zip_temp_path)  
                                                # deleting temp folder to hold the txt file from server folder
                                                shutil.rmtree('./storeFile')   
                                        else:
                                                # raise ValueError('txt file has less than 30 lines')
                                                print(f"{prefix_name +'.'+ postfix_name} file must contain 30 lines\n")
                                                
                        # handling py files 
                        if postfix_name == 'py':
                                try:
                                        # making a folder to hold the py script 
                                        mkdir('storePy')  
                                # if file exist error occurs  
                                except Exception:   
                                        # print(f"Process for Py script {prefix_name+'.'+postfix_name } could not be done for existing same folder") # need not to print anymore as copying the stuffs here 
                                        # deleting the old py script 
                                        remove('./storePy/demo.py')
                                        # copying the new py sctipt 
                                        shutil.copy(object_path, './storePy/demo.py')
                                        copied_py_in_server = './storePy/demo.py'
                                else:  # else woks when try did not rasie any error 
                                        # copying it to temp folder
                                        shutil.copy(object_path, './storePy/demo.py')   
                                        # file path of the py file
                                        copied_py_in_server = './storePy/demo.py' 

                                # running the code 
                                try:
                                        with open(copied_py_in_server) as file:
                                                script = compile(file.read(), "copied_py_in_server", 'exec')
                                                print(f"Py script {prefix_name+'.'+postfix_name } is running")
                                                exec(script)
                                                print(f"Py script {prefix_name+'.'+postfix_name } excution ended\n")
                                except FileNotFoundError:
                                        print(f"As directory not found Py script {prefix_name+'.'+postfix_name } is deleted\n")
                                        remove(copied_py_in_server)
                                except Exception:
                                        print(f"Py script {prefix_name+'.'+postfix_name } has error in it. It did not run in shell\n")
                                # deleting the temp folder to hold the py file 
                                shutil.rmtree('./storePy')
                 
                        
                # deleting all the files from the source 
                for object in range(len(source_object)):
                        object_path = source_object[object]
                        remove(object_path)


                # try:  to run the secondary script does not work 
                # exec(copied_py_in_server)
                # # except SystemExit:
                # #         pass 