#Specify a word and language and have it download the word voiced by google translate in that language

#http://translate.google.com/translate_tts?tl=it&q="abitate"
#italian

#http://translate.google.com/translate_tts?tl=cs&q="abitate"
#czech

def download_translate(word, language):
	lang = language
	query = word
	url = "http://translate.google.com/translate_tts?tl=" + lang + "&q=\"" + query + "\""
	pass


