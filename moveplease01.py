#!/usr/bin/env python3
import shutil #import shutil utility for movig files
import os #import for OS level manipuilation
os.chdir('/home/student/mycode/')
shutil.move('raynor.obj', 'ceph_storage/')
xname = input('What is the new name for kerrigan.obj? ') #using imput to ask user for filename variable xname
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) #using it to rename with input provided

