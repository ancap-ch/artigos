#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from io import TextIOWrapper
sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# from pylatex import Document, Package
# from pylatex.utils import escape_latex

import argparse
import os
import subprocess
import shutil


# print(escape_latex('\nAlso some crazy characters: $&#{}'))
# print(escape_latex('\nAlso some crazy characters: \qualquer{} $&#{}'))

modelos = 'C:/Users/Thiago/Desktop/ancap.ch/artigos/modelos'
fontes = 'C:/Users/Thiago/Desktop/ancap.ch/artigos/fontes'
ufontes = u'C:/Users/Thiago/Desktop/ancap.ch/artigos/fontes'
saidas = 'C:/Users/Thiago/Desktop/ancap.ch/artigos/pdfs'
main_tex = 'C:/Users/Thiago/Desktop/ancap.ch/artigos/main/main.tex'

path = fontes.encode('utf-8').strip()

debug = 0
passagens = 2
mobonly = 0
pconly = 0
last = 0

import unicodedata
#dirs = [unicodedata.normalize('NFC', f) for f in os.listdir(ufontes)]
dirs = os.listdir(path)
for index, d in enumerate(dirs, 1):
	sys.stdout.write(str(index))
	sys.stdout.write(": ")
	# sys.stdout.flush()	
	dd = d.decode('utf-8')
	ds = dd.replace("_", " ")
	print(ds)

while True:
	while True:
		print("------")
		sys.stdout.write(str(passagens))
		sys.stdout.write(" passagens. ")
		if debug:
			sys.stdout.write("debug, ")
		if mobonly:
			sys.stdout.write("mobonly, ")
		if pconly:
			sys.stdout.write("pconly, ")
		sys.stdout.flush()	
		print("\n------")
		print("1- vai\n2- debug ON/OFF\n3- mob only ON/OFF\n4- PC only ON/OFF\n5- passagens x/2")
		continua = eval(input("mude as opcoes: ") or "1")
		if continua == 1 or continua == 0:
			break
		if continua == 2:
			debug = 1 - debug
		if continua == 3:
			mobonly = 1 - mobonly
		if continua == 4:
			pconly = 1 - pconly
		if continua == 5:
			passagens =  eval(input("escolha o numero de passagens: ") or "2")
	print("------")
	indice = eval(input("crie o PDF: ") or last)
	copia = indice
	last = indice
	for index, d in enumerate(dirs, 1):
		if indice < 0:
			indice = 0
		if indice != 0 and indice != index:
			continue
		if copia < 0 and index < -copia:
			continue

		dd = d.decode('utf-8')
		ds = dd.replace("_", " ")
		#print(d)
		#print(dd)
		print(str(index) + " - " + ds + ":")
		for i in range(2):
			if i == 0 and mobonly:
				continue
			if i == 1 and pconly:
				continue
			f = open('file.tex','w', encoding='UTF-8')
			#l = open('lista.txt','w', encoding='UTF-8')
			f.write('\def \caminho{' + dd + '}\n')
			if i == 0:
				sys.stdout.write("pc...")
				sys.stdout.flush()	
				antes = fontes + "/" + dd + "/antes.tex"
				if os.path.isfile(antes):
					f.write('\input{' + antes + '}\n')
			else:
				sys.stdout.write("mob...")
				sys.stdout.flush()	
				f.write('\def \mobile{}\n')
			f.write('\input{' + main_tex + '}\n')
			f.close()

			for j in range(passagens):
				# cria o pdf...
				# ...acabou de criar
				sys.stdout.write(",")
				sys.stdout.flush()	
				if debug:
					proc = subprocess.Popen(['pdflatex', 'file.tex', "--shell-escape"])
				else:
					proc = subprocess.Popen(['pdflatex', 'file.tex', "-quiet", "--shell-escape"])
				proc.communicate()
				retcode = proc.returncode
				if not retcode == 0:
				    os.unlink('file.pdf')
				    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 
			# clean
			shutil.rmtree('_markdown_file')
			os.remove('file.aux')
			os.remove('file.log')
			os.remove('file.markdown.lua')
			os.remove('file.markdown.out')
			os.remove('file.out')
			os.remove('file.tex')
			os.remove('file.toc')

			if i == 0:
				shutil.copyfile('file.pdf', saidas + '/PC/' + ds + '.pdf')
			else:
				shutil.copyfile('file.pdf', saidas + '/Mobile/' + ds + ' (mobile).pdf')
			print("....ok")

