from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "YOUR EMAIL"
ACCOUNT_PASSWORD = "YOUR PASSWORD"
PHONE = YOUR NUMBER

service = Service("/Users/bjornstenberg/Development/chromedriver")
# Capital Letter means OBJECT
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3124743619&f_AL=true&f_E=2&f_JT=F%2CP&geoId="
           "104853962&keywords=python%20&location=Stockholm%20County%2C%20Sweden&refresh=true&sortBy=R")


# Sign in to Account
sign_in = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]").click()
time.sleep(2)

user_email = driver.find_element(By.ID, value="username").send_keys(ACCOUNT_EMAIL)
time.sleep(2)

user_password = driver.find_element(By.ID, value="password").send_keys(ACCOUNT_PASSWORD)

time.sleep(2)

log_in = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
log_in.click()

time.sleep(2)

all_jobs_listings = driver.find_elements(by=By.CSS_SELECTOR,value=".job-card-container--clickable")
for job_listing in all_jobs_listings:
    print("called")
    job_listing.click()
    time.sleep(5)

    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-apply-button--top-card")
        apply_button.click()
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button span")
        if submit_button.text == "Next":
            close_button = driver.find_element(by=By.CSS_SELECTOR, value="#artdeco-modal-outlet button")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex Application, Skipped.")
            continue
        else:
            submit_button.click()
            print("Application Submitted")
        # After application Submitted LinkedIn will show a pop-up to take assesment.
        time.sleep(2)
        take_assesment_close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        take_assesment_close_button.click()

    except NoSuchElementException:
        print("No application button, Skipped.")
        continue

time.sleep(5)
driver.quit()

