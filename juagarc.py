#!/usr/bin/env python
# -*- coding: utf-8 -*-
#	Juan Príncipe Ovelleiro
#	Juan José García Fonsecaç
#
#  juagarc.py

import pygtk
pygtk.require("2.0")
import gtk

class juego:				
				
				
	def __init__(self):
		filas = 10
		columnas = 10
		self.ventana = gtk.Window(gtk.WINDOW_TOPLEVEL)                  #crea ventana y la pone por encima
		self.ventana.set_border_width(100)								#pone el tamaño de la ventana
		tablero=gtk.Table(filas,columnas, homogeneous=True)
		boton=gtk.Button("1")
		boton1=gtk.Button("2")
		tablero.attach(boton,0,1,0,1)
		tablero.attach(boton1,1,2,0,1)
		self.ventana.add(tablero)
		self.ventana.show_all()
		
	def main(self):
		gtk.main()
		



if __name__ == '__main__':
	prueba = juego()
	prueba.main()
