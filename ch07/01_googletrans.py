from googletrans import Translator

def google_trans(message):
    google = Translator()
    result = google.translate(message, dest='ko')
    return result.text

text = '''
Black tea (also literally translated as red tea from various East Asian languages) is a type of tea that is more oxidized than oolong, yellow, white and green teas. Black tea is generally stronger in flavour than other teas. All five types are made from leaves of the shrub (or small tree) Camellia sinensis, though Camellia taliensis is also used rarely.
'''

result = google_trans(text)
print(result)
