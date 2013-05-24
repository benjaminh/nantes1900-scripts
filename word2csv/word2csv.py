#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# * parcours de fichiers doc pour récupération des coordonnées *

import os
import sys
import shutil
import subprocess
import glob
import re

source="/media/DD_ALT/DDBlanc/MYPASSPORT/Projets Equipes/Histoire-Patrimoine/7. 2013 CBrule-APolyakova/NANTES/NOTICES"
cible="/home/bhervy/Temp/Donnees"

#récupération de la liste de fichiers doc
listefichiers=glob.glob(source+"/*/*.doc")
#sortie = open("/home/bhervy/Temp/Donnees/Listefichiers", "a")
#sortie.write("\n".join(listefichiers))

#fichier temporaire pour stockage des nouveaux noms de fichiers
nvxfichiers = open("/home/bhervy/Temp/Donnees/Nvxfichiers", "a")

#Conversion de doc vers html avec bibliothèque wv
#for root,dirs,files in os.walk(source):
#	for file in files:
#		if (file.endswith(".doc")):
#			newfile=file.rpartition(".doc")[0]+".html"
#			nvxfichiers.write(newfile+"\n")
#			fichiersource=""
#			for i in listefichiers:
#				if (i.endswith(file)):
#					fichiersource = i
#					commandeshell=["wvHtml", "--charset=utf-8", fichiersource, newfile]
#					#commandeshell=["mv", "$(wvHtml "+fichiersource+" "+newfile+")", cible]
#					subprocess.call(commandeshell)
#					#Déplacement
#					tgt=os.path.join(cible,newfile)
#					shutil.move(newfile,tgt)

#Récupération des coordonnées dans un fichier csv
csvfile = open("/home/bhervy/Temp/Donnees/coord.csv", "a")
sortie = open("/home/bhervy/Temp/Donnees/Listefichiers", "a")
#sortie.write("\n".join(glob.glob(cible+"/*.html")))
for fichier in glob.glob(cible+"/*.html"):
	texte=unicode(open(fichier,'r').read(),"UTF-8").replace(" ","").replace(u"\u00A0","").replace("</u>","")
	slatitude = re.search('(?<=Latitude:)[a-zA-Z0-9_.]+\d', texte, re.I)#regexp
	slongitude = re.search('(?<=Longitude:)[a-zA-Z0-9_.-]+', texte, re.I)
	if slatitude and slongitude:
		lati = slatitude.group(0)
		longi = slongitude.group(0)
		csvfile.write(lati+","+longi+"\n")
		sortie.write(fichier+"\n")
csvfile.close()


