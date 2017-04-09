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

import re

rege = re.compile('&')
regdollar = re.compile('\$')
regporc = re.compile('%')
reghash = re.compile('([^\n](?<!\n#)(?<!\n##)(?<!\n###)(?<!\n####)(?<!\n#####))#')
regtraco = re.compile('(.*\\w)-(\\w.*)')
regaspas = re.compile('"([^-].+?)"(?!-)')
regaspas2 = re.compile('\[([^]]*)\]\(([^)]*\w)"-(\w[^)]*)\)')
regespacos = re.compile(' $', re.M)
regsecoes = re.compile('(^(?![#\n\[])[^\n]*)((\n)+^)(# )', re.M)
regsecoes2 = re.compile('(^(?![#\n\[])[^\n]*)((\n)+^)(## )', re.M)
regsecoes3 = re.compile('(^(?![#\n\[])[^\n]*)((\n)+^)(### )', re.M)

def emloop(reg, xp, escapando_):
	escapando_tmp = ""
	while escapando_tmp != escapando_:
		escapando_tmp = escapando_
		escapando_ = reg.sub(xp, escapando_)
	return escapando_

def escapar(escapando):
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = rege.sub('\&{}', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = regdollar.sub('\${}', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = regporc.sub('\%{}', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = emloop(reghash, r"\1\hash{}", escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = emloop(regtraco, r'\1"-\2', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = emloop(regaspas, r'\\textquotedblleft \1\\textquotedblright{}', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = emloop(regaspas2, r'[\1](\2-\3)', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = emloop(regespacos, r'', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = regsecoes.sub(r'\1\\fimsec\2\4', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = regsecoes2.sub(r'\1\\fimsubsec\2\4', escapando)
	sys.stdout.write(",")
	sys.stdout.flush()	
	escapando = regsecoes3.sub(r'\1\\fimsubsubsec\2\4', escapando)
	return escapando

def escapar_tmp(arquivo):
	fmd = open(fontes + '/' + dd + '/' + arquivo + '.md','r', encoding='UTF-8')
	escapado = escapar(fmd.read())
	fmd.close()
	fmd = open(fontes + '/' + dd + '/' + arquivo + '_tmp.md','w', encoding='UTF-8')
	fmd.write(escapado)
	fmd.close()
	return


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

		# escapa os caracteres

		sys.stdout.write("tratando a entrada..")
		sys.stdout.flush()	
		escapar_tmp('artigo')
		sys.stdout.write(";")
		escapar_tmp('comments')
		print("....ok")


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

