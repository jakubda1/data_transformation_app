# Rasa/Python dev zadani

## 1. Python
### 1.1
Napiste CLI aplikaci (skript/program) jehoz vstup je JSON pole plochych slovniku (flat dicts). 
Program vstup zanalyzuje a na vystupu vytvori slovnik vnorenych slovnku s klici urcenymi pres argumenty prikazove radky, hodnoty listu (zbyle prvky) budou ve formatu pole plochych slovniku, spadajici pod vhodnou skupinu. 

Struktura vstupniho JSON viz [input_data.json](data/input_data.json)

Priklady volani a vystupu:
> cat input_data.json | python my_script.py currency country city
```json
{
    "USD": {
        "US": {
            "Boston": [
                {
                    "amount": 100
                }
            ]
        }
    },
    "EUR": {
        "FR": {
            "Paris": [
                {
                    "amount": 20
                }
            ],
            "Lyon": [
                {
                    "amount": 11.4
                }
            ]
        },
        "ES": {
            "Madrid": [
                {
                    "amount": 8.9
                }
            ]
        }
    },
    "GBP": {
        "UK": {
            "London": [
                {
                    "amount": 12.2
                }
            ]
        }
    },
    "FBP": {
        "UK": {
            "London": [
                {
                    "amount": 10.9
                }
            ]
        }
    }
}                                                              
```

> cat input_data.json | python my_script.py currency country
```json
{
    "USD": {
        "US": [
            {
                "city": "Boston",
                "amount": 100
            }
        ]
    },
    "EUR": {
        "FR": [
            {
                "city": "Paris",
                "amount": 20
            },
            {
                "city": "Lyon",
                "amount": 11.4
            }
        ],
        "ES": [
            {
                "city": "Madrid",
                "amount": 8.9
            }
        ]
    },
    "GBP": {
        "UK": [
            {
                "city": "London",
                "amount": 12.2
            }
        ]
    },
    "FBP": {
        "UK": [
            {
                "city": "London",
                "amount": 10.9
            }
        ]
    }
}

```

## 2. Integrace
### 2.1 Web app
Vytvorenou CLI aplikaci prevedte do webove aplikace (WebApp). 
Pouzijte Python framework, ktery znate nejlepe (django, fastapi, flask, sanic). Ucelem teto casti NENI provereni znalosti frameworku.

Ve WebApp definujte 1 POST endpoint (/api/v1/parse-me/), ktery bude prijimat 2 parametry:
- args -> pole klicu pro vystup (vnoreny slovnk) 
- json_data -> vstup jako v prvni casti ulohy (raw vstup, ne soubor)

Validni provolani endpointu vrati standardni API response s vysledkem zpracovani.

### 2.2 Security - optional bonus
Endpoint by mel byt chraneny access Tokenem (auth). 
Plne postaci staticky definovany Token nekde v samotne WebApp (rozhodne nevytvarejte auth/autz logiku).
Pokud je pro vas jednodussi vytvorit username/passwort auth, smele do toho. 

### 2.3 Delivery - optional bonus
Vytvorenou WebApp zabalte Docker containeru a zpristupnete na nejakem portu (napr. 8080).
Logika z 2.1 a/nebo 2.2 by mela byt pristupna i pro WebApp spustenou v Dockeru.


### Dulezite
Reseni odevzdavate jako "finalni produkt urceny konecnemu zakaznikovi", tudiz by melo obsahovat pouze nalezitosti, ktere povazujete v takovem pripade za dulezite.

Doba vypracovani je priblizne 3-4h, neradil bych nad tim travit vice casu.

Pouzijte tech stack, se kterym mate nejvice zkusenosti. 
Python (3.8-3.10), Docker/Podman pro containerizaci, Postman/Paw pro volani API.

Pripadne dotazy a nejastnosti rad zodpovim na emailu vta@csob.cz nebo rychleji na tel. 703988257.

Preji hodne zdaru a tesim se na vase reseni.
Vysledek si pak spolecne projdeme a pobavime se nad zvolenym postupem.

Van Duy Ta

Kate Dev
