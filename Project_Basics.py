"""
Import Spreadsheet with list of websites and Pass Phrases
Generate and save random numbers needed for password algorithm
Output:
Saved spreadsheet with website, pass phrases and random numbers
Saved spreadsheet with indices and pass words
Program enhancements to work on in the future: 
    1) add new passwords to these spreadsheets/files asking for user input
    2) modify/refresh passwords by regenerating random numbers but not indicies
    3) generate existing password with info just on the existing passcode file 
""" 
import csv
import random

def main():

    #Is this a new passphrase doc to modifyied passphrase doc
    print("Will you be starting a new passphrase file or modifying an existing one?")
    mission_usr=input("Enter 'new' or 'existing': ")
    print("")
    print("")
    print("csv files must be entered using the 'filename.csv' format")
    print("websites such as 'www.sitename.com' must be enterd as just 'Sitename'")
    print("")
    print("")

    if mission_usr == "new":
        #Import new base csv file
        print("You will be entering the name of the input file containing the columns 'Website' and 'Passphrase'")
        csv_input = input("Using the 'filenm.csv' format, provide your file's name here: ")
        generate_inputs( csv_input ,"algorthinputs.csv") #next iteration I'd like to add timestamp to file names

        print("You will be entering the desired name of the output file containing the columns 'idvalue' and 'password'")
        csv_output = input("Using the 'filenm.csv' format, provide your desired file name here: ")
        generate_keypwd("algorthinputs.csv", csv_output)

        print("Your passphase file is 'algorthinputs.csv'. Plase make a note of this for future additions and revisions")

    
    elif mission_usr == "existing":
        print("Currently developing capability-WIP")
     #Import existing passphrase csv file
        # print("You will be entering the name of the your existing passphrase file")
        # passphrase_file = input("Using the 'filenm.csv' format, provide your passphrase file's name here: ")
        
        # print("How would you like to modify your existing passphrase file?")
        # usr_action = int(input("Enter 1 to refresh an existing password, 2 to add a new website, 3 to lookup a password: "))
        
        # if usr_action == 1:
        #     print(f"Thank You for your selection! A refreshed password will be generated for a website and passcode in {passphrase_file}")
        #     site_of_change= input ("Enter the website for which you'd like a refreshed pasword")
        #     pwd_update(passphrase_file,site_of_chage)
        # elif usr_action == 2:
        #     print(f"Thank You for your selection! A new website and pass phrase will be added to {passphrase_file} and a password generated")
        #     new_site = input("Enter the website for which you'd like a new pasword: ")
        #     new_passphrase = input("Enter the passphrase for your new website")
        #     #pwd_addon(csv_input, new_site, new_passphrase)
        # elif usr_action == 3:
        #     print(f"Thank You for your selection! Your password generated from {passphrase_file} will be displayed")
        #     new_site = input("Enter the website for which you'd like to view your pasword: ")
        #     #pwd_algorithm(csv_input,new_site)


# def pwd_update(passphrase_file,site_of_chage)

#def pwd_addon(passcodefilenm, websitename, newpassphrase)


def pwd_algorithm(websitename, passphrase, coinflip, randnum):
    if coinflip == "1":
        pwd_nm = websitename[0:2]+randnum+websitename[2:]+passphrase.replace("a","@").replace("o","*").replace("s","$")
        pwd_nm = pwd_nm[4:18]
    else:
        pwd_nm = passphrase[0:4]+randnum+passphrase[4:]+websitename.replace("a","&").replace("i","!").replace("s","$")
        pwd_nm = pwd_nm[3:17]
    return pwd_nm

def generate_inputs(webpasscodecsv,algorithminputscsv):
    with open(f'{webpasscodecsv}','r') as csvinput:
        with open(f'{algorithminputscsv}', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            col_deets=[] #somewhere to put list of column names and additional lists of row by row data
            row = next(reader) #read the next row of file (i.e. the first row here for existing column names)
            #add names of additional columns
            row.append('coinflip') 
            row.append('randnum')
            row.append('idvalue') 

            col_deets.append(row)#list that now contains a list of columns as the first item

            for row in reader: #populate the items in the lists that correspond to the new column names
                row.append(random.randint(0, 1)) #generate a random coin flip
                row.append(random.randint(11, 99)) #generate random number x such that f(x) gets inserted into password
                row.append(random.randint(15000, 35000)) #generate a random key
                col_deets.append(row) # add in values for all cols of the new column names

            print (col_deets)

            writer.writerows(col_deets)

def generate_keypwd(algorithminputscsv, keypwdfilecsv):
        with open(f'{algorithminputscsv}','r') as csvinput:
            with open(f'{keypwdfilecsv}', 'w') as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)

                col_deets=[[next(reader)[4]]] #somewhere to put list of column names and additional lists of row by row data
                col_deets[0].append('password') #add the column name for passwords to the first list in the list ...madness O_o
                for row in reader: #populate password with very simplified algorithm
                    row.append(pwd_algorithm(row[0],row[1],row[2],row[3])) # take a section
                    
                col_deets.append([row[4],row[5]]) # add in values for all cols of the new column names
                
                print (col_deets)

                writer.writerows(col_deets)





if __name__ == '__main__':
    main()
