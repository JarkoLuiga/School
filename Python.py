def konsooli_print(tulemus): # funktsiooni deklaratsioon
    if tulemus < 20:
        for _ in range(tulemus): # nii mitu korda kui on tulemus prindin tulemust
            print("Tere!")

file1 = open("A.txt", "r") # avan esimese faili file1 = muutuja, funktsioon = open("A.txt", "r")
file2 = open("B.txt", "r") # avan teise faili
muutuja1 = int(file1.read()) # loen faili read funktsiooni kasutades loen faili ning muudan selle intiks
muutuja2 = int(file2.read()) # loen faili, see on argument (file2.read())
tulemus = muutuja1 + muutuja2 # muutuja väärtustamine

if tulemus > 1000000:
    tulemusfile = open("miljon2r.txt", "w") # loon uue faili
else:
    tulemusfile = open("tulemus.txt", "w") # loon uue faili

tulemusfile.write(str(tulemus)) # kirjutan tulemuse stringina, kirjutan selle write funktsiooni abil

konsooli_print(tulemus) # kutsun funktsiooni 

file1.close() # sulgen faili
file2.close() # sulgen faili
