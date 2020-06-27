import os
import sys
import webbrowser as wb

PROJECTS_PATH = "D:/Projects/"

if sys.argv[1] == "start":
    os.system("explorer")
    if sys.argv[2] == "play":
        wb.open_new("https://www.google.com/")
        wb.open("https://www.youtube.com/")
    elif sys.argv[2] == "work":
        if sys.argv[3] == "-o":
            proj_name = sys.argv[4]
            proj_dir = os.path.join(PROJECTS_PATH, proj_name)
            os.chdir(proj_dir)
            os.system("start cmd.exe")
            os.system("code .")
            os.system(f"echo {proj_name} opened.")
        else:
            print("Error Project Does Not Exist!!")
            proj_name = sys.argv[3]
            proj_dir = os.path.join(PROJECTS_PATH, proj_name)
            os.mkdir(proj_dir)
            os.chdir(proj_dir)
            os.system("start cmd.exe")
            os.system("code .")
            os.system(f"echo {proj_name} created.")
elif sys.argv[1] == "play":
    wb.open("https://www.youtube.com/", new=0)
    wb.open_new("https://www.google.com/")
elif sys.argv[1] == "work":
    if sys.argv[2] == "-o":
        proj_name = sys.argv[3]
        proj_dir = os.path.join(PROJECTS_PATH, proj_name)
        os.chdir(proj_dir)
        os.system("start cmd.exe")
        os.system("code .")
        os.system(f"echo {proj_name} opened.")
    else:
        print("Error Project Does Not Exist!!")
        proj_name = sys.argv[2]
        proj_dir = os.path.join(PROJECTS_PATH, proj_name)
        os.mkdir(proj_dir)
        os.chdir(proj_dir)
        os.system("start cmd.exe")
        os.system("code .")
        os.system(f"echo {proj_name} created.")
