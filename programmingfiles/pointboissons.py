from math import *
print("\n\n")
print("""****Je suis le programme qui fait l'inventaire des boissons de New-Dar****""")
print()
print("Auteur: KOUAGOU N'Dah Jean\n")
print("Client acheteur du logiciel: KPANKOU Amour Tédi\n")
print("\nAlors, laissez-nous commencer l'inventaire")
print("\nN'oubliez pas de faire le point des boissons d'aujourd'hui et noter dans le cahier des recettes avant de commencer")
print()
periode=input("Veuillez insérer la période de l'inventaire sous le format : du jj/mm/aaaa au jj/mm/aaaa: ")
print("\n\n")
Quantite=[70,40,50,32,36,18,36,20,36,28,12,28,30,11,20,50,33,26,65,40,14,42,38,30,28,30,24,26,34,30,8,8,8,8]

Prix=[600,350,600,400,500,1200,700,900,500,700,400,800,500,400,500,600,1000,600,500,300,500,500,350,700,750,1000,500,500,500,600,4000,3500,3600,3500]	

Tableau=['de La Béninoise_0.6L','de La Béninoise_0.3L','de Beaufort_0.5L','de Beaufort_0.3L','de La Castel','de La Guinesse_0.6L','de La Guinesse_0.3L','de Eku_0.6L','de Eku_0.3L','de Pils_0.6L','de Pils_0.3L','de Awooyo','de XXL','de Satzembro','de Trophy','de Doppel','de Desperado','de Flag','de La Sucrerie_0.6L','de La Sucrerie_0.3L','de Malta','de La Star_Citron','de Panaché','de Vanpur','de Vanpur_Malta','de KAO','de EMG','de Sport_Actif','de FIFA','de Kuwabo','du Vin_Ferboy_et_Amanville','du Vin_Drostdy','du Vin_Bordeau_Chateau','du Vin_Bordeau_Traillac',]
Nombre=[12,24,12,24,12,12,24,12,24,12,12,12,24,12,12,12,24,12,12,24,12,20,24,24,24,24,6,24,6,6,6,6,6,6]

Plus_vendu="aucun"
Moins_vendu="aucun"
max=0
min=10000
Mont_initial=0
Mont_vendu=0
Mont_final=0
Stock_initial=[0]*len(Tableau)
Stock_achete=[0]*len(Tableau)
Stock_final=[0]*len(Tableau)
Boissons=['boisson']*len(Tableau)
Commande=['.']*len(Tableau)
for i in range(len(Tableau)):
	print("\nVeuillez entrer le stock initial ",Tableau[i],":")
	Stock_initial[i]=int(input())
for i in range(len(Tableau)):
	print("\nVeuillez entrer le stock acheté ",Tableau[i],":")
	Stock_achete[i]=int(input())
for i in range(len(Tableau)):
	print("\nVeuillez entrer le stock final ",Tableau[i],":")
	Stock_final[i]=int(input())
for i in range(len(Tableau)):
	commande=Quantite[i]-Stock_final[i]
	nbcommande=commande//Nombre[i]
	if nbcommande<0:
		nbcommande=0
	t=':'
	separ='  '
	Boissons[i]=Tableau[i]+t+str(Stock_final[i])+separ
	Mont_vendu=Mont_vendu+(Stock_initial[i]+Stock_achete[i]-Stock_final[i])*(Prix[i])
	Mont_final=Mont_final+Stock_final[i]*(Prix[i])
	Mont_initial=Mont_initial+Stock_initial[i]*Prix[i]
	if nbcommande!=0:
		Commande[i]=Tableau[i]+t+str(nbcommande)
	if max<Stock_initial[i]+Stock_achete[i]-Stock_final[i]:
		Plus_vendu=Tableau[i]
		max=Stock_initial[i]+Stock_achete[i]-Stock_final[i]
	if min>Stock_initial[i]+Stock_achete[i]-Stock_final[i]:
		Moins_vendu=Tableau[i]
		min=Stock_initial[i]+Stock_achete[i]-Stock_final[i]
print("\nLe montant total de la vente est: ",Mont_vendu)
achat=int(input("\n\nVeuillez entrer le montant des dépenses sur achat de boissons: "))
print("\n\n •Le montant actuel dans la caisse, sauf s'il y a manquant, est: ",400000-Mont_initial+Mont_vendu-achat)
depot=int(input("\n\nVeuillez entrer le montant d'argent déposé dans le cahier de recettes: "))
Mont_reel_caisse=400000-Mont_initial+depot-achat
print("\n\n •Le montant réel dans la caisse actuellement est: ",Mont_reel_caisse)
Benefice=Mont_vendu-achat+Mont_final-Mont_initial
print("\n\nLe bénéfice idéal (si pas de manquant) est: ",Benefice)
Benefice_reel=depot-achat+Mont_final-Mont_initial
print("\n\n Δ: Il y a manquant de: ",Mont_vendu-depot)
print("\n\n$ Alors, le bénéfice réel, compte tenu du manquant, est: ",Benefice_reel)
print("\n\nLe montant total des boissons qui restent s'élève à: ",Mont_final)
print("\n\nLe montant à laisser dans la caisse est: ",400000-Mont_final)
print("\n\nL'une des boissons les moins vendues est: ",Moins_vendu)
print("\n\nLa boisson la plus vendue est : ",Plus_vendu)
print("Nous vous recommandons l'achat régulier ",Plus_vendu)
print()
print("\n\nImportant pour le prochain inventaire, veuillez trouver ci-dessous les stocks finaux :\n")
for i in range(len(Boissons)):
	print(Boissons[i], end='  ')
print("\n\nMaintenant, commande:\n")
for i in range(len(Commande)):
	if Commande[i]!='.':
		print(Commande[i], end='     ')
print("\n\nPériode de l'inventaire d'aujourd'hui :",periode)
print("\n\n Merci d'être restés avec nous, on se retrouve très vite!\n\n")			
			
	
		
		
