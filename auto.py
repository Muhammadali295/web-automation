from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdgOTWcuesVLMrkiiG8D3NOkY3fgM-6DRORcLpm5fRmOmmWSg/viewform?usp=sf_link')
time.sleep(3)

Name1 = "ali"
Name2 = "saad"
Name3 = "sample"
Name4 = "basit"
n = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

r10 = web.find_element('xpath','//*[@id="i9"]/div[3]/div')
r11 = web.find_element('xpath','//*[@id="i12"]/div[3]/div')
r12 = web.find_element('xpath','//*[@id="i15"]/div[3]/div')
r20 = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')
r21 = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')
r22 = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')
r23 = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span')
r24 = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[5]/label/div/div[2]/div/span')
r25 = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[6]/label/div/div[2]/div/span')
r26 = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[7]/label/div/div[2]/div/span')
r30 = web.find_element('xpath','//*[@id="i51"]/div[3]/div')
r31 = web.find_element('xpath','//*[@id="i54"]/div[3]/div')
r32 = web.find_element('xpath','//*[@id="i57"]/div[3]/div')
r40 = web.find_element('xpath','//*[@id="i67"]/div[3]/div')
r41 = web.find_element('xpath','//*[@id="i70"]/div[3]/div')
r42 = web.find_element('xpath','//*[@id="i73"]/div[3]/div')
r43 = web.find_element('xpath','//*[@id="i79"]/div[3]/div')
m = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')

# a = 2
# b = 3
# c = 4
# d = 3
# # ali
# # case 3

# a = 2
# b = 4
# c = 4
# d = 4
# # saad
# # case 1

# a = 3
# b = 2
# c = 4
# d = 4
# # basit
# # case 2

a = 2
b = 4
c = 3
d = 4
# sample
# case 1

if a < b:
  if c > d:
  # Perform actions or assertions for this condition
    n.send_keys(Name1)
  elif c == d:
    n.send_keys(Name2)
  else:
    n.send_keys(Name3)
else:
  n.send_keys(Name4)
if a+b>5:
  r10.click()
  r20.click()
  r21.click()
  r22.click()
  r30.click()
  r40.click()
  m.send_keys('test case 1')
elif a>b:
  r11.click()
  r23.click()
  r24.click()
  r31.click()
  r41.click()
  m.send_keys('test case 2')
else:
  r12.click()
  r25.click()
  r26.click()
  r32.click()
  r42.click()
  m.send_keys('test case 3')
time.sleep(3)
submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()
get_confirmation_div_text = web.find_element(By.CSS_SELECTOR,'.vHW8K')
print(get_confirmation_div_text.text)
if ((get_confirmation_div_text.text) == "Your response has been recorded."):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")
time.sleep(3)