import re

from scipy import rand
# from nltk.corpus import stopwords

def get_words(sentence):
    #We only want to work with lowercase for the comparisons
    scentence = sentence.lower() 

    #remove punctuation and split into seperate words
    words = re.findall(r'\w+', scentence,flags = re.UNICODE) 

    #This is the simple way to remove stop words
    important_words=[]
    non_important_words = []
    for word in words:
        if word not in stopwords.words('spanish'):
            important_words.append(word)
        else:
            non_important_words.append(word)

    return non_important_words

sentences = ['De esta manera supe una segunda cosa muy importante: su planeta de origen era apenas más grande que una casa', 'Esto no podía asombrarme mucho', 'Es difícil distinguirlos aun con la ayuda del telescopio', 'Cuando un astrónomo descubre uno de estos planetas, le da por nombre un número', 'Le llama, por ejemplo, el asteroide 3251', 'Tengo poderosas razones para creer que el planeta del cual venía el principito era el asteroide B 612', 'Este asteroide ha sido visto sólo una vez con el telescopio en 1909, por un astrónomo turco', 'Este astrónomo hizo una gran demostración de su descubrimiento en un congreso Internacional de Astronomía', 'Pero nadie le creyó a causa de su manera de vestir', 'Las personas mayores son así', 'Felizmente para la reputación del asteroide B 612, un dictador turco impuso a su pueblo, bajo pena de muerte, el vestido a la europea', 'Si les he contado de todos estos detalles sobre el asteroide B 612 y hasta les he confiado su número, es por consideración a las personas mayores', 'A los mayores les gustan las cifras', 'Cuando se les habla de un nuevo amigo, jamás preguntan sobre lo esencial del mismo', 'Pero nosotros, que sabemos comprender la vida, nos burlamos tranquilamente de los números', 'A mí me habría gustado más comenzar esta historia a la manera de los cuentos de hadas', 'Porque no me gusta que mi libro sea tomado a la ligera', 'Siento tanta pena al contar estos recuerdos', 'Hace ya seis años que mi amigo se fue con su cordero', 'Y si intento describirlo aquí es sólo con el fin de no olvidarlo', 'Es muy triste olvidar a un amigo', 'No todos han tenido un amigo', 'Y yo puedo llegar a ser como las personas mayores, que sólo se interesan por las cifras', 'Para evitar esto he comprado una caja de lápices de colores', 'Trataré de hacer retratos lo más parecido posibles, pero no estoy muy seguro de lograrlo', 'Uno saldrá bien y otro no tiene parecido alguno', 'En las proporciones me equivoco también un poco', 'Aquí el principito es demasiado grande y allá es demasiado pequeño', 'Dudo también sobre el color de su traje', 'Titubeo sobre esto y lo otro y unas veces sale bien y otras mal', 'Es posible, en  fin, que me equivoque sobre ciertos detalles muy importantes', 'Pero habrá que perdonármelo ya que mi amigo no me daba nunca muchas explicaciones', 'Me creía semejante a sí mismo y yo, desgraciadamente, no sé ver un cordero a través de una caja', 'Es posible que yo sea un poco como las personas mayores', 'He debido envejecer', 'Cada día yo aprendía algo nuevo sobre el planeta, sobre la partida y sobre el viaje', 'Esto venía suavemente al azar de las reflexiones', 'De esta manera tuve conocimiento al tercer día, del drama de los baobabs', 'Aprendí bien pronto a conocer mejor esta flor', 'Siempre había habido en el planeta del principito flores muy simples adornadas con una sola fila de pétalos que apenas ocupaban sitio y a nadie molestaban', 'Aparecían entre la hierba una mañana y por la tarde se extinguían', 'Aquella había germinado un día de una semilla llegada de quién sabe dónde', 'El principito había vigilado cuidadosamente desde el primer día aquella ramita', 'Podía ser una  nueva especie de Baobab', 'Pero el arbusto cesó pronto de crecer y comenzó a echar su flor', 'El principito observó el crecimiento de un enorme capullo', 'La flor no acababa de preparar su belleza al abrigo de su envoltura verde', 'Elegía con cuidado sus colores, se vestía lentamente y se ajustaba uno a uno sus pétalos', 'No quería salir ya ajada como las amapolas; quería aparecer en todo el esplendor de su belleza', 'Creo que el principito aprovechó la migración de una bandada de pájaros silvestres para su evasión', 'La mañana de la partida, puso en orden el planeta', 'Deshollinó cuidadosamente sus volcanes en actividad', 'Eran muy útiles para calentar el desayuno todas las mañanas', 'Tenía, además, un volcán extinguido', 'Deshollinó también el volcán extinguido, pues, como él decía, nunca se sabe lo que puede ocurrir', 'Si los volcanes están bien deshollinados, arden sus erupciones, lenta y regularmente', 'Las erupciones volcánicas son como el fuego de nuestras chimeneas', 'Es evidente que en nuestra Tierra no hay posibilidad de deshollinar los volcanes; los hombres somos demasiado pequeños', 'Por eso nos dan tantos disgustos', 'El principito arrancó también con un poco de melancolía los últimos brotes de baobabs', 'Creía que no iba a volver nunca', 'Pero todos aquellos trabajos le parecieron aquella mañana extremadamente dulces', 'Y cuando regó por última vez la flor y se dispuso a ponerla al abrigo del fanal, sintió ganas de llorar']

# words = []
# for sent in sentences:
#     words += get_words(sent)

words = ['MANERA', 'supe', 'segunda', 'cosa', 'importante', 'planeta', 'origen', 'apenas', 'grande', 'casa', 'podía', 'asombrarme', 'sabía', 'bien', 'aparte', 'grandes', 'planetas', 'tierra', 'Júpiter', 'marte', 'venus', 'cuales', 'dado', 'nombre', 'existen', 'centenares', 'tan', 'pequeños', 'veces', 'difícil', 'DISTINGUIRLOS', 'aun', 'ayuda', 'telescopio', 'astrónomo', 'descubre', 'Planetas', 'da', 'nombre', 'número', 'llama', 'ejemplo', 'asteroide', '3251', 'poderosas', 'razones', 'creer', 'planeta', 'venía', 'principito', 'asteroide', '612', 'asteroide', 'Sido', 'visto', 'sólo', 'vez', 'telescopio', '1909', 'ASTRÓNOMO', 'turco', 'astrónomo', 'hizo', 'gran', 'demostración', 'descubrimiento', 'congreso', 'internacional', 'astronomía', 'nadie', 'creyó', 'Causa', 'manera', 'vestir', 'personas', 'mayores', 'así', 'felizmente', 'reputación', 'asteroide', '612', 'dictador', 'turco', 'impuso', 'pueblo', 'bajo', 'pena', 'muerte', 'VESTIDO', 'europea', 'entonces', 'astrónomo', 'volvió', 'dar', 'cuenta', 'descubrimiento', '1920', 'lucía', 'traje', 'elegante', 'mundo', 'aceptó', 'demostración', 'si', 'contado', 'detalles', 'Asteroide', '612', 'confiado', 'número', 'consideración', 'personas', 'mayores', 'mayores', 'gustan', 'cifras', 'habla', 'NUEVO', 'amigo', 'jamás', 'preguntan', 'esencial', 'mismo', 'Sabemos', 'comprender', 'vida', 'burlamos', 'tranquilamente', 'números', 'gustado', 'comenzar', 'historia', 'manera', 'cuentos', 'hadas', 'gusta', 'libro', 'tomado', 'ligera', 'siento', 'tanta', 'Pena', 'contar', 'recuerdos', 'hace', 'seis', 'años', 'AMIGO', 'cordero', 'si', 'intento', 'describirlo', 'aquí', 'sólo', 'fin', 'olvidarlo', 'triste', 'olvidar', 'amigo', 'Amigo', 'puedo', 'llegar', 'ser', 'personas', 'mayores', 'sólo', 'interesan', 'cifras', 'evitar', 'comprado', 'caja', 'lápices', 'colores', 'ciertamente', 'trataré', 'hacer', 'retratos', 'PARECIDO', 'posibles', 'seguro', 'lograrlo', 'saldrá', 'bien', 'parecido', 'alguno', 'proporciones', 'equivoco', 'aquí', 'principito', 'demasiado', 'grande', 'allá', 'demasiado', 'pequeño', 'dudo', 'Color', 'traje', 'titubeo', 'unas', 'veces', 'sale', 'bien', 'mal', 'posible', 'fin', 'equivoque', 'ciertos', 'DETALLES', 'importantes', 'perdonármelo', 'amigo', 'daba', 'nunca', 'Muchas', 'explicaciones', 'creía', 'semejante', 'mismo', 'desgraciadamente', 'sé', 'ver', 'cordero', 'través', 'caja', 'posible', 'personas', 'mayores', 'debido', 'envejecer', 'cada', 'día', 'Aprendía', 'nuevo', 'planeta', 'partida', 'viaje', 'venía', 'SUAVEMENTE', 'azar', 'reflexiones', 'manera', 'conocimiento', 'tercer', 'día', 'drama', 'baobabs', 'aprendí', 'bien', 'pronto', 'Conocer', 'mejor', 'flor', 'siempre', 'planeta', 'principito', 'flores', 'simples', 'adornadas', 'sola', 'fila', 'pétalos', 'apenas', 'ocupaban', 'sitio', 'nadie', 'molestaban', 'aparecían', 'HIERBA', 'mañana', 'tarde', 'extinguían', 'aquella', 'germinado', 'día', 'semilla', 'llegada', 'quién', 'sabe', 'dónde', 'principito', 'vigilado', 'cuidadosamente', 'primer', 'día', 'aquella', 'Ramita', 'tan', 'diferente', 'conocía', 'podía', 'ser', 'nueva', 'especie', 'baobab', 'arbusto', 'cesó', 'pronto', 'CRECER', 'comenzó', 'echar', 'flor', 'principito', 'observó', 'Crecimiento', 'enorme', 'capullo', 'convencimiento', 'salir', 'allí', 'aparición', 'milagrosa', 'flor', 'acababa', 'preparar', 'belleza', 'abrigo', 'envoltura', 'verde', 'elegía', 'cuidado', 'colores', 'Vestía', 'lentamente', 'ajustaba', 'pétalos', 'quería', 'salir', 'AJADA', 'amapolas', 'quería', 'aparecer', 'esplendor', 'belleza', 'creo', 'principito', 'aprovechó', 'migración', 'bandada', 'pájaros', 'Silvestres', 'evasión', 'mañana', 'partida', 'puso', 'orden', 'planeta', 'deshollinó', 'cuidadosamente', 'volcanes', 'actividad', 'cuales', 'poseía', 'dos', 'útiles', 'calentar', 'desayuno', 'todas', 'MAÑANAS', 'además', 'volcán', 'extinguido', 'deshollinó', 'volcán', 'extinguido', 'pues', 'decía', 'nunca', 'sabe', 'puede', 'ocurrir', 'si', 'volcanes', 'bien', 'deshollinados', 'arden', 'Erupciones', 'lenta', 'regularmente', 'erupciones', 'volcánicas', 'fuego', 'chimeneas', 'evidente', 'tierra', 'posibilidad', 'deshollinar', 'volcanes', 'HOMBRES', 'demasiado', 'pequeños', 'dan', 'tantos', 'disgustos', 'Principito', 'arrancó', 'melancolía', 'últimos', 'brotes', 'baobabs', 'creía', 'iba', 'volver', 'nunca', 'aquellos', 'trabajos', 'parecieron', 'aquella', 'mañana', 'extremadamente', 'dulces', 'regó', 'Última', 'vez', 'flor', 'dispuso', 'ponerla', 'abrigo', 'FANAL', 'sintió', 'ganas', 'llorar']
stopw = ['de', 'esta', 'una', 'muy', 'su', 'de', 'era', 'más', 'que', 'una', 'esto', 'no', 'mucho', 'muy', 'que', 'de', 'los', 'como', 'la', 'a', 'los', 'se', 'les', 'ha', 'otros', 'de', 'ellos', 'a', 'que', 'es', 'con', 'la', 'del', 'cuando', 'un', 'uno', 'de', 'estos', 'le', 'por', 'un', 'le', 'por', 'el', 'tengo', 'para', 'que', 'el', 'del', 'cual', 'el', 'era', 'el', 'este', 'ha', 'una', 'con', 'el', 'en', 'por', 'un', 'este', 'una', 'de', 'su', 'en', 'un', 'de', 'pero', 'le', 'a', 'de', 'su', 'de', 'las', 'son', 'para', 'la', 'del', 'un', 'a', 'su', 'de', 'el', 'a', 'la', 'el', 'a', 'de', 'su', 'en', 'y', 'como', 'un', 'muy', 'todo', 'el', 'su', 'les', 'he', 'de', 'todos', 'estos', 'sobre', 'el', 'y', 'hasta', 'les', 'he', 'su', 'es', 'por', 'a', 'las', 'a', 'los', 'les', 'las', 'cuando', 'se', 'les', 'de', 'un', 'sobre', 'lo', 'del', 'pero', 'nosotros', 'que', 'la', 'nos', 'de', 'los', 'a', 'mí', 'me', 'habría', 'más', 'esta', 'a', 'la', 'de', 'los', 'de', 'porque', 'no', 'me', 'que', 'mi', 'sea', 'a', 'la', 'al', 'estos', 'ya', 'que', 'mi', 'se', 'fue', 'con', 'su', 'y', 'es', 'con', 'el', 'de', 'no', 'es', 'muy', 'a', 'un', 'no', 'todos', 'han', 'tenido', 'un', 'y', 'yo', 'a', 'como', 'las', 'que', 'se', 'por', 'las', 'para', 'esto', 'he', 'una', 'de', 'de', 'que', 'yo', 'de', 'lo', 'más', 'pero', 'no', 'estoy', 'muy', 'de', 'uno', 'y', 'otro', 'no', 'tiene', 'en', 'las', 'me', 'también', 'un', 'poco', 'el', 'es', 'y', 'es', 'también', 'sobre', 'el', 'de', 'su', 'sobre', 'esto', 'y', 'lo', 'otro', 'y', 'y', 'otras', 'es', 'en', 'que', 'me', 'sobre', 'muy', 'pero', 'habrá', 'que', 'ya', 'que', 'mi', 'no', 'me', 'me', 'a', 'sí', 'y', 'yo', 'no', 'un', 'a', 'de', 'una', 'es', 'que', 'yo', 'sea', 'un', 'poco', 'como', 'las', 'he', 'yo', 'algo', 'sobre', 'el', 'sobre', 'la', 'y', 'sobre', 'el', 'esto', 'al', 'de', 'las', 'de', 'esta', 'tuve', 'al', 'del', 'de', 'los', 'a', 'esta', 'había', 'habido', 'en', 'el', 'del', 'muy', 'con', 'una', 'de', 'que', 'y', 'a', 'entre', 'la', 'una', 'y', 'por', 'la', 'se', 'pero', 'había', 'un', 'de', 'una', 'de', 'y', 'el', 'había', 'desde', 'el', 'de', 'las', 'que', 'él', 'una', 'de', 'pero', 'el', 'de', 'y', 'a', 'su', 'el', 'el', 'de', 'un', 'y', 'tenía', 'le', 'de', 'que', 'habría', 'de', 'de', 'una', 'pero', 'la', 'no', 'de', 'su', 'al', 'de', 'su', 'con', 'sus', 'se', 'y', 'se', 'uno', 'a', 'uno', 'sus', 'no', 'ya', 'como', 'las', 'en', 'todo', 'el', 'de', 'su', 'que', 'el', 'la', 'de', 'una', 'de', 'para', 'su', 'la', 'de', 'la', 'en', 'el', 'sus', 'en', 'de', 'los', 'que', 'le', 'eran', 'muy', 'para', 'el', 'las', 'tenía', 'un', 'también', 'el', 'como', 'él', 'se', 'lo', 'que', 'los', 'están', 'sus', 'y', 'las', 'son', 'como', 'el', 'de', 'nuestras', 'es', 'que', 'en', 'nuestra', 'no', 'hay', 'de', 'los', 'los', 'somos', 'por', 'eso', 'nos', 'el', 'también', 'con', 'un', 'poco', 'de', 'los', 'de', 'que', 'no', 'a', 'pero', 'todos', 'le', 'y', 'cuando', 'por', 'la', 'y', 'se', 'a', 'al', 'del', 'de']

functions = ["isalpha()", "isnumeric()", "islower()", "isupper()","capitalize()", "lower()", "upper()"]

num_operators = ["+", "-", "*"]
num_comp = ["==", "<", ">", ">=", "<="]

str_operators = ["+", "in"]


## Exercises
import random

def ex1():
    word = random.choice(words)
    return f'a = "{word}"\nprint(a.upper())\n'

def ex2():
    word = random.choice(words)
    a = random.randint(0, len(word)-1)
    if a == len(word)-1:
        b = a - random.randint(1, a)
    else:
        b = a + random.randint(1, len(word) - a - 1)
    a, b = min(a, b), max(a, b)
    return f'a = "{word}"\nprint(a[{a}:{b}])\n'

def ex3():
    word1 = random.choice(words)
    word2 = random.choice(words)
    return f'a = "{word1}" + "{word2}"\nprint(a)\n'

def ex4():
    word = random.choice(words)
    return f'a = "{word}".capitalize()\nprint(a.islower())\n'

def ex5():
    word = random.choice(stopw)
    sent = random.choice(sentences)
    return f'a = "{word}".lower()\nb = "{sent}"\nprint(a in b)\n'

def ex6():
    word = random.choice(words)
    sent = random.choice(sentences)
    word_in_sent = sent.split()
    phrase_idx = random.randint(0, len(word_in_sent)-3)
    phrase = ' '.join(word_in_sent[phrase_idx:phrase_idx+2])
    return f'a = "{sent}"\nb = "{word}"\nprint(a.replace("{phrase}", b))\n'

def ex7():
    word = random.choice(words)
    prob = random.uniform(0, 1)
    if  prob < 0.33:
        word += str(random.randint(0, 20))
    elif prob < 0.66:
        word = random.randint(0, 1000)
    return f'a = "{word}"\nprint(a.isalpha())\n'

def ex8():
    word = random.choice(words)
    n = random.randint(1, len(word))
    comp = random.choice(num_comp)
    return f'a = "{word}"\nprint(len(a) {comp} {n})\n'

def ex9():
    n1 = random.uniform(0, 10)
    n2 = random.randint(0, 10)
    op = random.choice(num_operators)
    return f'a = {n1:.1f}\nb = {n2}\nprint(a {op} b)\n'

def ex10():
    sent = random.choice(sentences)
    if random.uniform(0, 1) <= 0.5:
        word = sent.split()[-1]
    else:
        word = random.choice(words)
    return f'a = "{sent}"\nb = "{word}"\nprint(a.endswith(b))\n'

def ex11():
    sent = random.choice(sentences)
    if random.uniform(0, 1) <= 0.5:
        word = sent.split()[0]
        if random.uniform(0, 1) <= 0.3:
            word = word.lower()
    else:
        word = random.choice(words)
    return f'a = "{sent}"\nb = "{word}"\nprint(a.startswith(b))\n'

def ex12():
    word = random.choice(words)
    return f'a = "{word}"\nprint(a.lower())\n'

def ex13():
    word = random.choice(words)
    return f'a = "{word}"\nprint(a.capitalize())\n'

def ex14():
    word = random.choice(words)
    return f'a = "{word}"\nprint(a.islower())\n'

def ex15():
    word = random.choice(words)
    prob = random.uniform(0, 1)
    if  prob < 0.33:
        word += str(random.randint(0, 20))
    elif prob < 0.66:
        word = random.randint(0, 1000)
    return f'a = "{word}"\nprint(a.isnumeric())\n'

def ex16():
    word = random.choice(words)
    size = len(word)
    return f'a = "{word}" \nb = {size}\nprint(f"La palabra ' + '{a} tiene {b} letras")\n'

def ex17():
    word = random.choice(words)
    a = random.randint(1, len(word))
    return f'a = "{word}"\nprint(a[{a}])\n'

def ex18():
    word = random.choice(words)
    a = random.randint(1, len(word))
    return f'a = "{word}"\nprint(a[-{a}])\n'

def ex19():
    word = random.choice(words)
    a = random.randint(0, len(word)-1)
    return f'a = "{word}"\nprint(a[{a}:])\n'

def ex20():
    word = random.choice(words)
    a = random.randint(0, len(word)-1)
    return f'a = "{word}"\nprint(a[:{a}])\n'

# print(ex19())

# a=sentence print(sentence) 1
# a=word print(len(a)) 1
# a=word print(word.function()) 7
# a=word print(word[random_number]) 1
# a=word print(word[random_number:random_number]) 1
# a=word b=word print(a + ' ' + b) 1
# a=word b=sentence print(a in sentence) 1
# a=number b=number print(a operator b) 6
# a=sentence b=word print(a.replace(some word in sentence, b)) 1
# a=sentence b=word print(a.startswith(first_word or b [with prob 0.5])) 1
# a=sentence b=word print(a.endsswith(last_word or b [with prob 0.5])) 1

