import deepl

apikey = "YOUR_API_KEY"
trans = deepl.Translator(apikey)

text = '''
Black tea (also literally translated as red tea from various East Asian languages) is a type of tea that is more oxidized than oolong, yellow, white and green teas. Black tea is generally stronger in flavour than other teas. All five types are made from leaves of the shrub (or small tree) Camellia sinensis, though Camellia taliensis is also used rarely.
'''

result = trans.translate_text(text, target_lang='ko')
print(result) 