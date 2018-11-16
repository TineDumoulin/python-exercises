def sentencesplitter(path):
    '''A function that splits all sentences in a path ('path').

    path: str, path from which you want the sentences split.'''

    spl_sent = [] #lege lijst waar uiteindelijke de zinnen als aparte string in terechtkomen
    #lege string, die na elke gevonden zin opnieuw wordt leeggemaakt, zodat ik de gevonden zin kan verwijderen uit de tekst
    endcnt = 1 #teller die telt hoe veel woorden de zin telt (als index, dus te beginnen van 0)
    startcnt = 0
    
    with open(path, 'r', encoding='utf8') as f:
            text = f.read() #de tekst assignen
            
    splitted_text = (text.replace('\n', ' ')).split(' ') #de newlines verwijderen uit de tekst en de tekst in woorden opslitsen

    for word in splitted_text: #voor elk woord in de gesplitte zin (anders gaat hij iteraten over de letters, en ik wil dat hij iterate over de woorden)
        if ('.' in word or '!' in word or '?' in word): #als er een leesteken .! of ? voorkomt in het woord, dan betekent dat dat dat het einde is van een zin.
            sentence_to_append = ' '.join(splitted_text[startcnt:endcnt]) #als dat zo is, dan gaan we kijken welke woorden een gehele zin vormen, en die moeten uiteindelijk uit de tekst verwijderd worden
            spl_sent.append(sentence_to_append) #deze woorden gaan we eers toevoegen aan onze lijst met aparte zinnen
            startcnt = endcnt
            
        endcnt += 1 #dan tellen we 1 woord erbij op de counter (maar we beginnen van 0, om gemakkelijk te indexeren)
    
    print(spl_sent) #we printen een deel van de zinnen, om te zien of het gelukt is

sentencesplitter('junglebook.txt')
