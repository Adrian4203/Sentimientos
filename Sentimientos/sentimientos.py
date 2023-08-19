from textblob import TextBlob

textos = ["The service met expectations.",
"It was a standard service without highlighting in particular.",
"It conformed to the specifications offered.",
"There were no surprises, neither positive nor negative.",
"Excellent service, exceeded my expectations!",
"I am delighted with the treatment received by the staff.",
"Service was fast and efficient, very impressed!",
"The quality of the service was exceptional, I will definitely recommend it.",
"I was pleasantly surprised at how well everything turned out.",
"The staff was friendly and attentive at all times, very professional!",
"The service was impeccable, I can't find fault!",
"A fantastic experience. I will definitely use the service again.",
"The service provided was really valuable to me.",
"The service left a lot to be desired, I would not recommend it.",
"I was disappointed with the result of the service.",
"There were several errors during the process, which was frustrating.",
"Customer service was poor and unprofessional.",
"The promises made about the service were not fulfilled.",
"The quality of the service was low compared to the price paid.",
"I ran into several problems and obstacles while using the service."
]
positivo=0
negativo=0
neutro=0

for texto in textos:
    blob = TextBlob(texto)
    sentimiento = blob.sentiment.polarity

    if sentimiento > 0:
        clasificacion = "Positivo"
        positivo+=1
    elif sentimiento < 0:
        clasificacion = "Negativo"
        negativo+=1
    else:
        clasificacion = "Neutral"
        neutro+=1

    print("Texto: ",texto)
    print("Clasificación: ",clasificacion)
    print()

print("El resultado final es: ","positivos: ",positivo,", negativos: ", negativo,", neutros: ",neutro)