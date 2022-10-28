# -*- coding: utf-8 -*-
from sre_parse import DIGITS
from string import digits
import re

arquivo_telefones = open("telefones.csv", mode="r", encoding="utf-8")

string_arq_novo = "Name,Phone\n"

string_telefones = arquivo_telefones.readlines()

for i, line in enumerate(string_telefones):
    line = line.split(",")
    
    name = line[0]
    if name[-1] == " ":
        name = name.strip()
    name = "Bunrenkai "+name

    phone = line[1].replace("\n", "")
    cagadas = []
    for i, c in enumerate(phone):
        if c not in digits:
            cagadas.append(c)
    for c in cagadas:
        phone = phone.replace(c, "")
    if re.search("^0.0", phone):
        phone = "+81"+phone
    elif re.search("^81", phone):
        phone = "+"+phone
    elif re.search("^55", phone):
        phone = phone[2:]
    
    new_line = name+","+phone+"\n"
    
    string_arq_novo += new_line

string_arq_novo = string_arq_novo[:-1]

arquivo_telefones.close()

arq_novo = open("saida.csv", mode="w", encoding="utf-8")
arq_novo.write(string_arq_novo)
