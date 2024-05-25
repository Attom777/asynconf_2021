# HALLOWEEN - EXERCICE 2

# ================== FUNCTIONS ==================

def getData(variable):
    
    return int(input("Donnez le [ {} ] : ".format(variable)))

# ================== MAIN ================== 

#Initialisazion of user's variables
villasNumber = 0
housesNumber = 0
basementsNumber = 0

mummiesNumber = 0
vampiresNumber = 0
ghostsNumber = 0

mummiesCandy = 0
vampiresCandy = 0
ghostsCandy = 0

#Get user's data
villasNumber = getData("Nombres de villas")
housesNumber = getData("Nombres de maisons")
basementsNumber = getData("Nombres d'appartement")

mummiesNumber = getData("Nombres de momies")
vampiresNumber = getData("Nombres de vampires")
ghostsNumber = getData("Nombres de fantômes")

#Calcul for basements
if (mummiesNumber <= 2): mummiesCandy += mummiesNumber * 3
if (ghostsNumber > 0): ghostsCandy += 4
vampiresCandy += 0

#Calcul for houses
if (ghostsNumber > 0): ghostsCandy += (ghostsNumber - 1) * 3
mummiesCandy += mummiesNumber * 1
if (vampiresNumber > 4): 
    vampiresCandy += 8 + (vampiresNumber - 4) * 1
else: 
    vampiresCandy += vampiresNumber * 2

#Calcul for villas
if (vampiresNumber > 0): vampiresCandy += 12
vampiresCandy += (vampiresNumber - 1) * 2
mummiesCandy += mummiesNumber * 2
ghostsCandy += ghostsNumber * 2

#Calcul of parent's tax
vampiresCandy -= 2 * (villasNumber + housesNumber + basementsNumber)
ghostsCandy -= 2 * basementsNumber
mummiesCandy -= 1 * housesNumber

#Display results
print("\n\nBonbons des momies : {}, bonbons des fantômes : {}, bonbons des vampires : {}".format(mummiesCandy, ghostsCandy, vampiresCandy))











