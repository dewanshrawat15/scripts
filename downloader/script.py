from selenium import webdriver 
import time
import os
from os import system, name
import urllib.request

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def instagram_dp(username):
	base = "https://instagram.com/"
	link = base + username
	browser = webdriver.Chrome()
	browser.get(link)
	elem = browser.find_element_by_class_name('be6sR')
	img = elem.get_attribute('src')
	browser.close()

	play = webdriver.Chrome()
	play.get(img)
	play.close()

	file = urllib.request.urlretrieve(img, "profile.jpg")
	resize(file)
	browser.close()

def main():
	clear()
	print("This small script downloads the instagram profile picture of any person you want ")
	time.sleep(1)
	user = input("Enter the username of the person whose profile picture is to be seen: ")
	instagram_dp(user)

main()