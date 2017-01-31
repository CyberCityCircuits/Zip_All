# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:43:54 2016

@author: Admin
"""

#import libraries
import os
import shutil
import glob
import zipfile
from time import sleep

#set console size and color
os.system('mode con: cols=50 lines=28')
os.system('color F')
os.system('cls')
os.system('echo off')

#set varibles
version = '0.02.00'
splash_wait = 5
wait = .5
folder_bu = '!Archive'
cwd = os.getcwd()

#define commands
#splashscreen
def logo():  
    print ("    -----------------------------------------")
    print ("            01011010 01001001 01010000")
    print ("            ________  ______  _______")
    print ("           /        |/      |/       \\")
    print ("           $$$$$$$$/ $$$$$$/ $$$$$$$  |")
    print ("               /$$/    $$ |  $$ |__$$ |")
    print ("              /$$/     $$ |  $$    $$/")
    print ("             /$$/      $$ |  $$$$$$$/")
    print ("            /$$/____  _$$ |_ $$ |")
    print ("           /$$      |/ $$   |$$ |")
    print ("           $$$$$$$$/ $$$$$$/ $$/")
    print ("             ______   __        __")
    print ("            /      \ /  |      /  |")
    print ("           /$$$$$$  |$$ |      $$ |")
    print ("           $$ |__$$ |$$ |      $$ |")          
    print ("           $$    $$ |$$ |      $$ |")          
    print ("           $$$$$$$$ |$$ |      $$ |")          
    print ("           $$ |  $$ |$$ |_____ $$ |_____")
    print ("           $$ |  $$ |$$       |$$       |")     
    print ("           $$/   $$/ $$$$$$$$/ $$$$$$$$/")   
    print ("")
    print ("            01000001 01001100 01001100")
    print ("    -----------------------------------------")
    print ("                ZIP All V " + version)    
    print ("                   David A Ray")
    print ("     ")

#disclaimer
def disclaimer():
    os.system('cls')
    print ("")
    print ("")
    print ("")
    print ("  This program is designed to take a large")
    print ("  number of folders with datasets in them")
    print ("  and compress each one into a '.zip' file.")
    print ("")
    print ("  Be aware that using this software in a way")
    print ("  that it was not intended may lead to unintended")
    print ("  consequences.  Please understand this before")
    print ("  using this software.")
    print ("")
    print ("  ALL FILES CURRENTLY IN THE " + folder_bu + " FOLDER")
    print ("  WILL BE DELETED AND UNRECOVERABLE!!!")
    print ("")
    print ("  DO YOU UNDERSTAND?")
    print ("")
    confirm = raw_input("  Enter 'yes' to countinue: ")
    if confirm == ('yes') or confirm == ('YES') or confirm == ('Yes') or confirm == ('yES'):
        os.system('cls')        
        print ("  Zipping Each Folder and Moving Them to")        
        print ("  a Folder Named " + folder_bu + ".")
        print ("")
    else:
        end()
    
#end program
def end():
    print ("")
    print ("")
    print ("Program ending...")
   

#delete any existing archive
def del_bu():
    if os.path.exists(folder_bu):
        print ("  Deleting existing data in " + folder_bu + ".")
        shutil.rmtree(folder_bu)

#zip all folders
def zip_all():
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
                #size = os.path.getsize(f)
                #if size == 0:
                #    size = 1
                print " * " + subdir + "\\" + f
                fn = os.path.join(dirpath, f)
                zf.write(fn, arcname=f)        
                
                
#make archive folder
def mk_bu():
    print ("  Creating new " + folder_bu + " folder.")       
    if not os.path.exists(folder_bu):
        os.makedirs(folder_bu)


#copy zip to archive        
def copy_zip():
    print ("  Placing compressed data into " + folder_bu + ".")
    files = glob.iglob(os.path.join(cwd, "*.zip"))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, folder_bu)

def del_zip():
    files = [file for file in glob.glob("*.zip") if not file.endswith("0.zip")]
    for file in files:
        os.remove(file)
   
#run commands
if __name__ == "__main__":
    logo()
    sleep(splash_wait)
    disclaimer()
    sleep(wait)
    del_bu()
    sleep(wait)
    zip_all()
    sleep(wait)
    mk_bu()
    sleep(wait)
    copy_zip()
    sleep(wait)
    del_zip()
    os.system('pause')
    