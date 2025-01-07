import os
import shutil
#written by superhenryman 1/7/2025
dir_path = os.path.dirname(os.path.realpath(__file__))
step1 = input("Please input the path of your log files: ")
print("Disclaimer: Please do not put the relative path and instead the absolute path of your log files.")
source_dir = rf"{step1}"

file_types = {
    'logs': ['.log']
}
for category, extensions in file_types.items():
    folder_created = False  # flag to check if a folder should be created
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            if file_extension.lower() in extensions:
                category_folder = os.path.join(source_dir, category)
                if not os.path.exists(category_folder):  # only create the folder if a file matches
                    os.makedirs(category_folder)
                    folder_created = True
                break  # stop checking other files once a match is found


for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    

    if os.path.isfile(file_path):
        _, file_extension = os.path.splitext(filename) 
        

        for category, extensions in file_types.items():
            if file_extension.lower() in extensions:  
                category_folder = os.path.join(source_dir, category)  
                
#idk man i only saw a guide :(
                shutil.move(file_path, os.path.join(category_folder, filename))
                break  
print(f"Finished writing to {source_dir}\\logs.")
print("Would you like to save the logs to one singular text file?(yes/no)")
decision = input().strip().lower()
if decision != "yes" and decision!= "no":
    print("Sorry, please write a correct answer next time.")
elif decision == "yes":
    logs_dir = os.path.join(source_dir, 'logs')
    combined_log_file = "combined_logs.txt"
    if not os.path.exists(logs_dir):
        print(f"No 'logs' folder found in {source_dir}.")
    try:
        with open(combined_log_file, "w") as f:
            for log_file in os.listdir(logs_dir):
                log_path = os.path.join(logs_dir, log_file)
                if os.path.isfile(log_path):
                    with open(log_path, "r") as ins:
                        f.write(ins.read())
                        f.write("\n")
        print(f"All logs written into {combined_log_file} in the folder {dir_path}")
        print()
    except Exception as e:
        print(f"Error when combining: {e}")
else:
    print("Done.")
    exit()