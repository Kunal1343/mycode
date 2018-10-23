#!/usr/bin/env python3
hostname = input('Please enter Hostname:')
#hostname = 'MTG'
#if hostname == 'MTG':
# print('The hostname was found to be mtg')
##print('The hostname was found to be ' + hostname_input)
if hostname.lower() in ('mtg'):
  print('The hostname was found to be ' + hostname)
  print('Hostname matches expected config')
  print('Exiting the script')
else:
  print('Hostname does not match')
  print('exiting the script')
  exit()
