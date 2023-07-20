Tic-tac-toe
Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně. Jde o hru pro dva hráče (příp. počítač).

Program bude obsahovat:
Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:
Ukázka kódu2
ZKOPÍROVAT KÓD
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
import ...
Program pozdraví uživatele
Vypíše v krátkosti pravidla hry
Zobrazí hrací plochu
Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
Pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní.
Pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
Jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy
Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.
Úvodní text:
Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game
Příklad fungujícího kódu:
Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game
--------------------------------------------
+---+---+---+
| | | |
+---+---+---+
| | | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player o | Please enter your move number: 5
============================================
+---+---+---+
| | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player x | Please enter your move number: 1
============================================
+---+---+---+
| X | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player x | Please enter your move number:
...
============================================
Player o | Please enter your move number:
============================================
+---+---+---+
| X | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Congratulations, the player o WON!
============================================
