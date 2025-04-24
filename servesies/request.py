from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from db import db


class GetUrl:
    def __init__(self, url):
        self.url = url

    def conn(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        return driver

    async def get_url(self):
        driver = self.conn()
        i = 2
        while True:
            try:
                vacancy = driver.find_element(By.CSS_SELECTOR, f"#a11y-main-content > div:nth-child({i})")
                link_div = vacancy.find_element(By.CSS_SELECTOR,
                                                f"#a11y-main-content > div:nth-child({i}) > div > div.magritte-card___bhGKz_7-0-6.magritte-card-style-primary___eZ6aX_7-0-6.magritte-card-shadow-level-0___RNbQK_7-0-6.magritte-card-stretched___0Uc0J_7-0-6.magritte-card-press-enabled___kXfCl_7-0-6.magritte-card-hover-enabled___-wolU_7-0-6.magritte-increase-shadow___Lvfmm_7-0-6.magritte-border-default___eT8Lg_7-0-6 > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.vacancy-info--ieHKDTkezpEj0Gsx > h2 > span > a")
                link = link_div.get_attribute('href')
                print(link)
                await db.insert_db(link)
                i += 1
            except:
                i += 4


class GetInfo(GetUrl):
    def __init__(self, url):
        super().__init__(url)

    def get_stat(self):
        property_list = []
        driver = self.conn()
        try:
            vacancy_name = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div:nth-child(1) > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.magritte-card___bhGKz_7-0-6.magritte-card-style-primary___eZ6aX_7-0-6.magritte-card-shadow-level-0___RNbQK_7-0-6.magritte-card-stretched___0Uc0J_7-0-6 > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.vacancy-title > h1"))
            )
            vacancy_name = vacancy_name.text
        except:
            vacancy_name = 'Не указано'
        try:
            company = driver.find_element(By.CSS_SELECTOR,
                                          "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-0 > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-6 > div > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div.magritte-h-spacing-container___rrYJZ_2-0-44 > div > div.vacancy-company-details > span > a > span")
            company = company.text
        except:
            company = "Не указано"
        try:
            salary = driver.find_element(By.CSS_SELECTOR,
                                         "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div:nth-child(1) > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.magritte-card___bhGKz_7-0-6.magritte-card-style-primary___eZ6aX_7-0-6.magritte-card-shadow-level-0___RNbQK_7-0-6.magritte-card-stretched___0Uc0J_7-0-6 > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.vacancy-title > div.magritte-text___pbpft_3-0-32.magritte-text_style-primary___AQ7MW_3-0-32.magritte-text_typography-paragraph-2-regular___VO638_3-0-32 > span")
            salary = salary.text
        except:
            salary = 'Не указано'
        try:
            exp = driver.find_element(By.CSS_SELECTOR,
                                      "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div:nth-child(1) > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.magritte-card___bhGKz_7-0-6.magritte-card-style-primary___eZ6aX_7-0-6.magritte-card-shadow-level-0___RNbQK_7-0-6.magritte-card-stretched___0Uc0J_7-0-6 > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.magritte-v-spacing-container___mkW1c_2-0-44 > p:nth-child(1) > span")
            exp = exp.text
        except:
            exp = 'Не указано'
        try:
            type_work = driver.find_element(By.CSS_SELECTOR,
                                            "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div:nth-child(1) > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.magritte-card___bhGKz_7-0-6.magritte-card-style-primary___eZ6aX_7-0-6.magritte-card-shadow-level-0___RNbQK_7-0-6.magritte-card-stretched___0Uc0J_7-0-6 > div.magritte-icon-dynamic___KJ4yJ_10-2-0.magritte-icon-dynamic_full-width___vgWH5_10-2-0 > div > div > div > div.magritte-v-spacing-container___mkW1c_2-0-44 > p:nth-child(5)")
            type_work = type_work.text
        except:
            type_work = 'Не указано'
        try:
            requirements = driver.find_element(By.CSS_SELECTOR,
                                               "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div.vacancy-description > div.bloko-columns-row > div > div.vacancy-section.vacancy-section_magritte > div:nth-child(3) > ul")
            requirements = requirements.text.split('\n')
        except:
            requirements = ['Не указано']
        # region = driver.find_element(By.CSS_SELECTOR,"")
        try:
            date = driver.find_element(By.CSS_SELECTOR,
                                       "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div:nth-child(5) > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10 > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-8 > div > p")
            date = date.text
        except:
            date = 'Не указано'
        property_list.extend([vacancy_name, company, salary, exp, type_work, requirements, date])
        driver.close()
        return property_list
