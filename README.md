File-Organizer 

Introduction:

	The objective of the project is to build a python program that runs as a command-line tool. Basically, so many programmers create file on desktop for easy access. Myself also do the same thing, Due to a large number of files, it is a daunting task to sit and organize each file. To make that task easy, we use this Python script that comes in handy and returns a folder where all the files are organized in a well-manner within seconds. The script help’s you to organize files by size, date or even extensions. 


Modules used:

    • OS module:
      
          The OS module in python provides functions for interacting with the operating system. OS, comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.
	
    • shutil module:
      
          Shutil module in Python provides many functions of high-level operations on files and collections of files. It comes under Python's standard utility modules. This module helps in automating process of copying and removal of files and directories.
          
    • DateTime module:
		
		Checking the extension of the file in the computer directory and then comparing it with 			the dictionary values of extensions if matched then creating the new directory and inside 		it moving the different files according to the specified new directories.

Approach used:
          
    • Organizing files by size: 
      
          Checking the file size by using the if and elif conditions and then arranging the files into their specific folders by creating new directories as per the size of the files. All the files are first moved into (Organized Directory) then inside this folder all the other directories are created accordingly. files are arranged in the subsequent folders(BYTES, KB, MB, GB). 
          
      
      
      
    • Organizing files by date:

		The values of date and time for the files are taken and stored inside the directories. After 		finding out the days it has been stored, the files are then moved to different directories 			according to the number of days by comparing it using the if else conditional statements.

    • Organizing files by extensions:
		
		Checking the extension of the file in the computer directory and then comparing it with 			the dictionary values of extensions if matched then creating the new directory and inside 		it moving the different files according to the specified new directories.

Built using:
    1. Python language
    2. The code is built according to the standard pep8/flake8 rules and regulations.



