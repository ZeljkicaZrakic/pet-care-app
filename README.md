# Aplikacija za evidenciju njege i zdravstvenih obaveza kućnih ljubimaca

## Opis projekta

Ovaj projekt predstavlja web aplikaciju za vođenje evidencije o kućnim ljubimcima i njihovim zdravstvenim obavezama. Aplikacija omogućuje unos osnovnih podataka o ljubimcima te praćenje važnih zdravstvenih događaja kao što su cijepljenja, veterinarski pregledi, tretmani protiv parazita i mjerenja težine.

Cilj projekta je omogućiti jednostavno upravljanje podacima o ljubimcima na jednom mjestu te pomoći vlasnicima u praćenju važnih zdravstvenih termina i obaveza.

Projekt je razvijen u sklopu kolegija Informacijski sustavi koristeći tehnologije obrađene tijekom laboratorijskih vježbi.

### Funkcionalnosti:
1. Upravljanje ljubimcima
2. Dodavanje novog ljubimca
3. Pregled svih ljubimaca
4. Uređivanje podataka o ljubimcu
5. Brisanje ljubimca
6. Upravljanje zdravstvenim zapisima
7. Dodavanje zdravstvenog zapisa
8. Pregled zdravstvenih zapisa po ljubimcu
9. Uređivanje zdravstvenih zapisa

### Podržane vrste zdravstvenih zapisa:

- Cijepljenje
- Veterinarski pregled
- Tretman protiv parazita
-Mjerenje težine
Statistika i vizualizacija

### Aplikacija automatski prikazuje:

- Ukupan broj ljubimaca
- Ukupan broj zdravstvenih zapisa
- Broj cijepljenja
- Broj veterinarskih pregleda
- Broj tretmana protiv parazita
- Broj mjerenja težine

Podaci su dodatno prikazani pomoću pie chart grafikona izrađenog korištenjem Chart.js biblioteke.

### Tehnologije
Backend
- Python
- Flask
- PonyORM
- Baza podataka
- SQLite
Frontend
- HTML
- CSS
- Bootstrap 5
Vizualizacija podataka
- Chart.js
Docker
Git
GitHub

## Struktura projekta
```text
pet_care_app/
│
├── app.py
├── models.py
├── requirements.txt
├── Dockerfile
├── pets.sqlite
│
├── templates/
│   ├── index.html
│   ├── edit_pet.html
│   └── edit_record.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── zed.jpg
│
└── README.md
```

## Model podataka

Pet

Predstavlja kućnog ljubimca.

Atributi:

- id
- name
- species
- breed
- weight
- notes

CareRecord

Predstavlja zdravstveni zapis.

Atributi:

- id
- pet
- record_type
- description
- date
- next_due_date

Jedan ljubimac može imati više zdravstvenih zapisa.

## Pokretanje aplikacije lokalno

1. Kloniranje repozitorija
git clone https://github.com/ZeljkicaZrakic/pet-care-app.git
cd pet-care-app
2. Instalacija ovisnosti
pip install -r requirements.txt
3. Pokretanje aplikacije
python app.py

Aplikacija će biti dostupna na:

http://127.0.0.1:5000

## Pokretanje pomoću Dockera

- Izrada Docker image-a
- docker build -t pet-care-app .
- Pokretanje kontejnera
- docker run -p 5000:5000 pet-care-app

Aplikacija će biti dostupna na:

http://localhost:5000

## Poslovna primjena

Aplikacija može biti korisna:

- vlasnicima kućnih ljubimaca
- veterinarskim ambulantama
- skloništima za životinje
- uzgajivačnicama

Korištenjem aplikacije moguće je voditi centraliziranu evidenciju zdravstvenih obaveza te lakše pratiti buduće termine i intervencije.

