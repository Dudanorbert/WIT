trip=250
time_p=165
car=int(input('Trasa ma 250km, podaj z jaką średnią prędkością zamierzasz ją przejechać ?'))
trasa=trip/car * 60
print("Trasę powinieneś pokonać w",int(trasa),"min")
if trasa < 165:
    print('W takim tempie powinieneś być na miejscu szybciej niż pociągiem')
elif trasa > 165:
    print('Lepiej wsiądź w pociąg, będziesz szybciej na miejscu')


