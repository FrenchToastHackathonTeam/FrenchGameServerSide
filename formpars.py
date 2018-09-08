import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import numpy as np

def next_available_row(sheet):
	str_list = list(filter(None, sheet.col_values(1)))
	return str(len(str_list))

def get_vocabulary():
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	sheet = client.open('Teacher Form (Responses)').sheet1

	arr = [
		"הממ… הדבר שרואים פה הוא {}",
		"טוב, עכשיו צריך למצוא {}", 
		"אני חושב שעכשיו צריך {}",
		"עכשיו תמצאו {}",
		"נראה לי כדאי למצוא {}",
		"יש טביעות אצבעות על {}",
	]

	l = []
	uniq_words = sheet.cell(next_available_row(sheet), 2).value.split(',')
	random.shuffle(uniq_words)
	ran = np.random.choice(arr ,len(uniq_words))
	for sentance_blank, word in zip(ran, uniq_words):
		french_word, english_word = word.strip().split(" - ")
		l.append({
			"text": sentance_blank.format(french_word),
			"word": english_word
		})
		
	#cur = [var.strip() for var in sheet.cell(next_available_row(sheet), 2).value.split(',')]
	return {"data": l, "intro": ["הו לא! גנבו את המונה ליזה! איזה מזל שבמצלמות האבטחה שלנו רואים בבירור מספר חפצים שהגנבת הפילה בדרך מהמוזיאון.", 
	"אם נעקוב אחריהם, נמצא לאן היא ברחה!", 
	"מה איתי? אני… אני מיד מאחוריך. קדימה, אין זמן לאבד!"]}