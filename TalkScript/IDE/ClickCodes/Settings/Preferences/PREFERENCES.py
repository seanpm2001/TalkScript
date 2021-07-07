# Start of script
""" Info
This file is a preferences page for click escape codes, one of the key features in voice-based programming.
"""
# Divider
''' Import section '''
# TKScript stands for TalkScript. The packages do not yet exist
import os
import voiceRecognitionTKScript
import readAloudTKScript
import clickModeForTKScript
import settings_TKScript
import language_TKScript
''' The program section '''
def readAloud():
  voiceRecognition = condition(on) # Turns voice recognition on
  readAloud.os.getlang() # Retrives the default system language for reading aloud
  readAloud.os.preferences.clickCodes("/OGG/EN_US/clickcodes1.ogg") # Starts the file that reads this page aloud. Needs to be modified to work in languages other than English
  break
def readAgain():
  return readAloud() # Repeats what was said
  break
def clickCodes_Settings_Preferences():
  # readAloud = bool(true)
  return readAloud()
  print ("Preferences for Click Escape codes")
  print ("Click escape codes are vocal codes that indicate that you want to enter punctuation, numbers, or other special characters into your program")
  print ("You can start changing your preferences now using your voice")
  print ("\nThe following preferences are allowed:\nCK (deep K sound)\nNo other codes available")
  break
return clickCodes_Settings_Preferences()
print ("You have exited the preference page for click escae codes. Going back to main settings page")
break
# End of script
""" File info
File type: Python 3 source file (*.py)
File version: 1 (Tuesday, July 6th 2021 at 6:12 pm)
Line count (including blank lines and compiler line): 40
"""
