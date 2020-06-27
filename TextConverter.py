# Zawgyi to Unicode Text Converter
# Copyright (c) 2020 by Htoon Aung Kyaw
# Zawgyi to Unicode converting algorithm was got from https://github.com/kanaung/py-converter
# clipboard library was needed to install.
# pip install clipboard

# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk
import clipboard
import getopt
import re
import sys

# =====================================================================================

# Zawgyi to Unicode character replacement pairs
zguni = {'ဳ' : 'ု','ဴ' : 'ူ','္' : '်','်' : 'ျ','ျ' : 'ြ','ြ' : 'ွ','ွ' : 'ှ','ၚ' : 'ါ်','ၠ' : '္က','ၡ' : '္ခ','ၢ' : '္ဂ','ၣ' : '္ဃ','ၤ' : 'င်္','ၥ' : '္စ','ၦ' : '္ဆ','ၧ' : '္ဆ','ၨ' : '္ဇ','ၩ' : '္ဈ','ၪ' : 'ဉ','ၫ' : 'ည','ၬ' : '္ဋ','ၭ' : '္ဌ','ၮ' : 'ဍ္ဍ','ၯ' : 'ဍ္ဎ','ၰ' : '္ဏ','ၱ' : '္တ','ၲ' : '္တ','ၳ' : '္ထ','ၴ' : '္ထ','ၵ' : '္ဒ','ၶ' : '္ဓ','ၷ' : '္န','ၷ' : '္ပ','ၸ' : '္ပ','ၹ' : '္ဖ','ၺ' : '္ဗ','ၻ' : '္ဘ','ၼ' : '္မ','ၽ' : 'ျ','ၾ' : 'ြ','ၿ' : 'ြ','ႀ' : 'ြ','ႁ' : 'ြ','ႂ' : 'ြ','ႃ' : 'ြ','ႄ' : 'ြ','ႅ' : '္လ','ႆ' : 'ဿ','သ္သ' : 'ဿ','ႇ' : 'ှ','ႈ' : 'ှု','ႉ' : 'ှူ','ႊ' : 'ွှ','ႏ' : 'န','႐' : 'ရ','႑' : 'ဏ္ဍ','႒' : 'ဋ္ဌ','႓' : '္ဘ','႔' : '့','႕' : '့','႗' : 'ဋ္ဋ','၈ၤ':'ဂင်္','ဧ။္':'၏','ဧ၊္':'၏','၄င္း':'၎င်း','၎':'၎င်း','၎င္း':'၎င်း','ေ၀' : 'ေဝ','ေ၇' : 'ေရ','ေ၈':'ေဂ','စ်':'ဈ','ဥာ':'ဉာ','ဥ္':'ဉ်','ၾသ':'ဩ','ေၾသာ္':'ဪ'}
# Zawgyi to Unicode character corrections
zgunicorrect = {'\\s+္':'္','([က-အ])(င်္)' : '\\2\\1','(ေ)([က-အ၀၈၇]{1}္[က-အ၀၈၇]{1})' : '\\2\\1','([ေြ]{1,2})([က-အ၀၈၇]{1})':'\\2\\1','(ေ)([ျြွှ]+)':'\\2\\1','(ှ)(ျ)':'\\2\\1','(ံ)([ုူ])':'\\2\\1','([ုူ])([ိီ])':'\\2\\1','(ော)(္[က-အ])':'\\2\\1','(ဲ)(ွ)':'\\2\\1'}

# =====================================================================================

# function to convert zawgyi to unicode
def z2u_converter(input_string):
  pattern = '|'.join(map(re.escape, sorted(zguni, key=len, reverse=True)))
  return re.sub(pattern, lambda m: zguni[m.group()], input_string)

# function to correction for converting from zawgyi to unicode
def unicode_corrector(input_string, patterns):
  for patterns, repl in patterns.items():
    input_string = re.sub(patterns, repl, input_string)
  return input_string
  
# =====================================================================================

# windows initialization
root = tk.Tk()
root.resizable(0,0)
root.title('Text Converter')

# =====================================================================================

# function to close app
def close_window(): 
    root.destroy()

# function to clear all textbox
def clear_text():
    input_textbox.delete('1.0', tk.END)
    output_textbox.delete('1.0', tk.END)

# function to convert zawgyi text to unicode one
def convert_text():
	input_text = input_textbox.get("1.0", tk.END)
	converted_string = z2u_converter(input_text)
	converted_string = unicode_corrector(converted_string, zgunicorrect)
	output_textbox.insert('1.0', converted_string)

# function to copy output text
def copy_text():
	output_text = output_textbox.get("1.0", tk.END)
	#clipboard.copy(output_text)
	clipboard.copy(output_text)
    
# =====================================================================================

# windowwin frame
canvas = tk.Canvas(root, width = 1025, height = 400)
canvas.pack()

# =====================================================================================

# input label
input_label = tk.Label(root, text= 'Input Font')
canvas.create_window(10, 10, window=input_label, anchor='nw')

# input combobox
input_combo = ttk.Combobox(root, values=["Zawgyi", "Unicode"], width=30, state = 'disabled')
canvas.create_window(75, 10, window=input_combo, anchor='nw')
input_combo.current(0)

# input textbox
input_textbox = scrolledtext.ScrolledText(root, undo=True, font=('zawgyi-one', 10))
canvas.create_window(10, 40, width = 500, height = 300, window=input_textbox, anchor='nw')

# =====================================================================================

# output label
output_label = tk.Label(root, text= 'Output Font')
canvas.create_window(520, 10, window=output_label, anchor='nw')

# output combobox
output_combo = ttk.Combobox(root, values=["Zawgyi", "Unicode"], width=30, state = 'disabled')
canvas.create_window(595, 10, window=output_combo, anchor='nw')
output_combo.current(1)

# output textbox
output_textbox = scrolledtext.ScrolledText(root, undo=True, font=('pyidaungsu', 10))
canvas.create_window(520, 40, width = 500, height = 300, window=output_textbox, anchor='nw')

# =====================================================================================

# clear button
clear_button = tk.Button(root, text='Clear', command=clear_text)
canvas.create_window(10, 350, width = 100, height = 35, window=clear_button, anchor='nw')

# convert button
convert_button = tk.Button(root, text='Convert', command=convert_text)
canvas.create_window(750, 350, width = 100, height = 35, window=convert_button, anchor='ne')

# copy button
copy_button = tk.Button(root, text='Copy', command=copy_text)
canvas.create_window(860, 350, width = 100, height = 35, window=copy_button, anchor='ne')

# exit button
exit_button = tk.Button(root, text='Close', command=close_window)
canvas.create_window(1010, 350, width = 100, height = 35, window=exit_button, anchor='ne')

# =====================================================================================

root.mainloop()
