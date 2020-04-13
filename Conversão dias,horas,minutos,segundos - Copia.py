Segundos = input("or favor, entre com o número de segundos que deseja converter: ")

TotalSegundos = int(Segundos)

Dias = TotalSegundos // 86400

ResTotalDias = TotalSegundos %  86400

Horas = ResTotalDias // 3600

RestoTotalHoras = TotalSegundos % 3600

Minutos = RestoTotalHoras // 60

Segundos = TotalSegundos % 60

print (Dias,"dias,",Horas,"horas,",Minutos,"minutos e",Segundos,"segundos")
