from selenium import webdriver
import time

url = "https://app.sli.do/event/z0l48p5b/live/questions"
question_id = 19801553

while True:
    try:
        driver = webdriver.Chrome(executable_path="./chromedriver")
        driver.get(url)
        time.sleep(5)
        driver.execute_script("""document.querySelector('[data-qid="{}"] button').click()""".format(question_id))
        driver.close()
    except:
        pass
