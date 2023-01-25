import spacy
nlp = spacy.load("de_core_news_sm")
doc = nlp("Als liebevoller Gastgeber möchte ich meine Freunde einladen, damit wir z.B. einen schönen Abend zusammen verbringen können.")
print([(w.text, w.dep_) for w in doc])

print(spacy.explain("cp"))

for token in doc:
  if ("mo" in token.dep_):
    subtree = list(token.subtree)
    start = subtree[0].i
    end = subtree[-1].i + 1
    print(doc[start:end])

from spacy import displacy
displacy.serve(doc, style="dep")
