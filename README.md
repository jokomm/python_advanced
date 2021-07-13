# Python edasijõudnutele /  Advanced Python

## Homework 1

The general purpose of the exercise is to practice creating a python module and uploading it to the Pypi test environment, and afterwards using the created module.

1. Write a simple function that finds area and circumference of circle. When writing your code, keep in mind that negative values of radius are not possible.

The function input is radius R and returns the area S and circumference C

2. Create a python module and add your program to that module.

Use 'circle-yourusername' to name the module. When creating a module, be sure to pay attention to the contents of the setup.py, README.md and __init__.py files.

3. Upload the module to the Pypi TEST(!) Environment at https://test.pypi.org/

4. Reinstall the module in your computer. Make sure the installation was successful, if necessary remove the previous version with the 'pip uninstall' command.

The pip install command is something like this: pip install https://test.pypi.org/simple/ circle-yourusername

5. Write a program that imports the module you created, asks for R, and prints out area and circumference.

6. Write some tests to test the module. Pay attention to tests naming convention 'test_***.py'

7. Zip the created module and the program using the module and tests and upload it to Moodle. Also include a link to the module in the test environment as a single line text file: e.g.: https://test.pypi.org/project/circle-your username/

NB. To prevent problems reinstalling the module, use underscores, not hyphens, in folder names in the tree structure.

-------------------------------------------------------------------------------------------------------------------

Ülesande üldine eesmärk on harjutada pythoni mooduli loomist ja selle üles laadimist Pypi testkeskkonda ning loodud moodulit seejärel kasutada.

1. Kirjutage lihtne funktsioon, mis leiab ringi pindala ja ümbermõõdu. Koodi kirjutamisel arvestage, et negatiivse raadiuse korral ei ole võimalik vastuseid arvutada.

Funktsioon saab sisendi raadiuse R ning tagastab pindala S ja ümbermõõdu C. 

2. Looge pythoni moodul ja lisage oma programm sinna moodulisse.

Mooduli nimekujuks kasutage 'circle-teiekasutajanimi'. Mooduli loomisel pöörake kindlasti tähelepanu setup.py, README.md ja __init__.py failide sisule. 

3. Laadige moodul üles Pypi TEST(!)keskkonda https://test.pypi.org/

4. Paigaldage moodul tagasi oma arvutisse. Veenduge, et paigaldus õnnestus, vajadusel eemaldage eelmine versioon 'pip uninstall' käsuga.

Pip paigalduskäsk on umbes selline: pip install -i https://test.pypi.org/simple/circle-teiekasutajanimi

5. Kirjutage programm, mis impordib teie loodud mooduli, küsib raadiuse R ning prindib välja pindala ja ümbermõõdu.

6. Kirjutage mõned testid mooduli testimiseks. Pöörake kindlasti tähelepanu, et testide nimekuju peab olema 'test_***.py', see võimaldab automaattestidel neid üles leida ja käivitada.

7. Pakkige loodud moodul ja moodulit kasutav programm ning testid kokku ja laadige Moodlesse. Lisage üherealise tekstifaili kujul ka link testkeskkonnas olevale moodulile: nt: https://test.pypi.org/project/circle-teiekasutajanimi/

Python 3.6-3.8


##  Homework 2


Homework 2, Databases and Python.

There are 8 diners* in different buildings of TalTech. There are different opening hours for every canteen.

Task:

1) Create SQLite database DINERS, with two related tables CANTEEN and PROVIDER

Table CANTEEN fields: ID, ProviderID, Name, Location,  time_open, time_closed (weekday doesn't matter).

Table Provider fields: ID, ProviderName.

If you want, you may add some additional fields, but not necessary.

2) Insert IT College canteen data by separate statement, other canteens as one list.

3) Create query for canteens which are open 16.15-18.00

4) Create query for canteens which are serviced by Rahva Toit. NB! Create query by string "Rahva Toit" not by direct ID!.

Additional Information:
Tests and GUI are not necessary.

Add documentation and comments.

You may use direct SQL or SQLAlchemy (or other ORM).

Please zip all files (code + SQLite database) and upload to Moodle

Hints: SQLite datatypes: https://www.sqlite.org/datatype3.html

How to join and query data from related tables using SQLAlchemy: https://community.snowflake.com/s/article/How-to-Join-2-tables-using-SQL-Alchemy


## Homework 3

The aim of the homework is to practice working with a graphical environment and data, and to combine data from different sources. The aim is also to learn how to install packages in more complex cases. This is probably the most difficult homework, as installing packages can be quite complicated and may require a lot of time and additional reading.

The task is to draw direct flights departing from Tallinn Airport before COVID-19 and currently on the map of Europe

The OpenFlights Airports Database https://openflights.org/data.html has over 14,000 airports around the world, but scheduled flights from Tallinn to only a few dozen (before Corona-crisis).

Airport data with geographical coordinates
https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat (without column headers)
or
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/airports.dat (with column headers).

Direct flights departing from Tallinn (before COVID-19):
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/otselennud.csv

Direct flights departing from Tallinn (Apr 2021):
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/flights21.csv

Based on these tables, and using Python's cartography (eg cartopy) and drawing packages (eg matplotlib), a map of Europe must be created and the airports displayed on the map, where you can fly on direct routes from Tallinn. It is worth noting that due to the peculiarities of depicting the curvature of the globe, a geographical shortcut on a two-dimensional map is not a straight line, but a curve.
The created program must draw the map both on the screen and save it as a file (png, jpg, pdf or some other format) similar to the example: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.png The map must have also the title and name of author. Other designs are on your choice.

The same data and sample files are also compressed in the task attachment.

How to do this homework?

It is probably useful to add coordinates to the table of direct flights departing from Tallinn.
One way to do this is to use the 'pandas' library by importing the csv files (pandas.read_csv) and then to merge. The common field is called 'IATA'. Note that one file has a field separator comma, the other a semicolon.
Importing Pandas csv https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

An example of a table with aggregated data is: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.txt (Don't use it in homework!)

Some references:

https://scitools.org.uk/cartopy/docs/latest/installing.html
Installing Cartopy with Conda.

Drawing maps (contour maps, etc.). Drawing flight paths.
https://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html

More reading:
https://matplotlib.org/basemap/users/geography.html
https://matplotlib.org/basemap/users/installing.html
https://matplotlib.org/basemap/users/intro.html
https://towardsdatascience.com/planning-to-travel-around-the-world-with-python-42fac1d21a6e

https://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py

It is not necessary to use the above libraries, others can be used of your choice, the result is important.

Questions are welcome.

-------------------------------------------------------------------------------------------------------------------

Koduülesanne nr 3

Koduülesande eesmärk on harjutada graafilise keskkonna ja andmetega töötamist ning erinevatest allikatest pärit andmete kokkuliitmist. Samuti on eesmärgiks  pakettide paigaldamise õppimine keerulisematel juhtumitel.

Ülesandeks on Tallinna Lennujaamast koroonaeelsel ajal ja käesoleval ajal väljuvate otselendude joonistamine Euroopa kaardile. OpenFlights Airports Database-s https://openflights.org/data.html on üle 14000 lennujaama üle kogu maailma, kuid regulaarlennud Tallinnast toimuvad ainult mõnekümnesse.

Lennujaamade andmed koos geograafiliste koordinaatidega
https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat (ilma veerupealkirjadeta)
või
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/airports.dat (veerupealkirjadega).

Tallinnast väljunud koroonaeelsed otselennud:
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/otselennud.csv

Tallinnast aprillis 2021 väljuvad otselennud:
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/flights21.csv

Nende kolme tabeli põhjal ning Pythoni kartograafia- (nt. cartopy) ja joonestuspakettide (nt. matplotlib) kasutamisega tuleb luua Euroopa kaart ning kaardile kuvada ühe värviga lennujaamad, kuhu sai Tallinnast lennata koroonaeelsel ajal ja teise värviga praegusel ajal otseühenduses olevad lennujaamad koos lennuteekondadega sinna. Tähelepanu tasub pöörata sellele, et tulenevalt maakera kumeruse kujutamise iseärasustest ei ole geograafiline otsetee kahemõõtmelisel kaardil sirgjoon, vaid kõver.
Loodud programm peab joonestama kaardi nii ekraanile kui ka salvestama failina (png, jpg, pdf või mõni muu formaat) sarnaselt põhimõttelisele näidisele: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.png Kaardil peab olema ka pealkiri ja autori nimi. Muu kujundus on omal valikul.


Kuidas teha?

Ilmselt on otstarbekas Tallinnast väljuvate otselendude tabelile lisada koordinaadid.
Üks võimalus seda teha on kasutada 'pandas' library-t, selleks tuleb csv failid importida (pandas.read_csv) ja seejärel kokku 'mergeda'. Ühine väli kannab nime 'IATA'. Tasub tähele panna, et ühes failis on väljade eraldaja koma, teises semikoolon.
Pandas csv importimine https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

Kokkutõstetud andmetega tabeli näidis on: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.txt (Ärge kasutage seda faili oma töös!)

Mõningad viited:

https://scitools.org.uk/cartopy/docs/latest/installing.html
Cartopy installeerimine Conda abiga.

Maakaartide (kontuurkaardid jne) joonistamine. Lennuteekondade joonistamine.
https://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html

Veel lisalugemist:
https://matplotlib.org/basemap/users/geography.html
https://matplotlib.org/basemap/users/installing.html
https://matplotlib.org/basemap/users/intro.html
https://towardsdatascience.com/planning-to-travel-around-the-world-with-python-42fac1d21a6e

https://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py

Ei pea tingimata kasutama ülaltoodud teeke, omal valikul võib ka teisi kasutada, oluline on tulemus.


## Homework 4

Task Create a Python spider for page:

https://www.osta.ee/en/category/computers/desktop-computers (English)
or
https://www.osta.ee/kategooria/arvutid/lauaarvutid  (Estonian)
(Probably osta.ee is the largest auction environment in Estonia).

At your own choice, you can also choose another category from the osta.ee page (or any of your favourite similar website). It is important for the selection that there are at least 400 objects and 6 subpages in the selection.

Grab all computers from all pages and create JSON file with attributes:
{Title: '', Price: '', Picture href: ''}

The number of pages should not be hardcoded as this may vary depending on the number of items in the auction.

You may use Scrapy library or Beautiful Soup library.

Please zip all files (code + JSON file) and upload to Moodle

Attention! There are lot of crap code in the 'source' of osta.ee pages, which are not displayed on the screen, but have similar 'tags'. These redundant items that do not appear on this page must not be inserted to the .json file. 

Questions are welcome.

-------------------------------------------------------------------------------------------------------------------

Koduülesanne nr 4

Koduülesande eesmärk on lihtsa 'veebiämbliku' koostamine lehele https://www.osta.ee/kategooria/arvutid/lauaarvutid 

Omal äranägemisel võib osta.ee lehelt valida ka mõne muu kategooria. Oluline on valiku juures see, et valikus oleks vähemalt 400 objekti ja 6 alamlehte.

Kammige läbi kõik kaubad kõikidel alamlehtedel (1 kuni ...) ja looge JSON fail järgnevate atribuutidega:

{Title: '', Price: '', Picture href: ''} Lehtede arvu ei tohi koodi 'hardcodeda', sest see võib muutuda sõltuvalt oksjonil olevate esemete arvust.

Võite kasutada oma töös Scrapy library-t või Beautiful Soup library-t.

Kokkupakitud failid (kood + JSON fail) laadige üles Moodle-sse.

Tähelepanu! osta.ee lehtede 'source's leidub hulgaliselt ka muud "sodi", mida ei kuvata ekraanil, kuid on sarnaste 'tag'idega. Neid üleliigseid, antud lehel mittekuvatavaid kaupasid ei tohi .json faili tekkida.
