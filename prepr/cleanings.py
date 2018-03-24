"""Preliminary filtering of the data with usefulness criteria."""

def clean_teach_eval(source, dest, year):
    """Cleaning of the teachings evaluation collections's documents.
    source: MongoDB collection
    dest:   MongoDB collection too
    year:   academic year of reference (start) """

    for doc in source.find():
        source.delete_many(doc)

        del doc['']                 # little quirk by mongoimport
        del doc['CID']              # useless as a key for this application
        del doc['Corso']            # always 'INFORMATICA' since it is the object of this study
        del doc['Tipo corso']       # as above, always 'INFORMATICA'

        # simply clearer
        doc['P<6'] = doc.pop('P1')
        doc['P>=6'] = doc.pop('P2')

        # clarify questions
        if year == 2010:
            doc = _clarify_questions_2010(doc)
        if year == 2011:
            doc = _clarify_questions_2011(doc)

            # ...
        #del doc['Q']
        #del doc['Quesito']

        # reference period for exam valuation
        doc['Inizio Periodo di Riferimento'] = str(year+1)+'-01-01'
        doc['Fine Periodo di Riferimento'] = str(year+2)+'-03-01'
        doc['Dataset Provenienza'] = str(year) + '-' + str(year+1)

        dest.insert_one(doc)

def _clarify_questions_2011(doc):
    if doc['Q'] == 'D4':
        doc['Oggetto Valutazione'] = 'Conoscenze preliminari sufficienti'
    if doc['Q'] == 'D5':
        doc['Oggetto Valutazione'] = 'Argomenti trattati nuovi o integrativi'
    if doc['Q'] == 'D6':
        doc['Oggetto Valutazione'] = 'Carico di studio proporzionato a credti'
    if doc['Q'] == 'D7':
        doc['Oggetto Valutazione'] = 'Materiale didattico adeguato'
    if doc['Q'] == 'D8':
        doc['Oggetto Valutazione'] = 'Attivita integrative utili'
    if doc['Q'] == 'D9':
        doc['Oggetto Valutazione'] = 'Modalita esame chiare'
    if doc['Q'] == 'D10':
        doc['Oggetto Valutazione'] = 'Orari didattica rispettati'
    if doc['Q'] == 'D11':
        doc['Oggetto Valutazione'] = 'Docente stimola interesse per la materia'
    if doc['Q'] == 'D12':
        doc['Oggetto Valutazione'] = 'Docente chiaro'
    if doc['Q'] == 'D13':
        doc['Oggetto Valutazione'] = 'Docente effettivamente reperibile per chiarimenti'
    if doc['Q'] == 'D14':
        doc['Oggetto Valutazione'] = 'Docente disponibile ed esauriente per chiarimenti'
    if doc['Q'] == 'D17':
        doc['Oggetto Valutazione'] = 'Argomenti interessanti'
    if doc['Q'] == 'D18':
        doc['Oggetto Valutazione'] = 'Soddisfazione complessiva corso'
    if doc['Q'] == 'D19':
        doc['Oggetto Valutazione'] = 'Copertura programma a lezione'
    if doc['Q'] == 'D20':
        doc['Oggetto Valutazione'] = 'Prove intermedie utili'
    return doc

def _clarify_questions_2010(doc):
    if doc['Q'] == 'D1':
        doc['Oggetto Valutazione'] = 'Carico di lavoro accettabile'
    if doc['Q'] == 'D2':
        doc['Oggetto Valutazione'] = 'Organizzazione corso (orario, intermedi, esami)'
    if doc['Q'] == 'D3':
        doc['Oggetto Valutazione'] = 'Orario lezioni consente studio individuale'
    if doc['Q'] == 'D4':
        doc['Oggetto Valutazione'] = 'Carico di studio proporzionato a credti'
    if doc['Q'] == 'D5':
        doc['Oggetto Valutazione'] = 'Materiale didattico adeguato'
    if doc['Q'] == 'D6':
        doc['Oggetto Valutazione'] = 'Attivita integrative utili'
    if doc['Q'] == 'D7':
        doc['Oggetto Valutazione'] = 'Modalita esame chiare'
    if doc['Q'] == 'D8':
        doc['Oggetto Valutazione'] = 'Orari didattica rispettati'
    if doc['Q'] == 'D9':
        doc['Oggetto Valutazione'] = 'Docente effettivamente reperibile per chiarimenti'
    if doc['Q'] == 'D10':
        doc['Oggetto Valutazione'] = 'Docente stimola interesse per la materia'
    if doc['Q'] == 'D11':
        doc['Oggetto Valutazione'] = 'Docente chiaro'
    if doc['Q'] == 'D12':
        doc['Oggetto Valutazione'] = 'Docente disponibile ed esauriente per chiarimenti'
    if doc['Q'] == 'D13':
        doc['Oggetto Valutazione'] = 'Aule lezioni adeguate'
    if doc['Q'] == 'D14':
        doc['Oggetto Valutazione'] = 'Aule e strumenti attivita integrative adeguati'
    if doc['Q'] == 'D15':
        doc['Oggetto Valutazione'] = 'Conoscenze preliminari sufficienti'
    if doc['Q'] == 'D16':
        doc['Oggetto Valutazione'] = 'Argomenti trattati nuovi o integrativi'
    if doc['Q'] == 'D17':
        doc['Oggetto Valutazione'] = 'Argomenti interessanti'
    if doc['Q'] == 'D18':
        doc['Oggetto Valutazione'] = 'Soddisfazione complessiva corso'
    return doc