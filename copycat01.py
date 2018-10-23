#!/usr/bin/env python3
import shutil #Import Shutil module for file transfer related tasks
import os #import OS module for OS related manipulation
os.chdir('/home/student/mycode/') #allows to run script from anywhere , specify where the path is
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy') #shutil will copy the files
shutil.copytree('5g_research/', '5g_research_backup/') # shutil.copytree for directory and subdirectories

