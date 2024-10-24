kolf-knooppunt

# Kolf Nodezator

> Een Python Flask-applicatie met Nodezator

Open deze URL met`https://github.dev/`in plaats van`https://github.com/`om de webgebaseerde IDE van Visual Studio Code te gebruiken.

[Referenties](./REFERENCES.md)

# Samenvatting

Voer deze applicatie als volgt uit:

1) Voer in`flask_app`map:`$ cd flask_app`2) Als deze niet bestaat, creëer dan een virtuele omgeving binnen de`flask_app`map:`$ python3 -m venv .venv`(macOS:`$ virtualenv .venv`)

Volg in geval van het volgende het advies:

De virtuele omgeving is niet succesvol gemaakt omdat surepip dat niet is
beschikbaar.

Op Debian/Ubuntu-systemen moet u het bestand python3-venv installeren
pakket met behulp van de volgende opdracht.

    sudo apt-get update
    sudo apt install python3.10-venv

Mogelijk moet je sudo gebruiken met die opdracht.  Na het installeren van het python3-venv
pakket, creëer uw virtuele omgeving opnieuw.

Op macOS zie<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) Start de virtuele omgeving en voer het volgende in:`. .venv/bin/activate`(macOS:`source .venv/bin/activate`)
4) Rennen`$ pip install -r requirements.txt`5) Uitvoeren:`$ cd app`Dan`$ npm install`Eindelijk`$ cd ..`6) Stel de Flask-app in op de app-map:`(.venv) $ export FLASK_APP=app`7) Stel de Flask Environment in op True voor ontwikkeling:`(.venv) $ export FLASK_DEBUG=True`8) Stel de SQLAlchemy Database-URI in:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, standaard is`sqlite:///app.db`9) SQLAlchemy-trackwijzigingen instellen:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) Geheime sleutel instellen:`(.venv) $ export SECRET_KEY=********`11) Voer de flask-app uit: ~`(.venv) $ flask run`~`(.venv) $ python3 run.py`12) Open de webinterface zoals gevraagd
13) Gebruik`CTRL+c`om de webserver te verlaten.
14) U kunt ook de flask-opdrachtregelinterface uitvoeren:`(.venv) $ flask shell`15) Voer eventuele flescommando's uit: >>>
16) Gebruik`exit()`om de opdrachtregelinterface te verlaten.

Over het algemeen kunt u de volgende stappen nemen om uw databasemigraties te beheren terwijl u uw Flask-applicaties ontwikkelt:

1) Wijzig de databasemodellen.

2) Indien nee`migrations`directory bestaat nog in de`flask_app`map, uitvoeren` (.venv) flask_app $ flask db init`.

3) Genereer een migratiescript met de`flask db migrate -m "some comment"`commando. Als er sinds de laatste migratie geen wijzigingen zijn aangebracht, wordt u gevraagd om`No changes in schema detected.`. Daarom kun je dit commando zonder angst herhalen.

4) Controleer het gegenereerde migratiescript en corrigeer het indien nodig.

5) Pas de wijzigingen toe op de database met de`flask db upgrade`commando.

6) Om een ​​eerdere databaseversie te herstellen, gebruikt u de`flask db downgrade`commando.

## 100 - Inleiding

Zien[README.md](./100/README.md)

## 200 - Vereisten

Zien[README.md](./200/README.md)

## 300 - Onze applicatie bouwen

Zien[README.md](./300/README.md)

## 400 - Conclusie

Zien[README.md](./400/README.md)
