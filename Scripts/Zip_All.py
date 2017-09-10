# -*- coding: utf-8 -*-
"""
Zip_All
David A Ray
David@DREAM-Enterprise.com
"""

#import libraries
import os
import sys
import shutil
import glob
from time import sleep

import var

#define cosole size and color
os.system("mode con: cols=" + str(var.width) + " lines=" + str(var.lines))
os.system("color F")
os.system("cls")
os.system("echo off")

#copy zip to archive        
def copy_zip():
    print ()
    print ("  Placing compressed data into " + var.folder_bu + ".")
    files = glob.iglob(os.path.join(var.cwd, "*.zip"))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, var.folder_bu)


#delete any existing archive
def del_bu():
    if os.path.exists(var.folder_bu):
        print ()
        print ("  Deleting existing data in " + var.folder_bu + ".")
        shutil.rmtree(var.folder_bu)

def del_zip():
    print ()
    print ("  Cleaning up...")
    filelist = [ f for f in os.listdir(".") if f.endswith(".zip") ]
    for f in filelist:
        os.remove(f)
    print()

#disclaimer
def disclaimer():
    os.system('cls')
    print ()
    print ()
    print ()
    print ()
    print ()
    print ()
    print ("  This program is designed to take a large")
    print ("  number of folders with datasets in them")
    print ("  and compress each one into a '.zip' file.")
    print ()
    print ("  Be aware that using this software in a way")
    print ("  that it was not intended may lead to unintended")
    print ("  consequences.  Please understand this before")
    print ("  using this software.")
    print ()
    print ()
    print ("  DO YOU UNDERSTAND?")
    print ()
    confirm = input("  Enter 'yes' to countinue: ")
    if confirm.lower() == ('yes') or confirm.lower() == ('y'):
        os.system('cls')        
        print ("  Zipping Each Folder and Moving Them to")        
        print ("  a Folder Named " + var.folder_bu + ".")
        print ()
    else:
        print ()
        print ("  Invalid Entry")
        sleep(.5)
        end()
    
#end program
def end():
    print ()
    print ("  Program ending...")
    sleep(var.wait)
    sys.exit()
    
#splashscreen
def logo():  
    print ()
    print (("-----------------------------------------").center(var.cent_width))
    print (("01011010 01001001 01010000").center(var.cent_width))
    print (("        ________  ______  _______        ").center(var.cent_width))
    print (("       /        |/      |/       \\      ").center(var.cent_width))
    print (("       $$$$$$$$/ $$$$$$/ $$$$$$$  |      ").center(var.cent_width))
    print (("           /$$/    $$ |  $$ |__$$ |      ").center(var.cent_width))
    print (("          /$$/     $$ |  $$    $$/       ").center(var.cent_width))
    print (("         /$$/      $$ |  $$$$$$$/        ").center(var.cent_width))
    print (("        /$$/____  _$$ |_ $$ |            ").center(var.cent_width))
    print (("       /$$      |/ $$   |$$ |            ").center(var.cent_width))
    print (("       $$$$$$$$/ $$$$$$/ $$/             ").center(var.cent_width))
    print (("         ______   __        __           ").center(var.cent_width))
    print (("        /      \ /  |      /  |          ").center(var.cent_width))
    print (("       /$$$$$$  |$$ |      $$ |          ").center(var.cent_width))
    print (("       $$ |__$$ |$$ |      $$ |          ").center(var.cent_width))
    print (("       $$    $$ |$$ |      $$ |          ").center(var.cent_width))
    print (("       $$$$$$$$ |$$ |      $$ |          ").center(var.cent_width))
    print (("       $$ |  $$ |$$ |_____ $$ |_____     ").center(var.cent_width))
    print (("       $$ |  $$ |$$       |$$       |    ").center(var.cent_width))     
    print (("       $$/   $$/ $$$$$$$$/ $$$$$$$$/     ").center(var.cent_width))   
    print ()
    print (("01000001 01001100 01001100").center(var.cent_width))
    print (("-----------------------------------------").center(var.cent_width))
    print ((var.name + " - " + var.build_date).center(var.cent_width))
    print (("David A Ray").center(var.cent_width))
    print ((var.email).center(var.cent_width))
    print ()
                            
#make archive folder
def mk_bu():
    print ()
    print ("  Creating new " + var.folder_bu + " folder.")       
    if not os.path.exists(var.folder_bu):
        os.makedirs(var.folder_bu)

#define commands
def header():
    os.system("cls")
    print ()
    print ((var.name).center(var.cent_width))
    print (var.email.center(var.cent_width))
    print ()
    sleep (1)

#zip all folders
def zip_all():
    print ()
    print ("  Compressing...  Please be patient...")
    dir = var.cwd  
    # get list of all subdirectories in the directory
    subdirs = [subdir for subdir in os.listdir(dir) if os.path.isdir(os.path.join(dir, subdir))]
    # create a zip archive for each subdirectory
    for subdir in subdirs:
        if subdir.startswith(var.folder_bu_base):
            if subdir == var.folder_bu:
                pass
            else:
                print ("  Skipping " + subdir)
            
        else:
            print ("  Compressing " + subdir)
            shutil.make_archive(subdir,
                                'zip',
                                dir,
                                subdir)
        
            shutil.copy2(subdir+".zip", var.folder_bu)
            os.remove(subdir+".zip")
        sleep(.01)
        
#run commands
if __name__ == "__main__":
    logo()
    sleep(var.splash_wait)
    #disclaimer()
    #sleep(var.wait)
    header()
    #del_bu()
    #sleep(var.wait)
    mk_bu()
    sleep(var.wait)
    zip_all()
    sleep(var.wait)
    #copy_zip()
    #sleep(var.wait)
    #del_zip()
    end()
    