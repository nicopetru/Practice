from datetime import date
Cmati = "24-05"

today = date.today()
format = today.strftime("%d-%m")

if format == Cmati:
    print("Feliz cumple Mati")