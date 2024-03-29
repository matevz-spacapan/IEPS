# IEPS 2. naloga

V tej nalogi smo izdelali skripto, ki iz vnaprej izbranih spletnih strani izvede ekstrakcijo podatkov s pomočjo regularnih izrazov ter XPath izrazov.

## Poganjanje skripte

### Predpogoji
Naša implementacija zahteva, da imamo nameščeni knjižnici `lxml` in `elementpath`.
Za namestitev zgoraj omenjenih knjižnic, uporabimo spodnji ukaz:
* `pip install lxml elementpath`


Skripta se nahaja v mapi `implementation-extraction`, zaženemo pa jo z ukazom `python run-extraction.py ALGORITHM`, kjer vrednost `ALGORITHM` lahko zavzame eno izmed sledečih vrednosti:
* `A` za izvajanje ekstrakcije podatkov z uporabo regularnih izrazov,
* `B` za izvajanje ekstrakcije podatkov z uporabo XPath izrazov.

#### Spletne strani za izvajanje ekstrakcije (`A` in `B`)
V mapi `input-extraction` se nahajajo 3 podmape v katerih je vsebina spletnih strani, ki se uporabljajo v algoritmih `A` in `B`:
* `rtvslo.si`: Članek. Ekstrahirali smo podatke, ki so označeni na spodnji sliki (pri temu nismo zajemali slik ipd.).

![RTV Slo podatki za ekstrakcijo](https://szitnik.github.io/wier-labs/img/pa2/rtvslo.png)
* `overstock.com`: Seznam prodajanih artiklov. Ekstrahirali smo individualne artikle, kot označeno na spodnji sliki.

![Overstock podatki za ekstrakcijo](https://szitnik.github.io/wier-labs/img/pa2/overstock.png)
* `store.steampowered.com`: Seznam iger, ki so združene v paketu. Ekstrahirali smo nekaj podatkov o paketu, kot tudi vse elemente, ki so v njem.

![Steam Store podatki za ekstrakcijo](./input-extraction/store.steampowered.com/Opisi.png)
