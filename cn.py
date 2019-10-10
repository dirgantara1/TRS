#!/usr/bin/python
# coding=utf-8
# (ucu sangek) Dirgantara
# Source : Python2 Gerak"
# translete wak

#module
import urllib2
from urllib2 import URLError
import os
import sys
import time
import random
import cookielib
import mechanize

###id###
def id():
	print "\033[1;77m ID NEGARA"
	os.system('cat id_country.txt')
	print ""
	print "press enter to continue and Ctrl C to stop....."
	os.system('read "p" ')
	menu()


###translate###
def translate():
    try:
    	os.system('   toilet Google | lolcat')
    	print "\033[1;95m TRANSLATE GOOGLE "
        kata = raw_input("\033[1;97m [°_°] \033[1;95mText : ")
        bahasa_awal = raw_input(" \033[1;97m[\033[1;95mMasukkan Bahasa Awal\033[1;97m]\033[1;95m(ex: id): ") 
        bahasa_tujuan = raw_input(" \033[1;97m[\033[1;95mMasukkan Bahasa Tujuan\033[1;97m]\033[1;95m(ex: en): ")
        print " \033[1;97m═══════════════════════════════"
        url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+")) #replace apabila terjadi kalimat
        agent = {'User-Agent':'Mozilla/5.0'}
        cari_hasil = 'class="t0">'
        request = urllib2.Request(url, headers=agent)
        page = urllib2.urlopen(request).read()
        result = page[page.find(cari_hasil)+len(cari_hasil):]
        result = result.split("<")[0]
        print " \033[1;91m%s \033[1;97m=TRANSLATE=\033[1;91m>" % kata,result
        print ""
        sangek = raw_input("\033[1;97m ingin Translate lagi y/n? :\033[1;91m ")
        if sangek =="":
        	print " milih apa kau babi..!"
        elif sangek =="y":
        	translate()
        elif sangek =="Y":
            translate()
        elif sangek =="n":
        	menu()
        elif sangek =="N":
            menu()
       
      	
    except URLError, e:
        print "Periksa Jaringan Anda..."

def menu():
	os.system('sh sh.sh')
	print ""
	print "\033[1;77m[\033[1;91m1.\033[1;92m Lihat ID Negara\033[1;97m]"
	print "\033[1;77m[\033[1;91m2.\033[1;92m Translate\033[1;97m]"
	print ""
	pilih = raw_input("[?] Pilihan : ")
	if pilih =="":
		print "Bukan pilihan ! "
		menu()
	elif pilih == "1":
		id()
        elif pilih == "2":
        	translate()
        else:
        	print "Bukan pilihan !"
                menu()

if __name__ == "__main__":
	menu()
