import panelUpdating
import time

# tsoFile = open("TSO.txt", "r+")
# checkingFile = tsoFile.read()

Program_runs = True
while Program_runs:
    print("Choose what do you want to do! ")
    time.sleep(0.2)
    print("\na) check whether a certain gene is in the TSO")
    print("b) check whether a certain gene is in the TS cardio")
    print("c) update a HPO database (TSO)")
    print("d) update a HPO database (TS cardio)\n")
    print("To quit, press 'q'!")
    time.sleep(0.2)
    selection = input("\nEnter your selection: ")
    selection = selection.lower()
    if selection == 'a':
        while True:
            geneOfChoice = input("Enter the name of the gene you want to check whether is in the TSO or not: ")
            if panelUpdating.checkingGene(geneOfChoice) == 0:
                print("(✓) Gene " + geneOfChoice.upper() + " is in the TSO file.")
            else:
                print("(x) Gene " + geneOfChoice.upper() + " is NOT in the TSO file.")
            selectionCheck = input("\nDo you want to check for another gene? [y/n] ")
            selectionCheck.lower()
            if selectionCheck == 'y':
                continue
            if selectionCheck == 'n':
                break
        time.sleep(0.2)
        print("\nExiting the program...")
        break
    if selection == 'q':
        time.sleep(0.2)
        print("\nExiting the program...")
        break
    if selection == 'b':
        while True:
            geneOfChoice = input("Enter the name of the gene you want to check whether is in the cardio TS or not: ")
            if panelUpdating.checkingGeneInCardio(geneOfChoice) == 0:
                print("(✓) Gene " + geneOfChoice.upper() + " is in the TSO file.")
            else:
                print("(x) Gene " + geneOfChoice.upper() + " is NOT in the TSO file.")
            selectionCheck = input("\nDo you want to check for another gene? [y/n] ")
            selectionCheck.lower()
            if selectionCheck == 'y':
                continue
            if selectionCheck == 'n':
                break
        time.sleep(0.2)
        print("\nExiting the program...")
        break
    if selection == 'c':
        print()
        input("Copy the gene list to the 'panel.txt' file (Each gene has to be written in its own line).\n"
              "Press ENTER to update!\n")
        panelUpdating.genesInTSO()
        panelUpdating.genesInPanel()
        panelUpdating.updating()
        print()
        while True:
            try:
                selection = input("Would you like the terminal to print out the missing and non-missing genes? [y/n] ").upper()
                if selection == 'Y':
                    while True:
                        try:
                            selection = input("a) 'missingGenes.txt'\n"
                                              "b) 'nonMissingGenes.txt'\n"
                                              "Select which file would you like to print out in terminal. ").upper()
                            if selection == 'A':
                                print("\nYou have selected 'missingGenes.txt' file. Here are the genes!\n")
                                time.sleep(1)
                                file = open("missingGenes.txt", "r")
                                content = file.read()
                                print(content)
                                file.close()
                                break
                            if selection == 'B':
                                print("\nYou have selected 'nonMissingGenes.txt' file. Here are the genes!\n")
                                time.sleep(1)
                                file = open("nonMissingGenes.txt", "r")
                                content = file.read()
                                print(content)
                                file.close()
                                break
                            else:
                                print("\n(x) Invalid input!\n")
                                time.sleep(0.2)
                        except ValueError:
                            continue
                if selection == 'N':
                    break
            except ValueError:
                continue
        break
    if selection == 'd':
        print()
        input("Copy the gene list to the 'panel.txt' file (Each gene has to be written in its own line).\n"
              "Press ENTER to update!\n")
        panelUpdating.genesInTScardio()
        panelUpdating.genesInPanel()
        panelUpdating.updatingTScardio()
        print()
        while True:
            try:
                selection = input("Would you like the terminal to print out the missing and non-missing genes? [y/n] ").upper()
                if selection == 'Y':
                    while True:
                        try:
                            selection = input("a) 'missingGenes.txt'\n"
                                              "b) 'nonMissingGenes.txt'\n"
                                              "Select which file would you like to print out in terminal. ").upper()
                            if selection == 'A':
                                print("\nYou have selected 'missingGenes.txt' file. Here are the genes!\n")
                                time.sleep(1)
                                file = open("missingGenes.txt", "r")
                                content = file.read()
                                print(content)
                                file.close()
                                break
                            if selection == 'B':
                                print("\nYou have selected 'nonMissingGenes.txt' file. Here are the genes!\n")
                                time.sleep(1)
                                file = open("nonMissingGenes.txt", "r")
                                content = file.read()
                                print(content)
                                file.close()
                                break
                            else:
                                print("\n(x) Invalid input!\n")
                                time.sleep(0.2)
                        except ValueError:
                            continue
                if selection == 'N':
                    break
            except ValueError:
                continue
        break
    else:
        print("\nInvalid selection!\n")
        continue
