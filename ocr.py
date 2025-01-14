import sys
from PIL import Image
import pytesseract
from googletrans import Translator
from pypinyin import pinyin, Style

cn_txt = pytesseract.image_to_string(Image.open(sys.stdin.read().strip()), lang="chi_sim")
translator = Translator()
en_txt = translator.translate(cn_txt, src='zh-CN', dest='en')
print(en_txt.text)
pinyin_txt = pinyin(cn_txt.text, style=Style.TONE3)
print(" ".join([word[0] for word in pinyin_txt]))
