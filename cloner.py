#-*-coding: utf-8-*-
from urllib.request import urlopen
import sys
h = ("""
Manual:
Para usar o cloner basta usar 2 parametros
1 - endereço de origem
2 - endereço de destino...
exemplo:
python3 cloner.py https://www.site.com/arquivo.txt C:\\Users\\usuario\\Documents\\arquivo.txt
""")
if sys.argv[1] == "-h":
  print(h)
else:
  print("# cloner by: Renegado #")
  try:
    o = urlopen(sys.argv[1])
    try:
      with open(sys.argv[2], "wb") as fl:
        fl.write(o.read())
        print('Concluido!')
    except IOError:
      print("Não deu para criar arquivo!")
  except IOError:
    print("Arquivo não encontrado!")