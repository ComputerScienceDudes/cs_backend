from email.header import Header
import os
import json
import time

class Survey_Entry:
    def __init__(self, Name, Age, Grade, Wants_College, Wants_Job):
        self.Name = Name
        self.Age = Age
        self.Grade = Grade
        self.Wants_College = Wants_College
        self.Wants_Job = Wants_Job

def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def BoolFromString(string):
    if string.lower() == "yes" or string.lower() == "y":
        return True
    elif string.lower() == "no" or string.lower() == "n":
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return BoolFromString(input("Please enter again: "))
    
def Get_Entry(Entry):
    ClearConsole()
    Entry.Name = input("Enter your name: ") 
    ClearConsole()
    Entry.Age = input("Enter your age: ")
    ClearConsole()
    Entry.Grade = input("Enter your grade: ")
    ClearConsole()
    Entry.Wants_College = BoolFromString(input("Do you want to go to college? (yes/no): "))
    ClearConsole()
    Entry.Wants_Job = BoolFromString(input("Do you want to get a job? (yes/no): "))
    ClearConsole()

# Start
Survey_File = open("Survey.json", "r+")

# Guarantee structure if file is empty
FirstChar = Survey_File.read(1)
Empty = (FirstChar == "" or FirstChar == -1)
if Empty:
    Survey_File.close()
    Survey_File = open("Survey.json", "w")
    Structure = {"Header": {"Name": "The Survey", "Entries": 0}, "Data": []}
    json.dump(Structure, Survey_File, indent=4)
Survey_File.close()

# Get survey data
Survey_File = open("Survey.json", "r+")
json_data = json.load(Survey_File)
Survey_File.close()

# Main loop
while True:
    ClearConsole()
    continue_survey = BoolFromString(input("Would you like to fill out the survey? (yes/no): "))
    if not continue_survey:
        exit()

    # Take survey
    Log = Survey_Entry("", "", "", False, False)
    Get_Entry(Log)

    json_data["Data"].append(Log.__dict__)
    json_data["Header"]["Entries"] = len(json_data["Data"])

    Survey_File = open("Survey.json", "w")
    json.dump(json_data, Survey_File, indent=4)
    Survey_File.close()
    
    ClearConsole()
    print(f"Thank you for your responses, {Log.Name}!")
    time.sleep(2)