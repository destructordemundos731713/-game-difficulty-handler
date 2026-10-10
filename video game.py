dificultad = {"dificultad" : "normal"}

seleciona_dificultad = input("escribe la dificultad que desea / type the difficulty you want: ")

if seleciona_dificultad == "dificultad":
    print("usted ya se encuentra en esta dificultad / you are already on this difficulty")
    print(dificultad)

elif seleciona_dificultad == "facil":
    print("usted a desidido cambiar de dificultad (facil) / you have decided to change the difficulty (easy)")
    dificultad["dificultad"] = "facil" 
    print(dificultad)

elif seleciona_dificultad == "dificil":
    print("usted a desidido cambiar de dificultad(dificil) / you have decided to change the difficulty (hard)")
    dificultad["dificultad"] = "dificil"  
    print(dificultad)
elif seleciona_dificultad == "normal":
    print("usted a desidido cambiar de dificultad(NORMAL) / you have decided to change the difficulty (NORMAL)")
    dificultad["dificultad"] = "normal"
    print(dificultad)

else:
    print("usted no es de este planeta / you are not from this planet")



