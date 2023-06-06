import pymorphy2
import nltk

def save_results(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

morph = pymorphy2.MorphAnalyzer()

# Task 1
results = str(len(morph.parse('блестящий')))
save_results('task1.txt', results)

# Task 2
results = []
for i in morph.parse('блестящий'):
    result = f"Word: {i.word}\nTag: {i.tag}\nNormal Form: {i.normal_form}\nPOS: {i.tag.POS}\nCyrillic Representation: {i.tag.cyr_repr}\nScore: {i.score}\n"
    results.append(result)
save_results('task2.txt', ''.join(results))

# Task 3
results = []
for i in morph.parse('блестящий'):
    if 'ADJF' in i.tag:
        result = f"Word: {i.word}\n\nMorphological Categories for Adjective:\nGender: {i.tag.gender}\nAnimacy: {i.tag.animacy}\nNumber: {i.tag.number}\nCase: {i.tag.case}\n\nMorphological Categories for Participle:\nAspect: {i.tag.aspect}\nTense: {i.tag.tense}\nTransitivity: {i.tag.transitivity}\nVoice: {i.tag.voice}\nCase: {i.tag.case}\nNumber: {i.tag.number}\nGender: {i.tag.gender}\n"
        results.append(result)
save_results('task3.txt', ''.join(results))

# Task 4-5
results = "творительный падеж множественного числа\n"
for i in morph.parse('блестящими'):
    lexemes = ', '.join(lexeme.word for lexeme in i.lexeme)
    result = f"Word: {i.word}\nLexemes: {lexemes}\n"
    results += result
save_results('task4-5.txt', results)

# Task 6
text = "Раскрыл я с тихим шорохом глаза страниц … И потянуло порохом от всех границ. Не вновь, которым за двадцать, в грозе расти. Нам не с чего радоваться, но нечего грустить. Бурна вода истории. Угрозы и войну мы взрежем на просторе, как режет киль волну."
tokens = nltk.word_tokenize(text)
patterns = []
for i in tokens:
    patterns += [(i, morph.parse(i)[0].tag.POS)]
regexp_tagger = nltk.RegexpTagger(patterns)
tagged_tokens = regexp_tagger.tag(tokens)

results = f"Token Patterns: {patterns}\nTagged Tokens: {tagged_tokens}\nNumber of Tokens: {len(tokens)}\nNumber of Tagged Tokens: {len(tagged_tokens)}\n"
save_results('task6.txt', results)

# Task 7
results = "---украинский язык--------------\n"
morph = pymorphy2.MorphAnalyzer(lang='uk')
results += str(len(morph.parse('прикордонний'))) + '\n'
for i in morph.parse('прикордонний'):
    result = f"Word: {i.word}\nTag: {i.tag}\nNormal Form: {i.normal_form}\nPOS: {i.tag.POS}\nCyrillic Representation: {i.tag.cyr_repr}\nScore: {i.score}\n"
    results += result
save_results('task7.txt', results)

text = "А роки йдуть, вперед крокують Вже молоді літа не ті. Недоберу чого бракує В моїм щоденному житті. І тіж " \
       "веселі майські ночі І тіж весняні теплі дні І не умер ніхто з рідні Та деж другії карі очі. Та молоді слова " \
       "дівочі І де усмішка із лиця Та де горячі поцілунки Й з моїм споріднені серця."
tokens = nltk.word_tokenize(text)
patterns = []
for i in tokens:
    patterns += [(i, morph.parse(i)[0].tag.POS)]
regexp_tagger = nltk.RegexpTagger(patterns)
tagged_tokens = regexp_tagger.tag(tokens)

results = f"Token Patterns: {patterns}\nTagged Tokens: {tagged_tokens}\nNumber of Tokens: {len(tokens)}\nNumber of Tagged Tokens: {len(tagged_tokens)}\n"
save_results('task7.txt', results)
