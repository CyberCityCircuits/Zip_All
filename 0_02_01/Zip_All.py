# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:43:54 2016

@author: Admin
"""

#import libraries
import os
import sys
import shutil
import glob
import zipfile
from time import sleep
#import datetime as dt

#define varibles
application = ("Zip_All")
version = ("0.02.01")
name = ("David A Ray")
folder_bu = ("!Archive")

#define system varibles
cwd = os.getcwd()
width = 50
lines = 28
splash_wait = 5
wait = .5

cent_width = (width-1)

#define cosole size and color
os.system("mode con: cols=" + str(width) + " lines=" + str(lines))
os.system("color F")
os.system("cls")
os.system("echo off")

#define commands
def header():
    os.system("cls")
    print ()
    print ((application + " " + version).center(cent_width))
    print (name.center(cent_width))
    print ()
    sleep (1)

#splashscreen
def logo():  
    print ()
    print (("-----------------------------------------").center(cent_width))
    print (("01011010 01001001 01010000").center(cent_width))
    print (("        ________  ______  _______        ").center(cent_width))
    print (("       /        |/      |/       \\      ").center(cent_width))
    print (("       $$$$$$$$/ $$$$$$/ $$$$$$$  |      ").center(cent_width))
    print (("           /$$/    $$ |  $$ |__$$ |      ").center(cent_width))
    print (("          /$$/     $$ |  $$    $$/       ").center(cent_width))
    print (("         /$$/      $$ |  $$$$$$$/        ").center(cent_width))
    print (("        /$$/____  _$$ |_ $$ |            ").center(cent_width))
    print (("       /$$      |/ $$   |$$ |            ").center(cent_width))
    print (("       $$$$$$$$/ $$$$$$/ $$/             ").center(cent_width))
    print (("         ______   __        __           ").center(cent_width))
    print (("        /      \ /  |      /  |          ").center(cent_width))
    print (("       /$$$$$$  |$$ |      $$ |          ").center(cent_width))
    print (("       $$ |__$$ |$$ |      $$ |          ").center(cent_width))
    print (("       $$    $$ |$$ |      $$ |          ").center(cent_width))
    print (("       $$$$$$$$ |$$ |      $$ |          ").center(cent_width))
    print (("       $$ |  $$ |$$ |_____ $$ |_____     ").center(cent_width))
    print (("       $$ |  $$ |$$       |$$       |    ").center(cent_width))     
    print (("       $$/   $$/ $$$$$$$$/ $$$$$$$$/     ").center(cent_width))   
    print ()
    print (("01000001 01001100 01001100").center(cent_width))
    print (("-----------------------------------------").center(cent_width))
    print ((application + " V" + version).center(cent_width))
    print (("David A Ray").center(cent_width))
    print ()

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
    print ("  ALL FILES CURRENTLY IN THE " + folder_bu + " FOLDER")
    print ("  WILL BE DELETED AND UNRECOVERABLE!!!")
    print ()
    print ("  DO YOU UNDERSTAND?")
    print ()
    confirm = input("  Enter 'yes' to countinue: ")
    if confirm.lower() == ('yes') or confirm.lower() == ('y'):
        os.system('cls')        
        print ("  Zipping Each Folder and Moving Them to")        
        print ("  a Folder Named " + folder_bu + ".")
        print ()
    else:
        print ("  Invalid Entry")
        
        end()
    
#end program
def end():
    print ()
    print ("  Program ending...")
    sleep(wait)
    sys.exit()
   
#delete any existing archive
def del_bu():
    if os.path.exists(folder_bu):
        print ()
        print ("  Deleting existing data in " + folder_bu + ".")
        shutil.rmtree(folder_bu)

#zip all folders
def zip_all():
    print ()
    print ("  Compressing...  Please be patient...")
    dir = cwd  
    # get list of all subdirectories in the directory
    subdirs = [subdir for subdir in os.listdir(dir) if os.path.isdir(os.path.join(dir, subdir))]
    # create a zip archive for each subdirectory
    for subdir in subdirs:
        zf_name = subdir + ".zip"
        zf = zipfile.ZipFile(zf_name, mode='w')
        for dirpath,dirs,files in os.walk(os.path.join(dir, subdir)):
            for f in files:
                print (" * " + subdir + "\\" + f)
                fn = os.path.join(dirpath, f)
                zf.write(fn, arcname=f)
                sleep(.01)
                            
#make archive folder
def mk_bu():
    print ()
    print ("  Creating new " + folder_bu + " folder.")       
    if not os.path.exists(folder_bu):
        os.makedirs(folder_bu)

#writes readme file        

#copy zip to archive        
def copy_zip():
    print ()
    print ("  Placing compressed data into " + folder_bu + ".")
    files = glob.iglob(os.path.join(cwd, "*.zip"))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, folder_bu)

def del_zip():
    filelist = [ f for f in os.listdir(".") if f.endswith(".zip") ]
    for f in filelist:
        os.remove(f)
    print()
    print ("  Cleaning up...")
   
#run commands
if __name__ == "__main__":
    logo()
    sleep(splash_wait)
    disclaimer()
    sleep(wait)
    header()
    del_bu()
    sleep(wait)
    zip_all()
    sleep(wait)
    mk_bu()
    sleep(wait)
    copy_zip()
    sleep(wait)
    del_zip()
    end()
    