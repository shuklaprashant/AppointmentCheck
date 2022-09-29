import time
from notify import notify_call, notify_text
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Remote('http://selenium:4444/wd/hub',
desired_capabilities=DesiredCapabilities.CHROME)

# driver = webdriver.Chrome("./chromedriver")
driver.get("https://ais.usvisa-info.com/en-gb/niv/users/sign_in")

usernName = driver.find_element_by_id("user_email")
if usernName:
    usernName.send_keys("prashant_978737@yahoo.co.in")

password = driver.find_element_by_id("user_password")
if password:
    password.send_keys("Jan@2022")

policy_checked = driver.find_element_by_xpath("//*[@id='new_user']/div[3]/label/div")
if policy_checked:
    policy_checked.click()

sign_in = driver.find_element_by_name("commit")
if sign_in:
    sign_in.click()

time.sleep(2)

appointment_continue = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul/li/a")
if appointment_continue:
    appointment_continue.click()

reschedule_appointment_tile = driver.find_element_by_xpath('//*[@id="forms"]/ul/li[4]')
if reschedule_appointment_tile:
    reschedule_appointment_tile.click()

reschedule_appointment = driver.find_element_by_xpath("//a[contains(text(),'Reschedule Appointment')]")
if reschedule_appointment:
    driver.execute_script("arguments[0].click();", reschedule_appointment)

appointments_status = driver.find_element_by_id("consulate_date_time_not_available")
if appointments_status:
    no_appointment_available = appointments_status.text
    # assert no_appointment_available == "There are no available appointments at the selected location. Please try again later."
    if no_appointment_available != "There are no available appointments at the selected location. Please try again later.":
        notify_call()
    else:
        notify_text()
        # time.sleep(60)
        print("Nothing found!")

driver.close()