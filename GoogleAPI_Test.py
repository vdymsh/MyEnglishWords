#
# Pre-requirements:
# pip install googletrans
#
from googletrans import Translator

translator = Translator()
ans = translator.translate('Reveal', src='en', dest='ru')
print(ans)
print(ans.text)
