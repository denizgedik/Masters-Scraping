from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from seleniumwire import webdriver
import csv
import undetected_chromedriver as uc
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

options = uc.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)

links = [
"https://www.mastersportal.com/studies/35913/research-on-teaching-and-learning.html?ref=search_card",
"https://www.mastersportal.com/studies/3982/psychology-learning-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/22397/educational-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/22397/educational-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/14478/education-and-training-management.html?ref=search_card",
"https://www.mastersportal.com/studies/305670/developmental-and-educational-psychology.html?ref=search_card",
"https://www.mastersportal.com/studies/201230/educational-leadership-management-and-emerging-technologies.html?ref=search_card",
"https://www.mastersportal.com/studies/365843/humanities-research-environmental-humanities.html?ref=search_card",
"https://www.mastersportal.com/studies/294697/educational-psychology-learning-and-performance.html?ref=search_card",
"https://www.mastersportal.com/studies/304068/research-master-business-data-science.html?ref=search_card#content:contents",
"https://www.mastersportal.com/studies/749/educational-studies.html?ref=search_card",
"https://www.mastersportal.com/studies/112786/youth,-education-and-society.html?ref=search_card",
"https://www.mastersportal.com/studies/343974/education-leadership-and-management.html?ref=search_card",
"https://www.mastersportal.com/studies/506/sociology-and-social-research.html?ref=search_card",
"https://www.mastersportal.com/studies/304046/humanities-research.html?ref=search_card",
"https://www.mastersportal.com/studies/370517/societal-resilience.html?ref=search_card",
"https://www.mastersportal.com/studies/365843/humanities-research-environmental-humanities.html?ref=search_card",
"https://www.mastersportal.com/studies/336340/learning,-digitalization,-and-sustainability-(leads).html?ref=search_card",
"https://www.mastersportal.com/studies/343499/cultural-heritage.html?ref=search_card",
"https://www.mastersportal.com/studies/314673/early-childhood-education.html?ref=search_card",
"https://www.mastersportal.com/studies/89740/education-and-training-management-(elearning).html?ref=search_card",
"https://www.mastersportal.com/studies/23727/psychology-(conversion-degree).html?ref=search_card",
"https://www.mastersportal.com/studies/303014/teaching,-learning-and-media-education.html?ref=search_card",
"https://www.mastersportal.com/studies/24504/education-and-sociology.html?ref=search_card",
"https://www.mastersportal.com/studies/314644/psychology-(conversion).html?ref=search_card",
"https://www.mastersportal.com/studies/340711/technical-design-and-technology-education.html?ref=search_card",
"https://www.mastersportal.com/studies/16723/psychology.html?ref=search_card",
"https://www.mastersportal.com/studies/286752/changing-education.html?ref=search_card",
"https://www.mastersportal.com/studies/240221/guidance-counselling.html?ref=search_card",
"https://www.mastersportal.com/studies/240213/specific-learning-difficulties-(dyslexia).html?ref=search_card",
"https://www.mastersportal.com/studies/360326/advanced-research-methods-and-social-analysis-innovations.html?ref=search_card",
"https://www.mastersportal.com/studies/314669/education.html?ref=search_card",
"https://www.mastersportal.com/studies/13231/psychology.html?ref=search_card",
"https://www.mastersportal.com/studies/11102/psychology-of-education.html?ref=search_card",
"https://www.mastersportal.com/studies/240215/masters-in-special-educational-needs.html?ref=search_card",
"https://www.mastersportal.com/studies/351902/data-science.html?ref=search_card",
"https://www.mastersportal.com/studies/263729/big-data-management.html?ref=search_card",
"https://www.mastersportal.com/studies/320479/data-science.html?ref=search_card",
"https://www.mastersportal.com/studies/363219/data-science.html?ref=search_card",
"https://www.mastersportal.com/studies/313300/psychology.html?ref=search_card",
"https://www.mastersportal.com/studies/3982/psychology-learning-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/271/higher-education.html?ref=search_card",
"https://www.mastersportal.com/studies/13178/sociology-social-research.html?ref=search_card",
"https://www.mastersportal.com/studies/287691/early-childhood-research.html?ref=search_card",
"https://www.mastersportal.com/studies/268633/international-education-and-development.html?ref=search_card",
"https://www.mastersportal.com/studies/373069/education.html?ref=search_card",
"https://www.mastersportal.com/studies/43628/research-master.html?ref=search_card",
"https://www.mastersportal.com/studies/35913/research-on-teaching-and-learning.html?ref=search_card",
"https://www.mastersportal.com/studies/50909/social-sciences-and-educational-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/50911/psychology-psychological-intervention.html?ref=search_card",
"https://www.mastersportal.com/studies/355246/education-(teaching-and-learning).html?ref=search_card",
"https://www.mastersportal.com/studies/202591/teaching-and-learning.html?ref=search_card",
"https://www.mastersportal.com/studies/305670/developmental-and-educational-psychology.html?ref=search_card",
"https://www.mastersportal.com/studies/70806/teaching-and-learning-english-as-a-foreign-second-language.html?ref=search_card",
"https://www.mastersportal.com/studies/351546/education-(mentoring,-leading-and-global-learning).html?ref=search_card",
"https://www.mastersportal.com/studies/340711/technical-design-and-technology-education.html?ref=search_card",
"https://www.mastersportal.com/studies/340709/access-to-education-in-inclusive-schools-and-communities.html?ref=search_card",
"https://www.mastersportal.com/studies/340708/access-to-education-in-culturally-responsive-education.html?ref=search_card",
"https://www.mastersportal.com/studies/232237/msc-smartedtech,-co-creativity-&-technology-enhanced-learning.html?ref=search_card",
"https://www.mastersportal.com/studies/225335/educational-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/66812/educational-psychology.html?ref=search_card",
"https://www.mastersportal.com/studies/292109/educational-science-%E2%80%93-teaching-and-learning.html?ref=search_card",
"https://www.mastersportal.com/studies/22397/educational-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/314638/education-international-education.html?ref=search_card",
"https://www.mastersportal.com/studies/357762/educational-science.html?ref=search_card",
"https://www.mastersportal.com/studies/27976/intercultural-communication-and-european-studies.html?ref=search_card",
"https://www.mastersportal.com/studies/363277/comparative-studies-in-english-and-american-language,-literature-and-culture.html?ref=search_card",
"https://www.mastersportal.com/studies/307703/european-languages.html?ref=search_card",
"https://www.mastersportal.com/studies/313932/european-studies.html?ref=search_card",
"https://www.mastersportal.com/studies/290/development,-environment-and-cultural-change.html?ref=search_card",
"https://www.mastersportal.com/studies/268633/international-education-and-development.html?ref=search_card",
"https://www.mastersportal.com/studies/107857/sustainable-development.html?ref=search_card",
"https://www.mastersportal.com/studies/305670/developmental-and-educational-psychology.html?ref=search_card",
"https://www.mastersportal.com/studies/104420/gender-studies.html?ref=search_card",
"https://www.mastersportal.com/studies/299482/life-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/50909/social-sciences-and-educational-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/313337/applied-experimental-psychological-sciences-(aeps).html?ref=search_card",
"https://www.mastersportal.com/studies/308437/mind-and-brain.html?ref=search_card",
"https://www.mastersportal.com/studies/241242/psychology,-neuroscience-and-human-sciences.html?ref=search_card",
"https://www.mastersportal.com/studies/13178/sociology-social-research.html",
"https://www.mastersportal.com/studies/287691/early-childhood-research.html",
"https://www.mastersportal.com/studies/3982/psychology-learning-sciences.html",
"https://www.mastersportal.com/studies/313337/applied-experimental-psychological-sciences.html",
"https://www.mastersportal.com/studies/50909/social-sciences-and-educational-sciences.html",
"https://www.mastersportal.com/studies/313337/applied-experimental-psychological-sciences.html",
"https://www.mastersportal.com/studies/248755/education-sciences.html",
"https://www.mastersportal.com/studies/355246/education.html",
"https://www.mastersportal.com/studies/340711/technical-design-and-technology-education.html",
"https://www.mastersportal.com/studies/76079/social-research.html",
"https://www.mastersportal.com/studies/313337/applied-experimental-psychological-sciences.html#content:requirement",
"https://www.mastersportal.com/studies/100471/international-studies-in-education.html#content:requirement",
"https://www.mastersportal.com/studies/308437/mind-and-brain.html#content:requirement",
"https://www.mastersportal.com/studies/340520/youth-and-community-studies.html",
"https://www.mastersportal.com/studies/292148/psychology-cognitive-psychology-learning-and-work.html#content:requirement",
"https://www.mastersportal.com/studies/1575/psychology-evaluation-and-assessment.html#content:requirement",
"https://www.mastersportal.com/studies/240470/project-management.html",
"https://www.mastersportal.com/studies/336330/global-studies-sustainable-societies-and-social-change.html#content:requirement",
"https://www.mastersportal.com/studies/268633/international-education-and-development.html",
"https://www.mastersportal.com/studies/30845/european-studies.html#content:requirement",
"https://www.mastersportal.com/studies/303556/management.html",
"https://www.mastersportal.com/studies/35913/research-on-teaching-and-learning.html",
"https://www.mastersportal.com/studies/341523/digital-transformation-management.html",
"https://www.mastersportal.com/studies/299485/digital-sciences.html#content:requirement",
"https://www.mastersportal.com/studies/333561/management-of-innovation-and-entrepreneurship.html#content:requirement",
"https://www.mastersportal.com/studies/256618/global-development-and-entrepreneurship.html",
"https://www.mastersportal.com/studies/295998/life-sciences.html#content:requirement",
"https://www.mastersportal.com/studies/295996/digital-sciences.html#content:requirement",
"https://www.mastersportal.com/studies/295999/learning-sciences.html",
'https://www.mastersportal.com/studies/268633/international-education-and-development.html?ref=search_card',
'https://www.mastersportal.com/studies/100471/international-studies-in-education.html?ref=search_card',
'https://www.mastersportal.com/studies/287691/early-childhood-research.html?ref=search_card',
'https://www.mastersportal.com/studies/373069/education.html?ref=search_card',
'https://www.mastersportal.com/studies/363481/vocational-education-and-innovation.html?ref=search_card',
'https://www.mastersportal.com/studies/295999/learning-sciences.html?ref=search_card',
'https://www.mastersportal.com/studies/35913/research-on-teaching-and-learning.html?ref=search_card',
'https://www.mastersportal.com/studies/50909/social-sciences-and-educational-sciences.html?ref=search_card',
'https://www.mastersportal.com/studies/248755/education-sciences.html?ref=search_card',
'https://www.mastersportal.com/studies/266908/secondary-education-teaching.html?ref=search_card',
'https://www.mastersportal.com/studies/268633/international-education-and-development.html?ref=search_card',
'https://www.mastersportal.com/studies/362740/dual-degree-in-curriculum-and-instruction-elementary-education-concentration-and-literacy-education.html?ref=search_card',
'https://www.mastersportal.com/studies/376717/high-school-education.html?ref=search_card',
'https://www.mastersportal.com/studies/334484/critical-pedagogy.html?ref=search_card',
'https://www.mastersportal.com/studies/749/educational-studies.html?ref=search_card',
'https://www.mastersportal.com/studies/359922/learning-and-developmental-sciences-educational-psychology.html?ref=search_card',
'https://www.mastersportal.com/studies/232237/smart-edtech-co-creativity-and-digital-tools-for-educational-innovation.html?ref=search_card',
'https://www.mastersportal.com/studies/374606/international-education.html?ref=search_card',
'https://www.mastersportal.com/studies/225335/educational-sciences.html?ref=search_card',
'https://www.mastersportal.com/studies/320542/information-and-computer-education.html?ref=search_card',
'https://www.mastersportal.com/studies/232914/educational-sciences.html?ref=search_card',
'https://www.mastersportal.com/studies/232920/education.html?ref=search_card',
'https://www.mastersportal.com/studies/377829/design-leadership.html'
]
programs = []

# WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reply-button")))

masters_count = -1
for masters_link in links:
    masters_count += 1

    driver.get(masters_link)

    soup = BeautifulSoup(driver.page_source, "lxml")

    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "StudyTitle")))
        program_name = soup.find('h1', class_='StudyTitle').text
    except:
        program_name = 'na'
    try:
        university_name = soup.find('div', class_='OrganisationName').find('a', class_='TextLink Connector js-essential-info-organisation-link').text
    except:
        university_name = 'na'
    try:
        uni_rank = int((soup.find('span', class_='ValueAndType').find('span', class_='Value').text).replace("st", "").replace("nd", "").replace("th", "").replace("rd", ""))
    except:
        uni_rank = 'na'
    try:
        country = soup.findAll('a', class_='LocationItem TextLink Connector')[1].text
    except:
        country = 'na'
    try:
        city = soup.findAll('a', class_='LocationItem TextLink Connector')[0].text
    except:
        city = 'na'
    try:
        print(soup.find('div', class_='TuitionFeeContainer').find('span', class_='Title').text)
        price_year = int((soup.find('div', class_='TuitionFeeContainer').find('span', class_='Title').text).replace('Free', '0').replace(',', '').replace('.', ''))
    except:
        price_year = 'na'
    try:
        print(soup.find('li', class_='FactListSubListItem').find('span', class_='Duration').text)
        semesters = int((soup.find('li', class_='FactListSubListItem').find('span', class_='Duration').text).replace(' ', '').replace('&nbsp', '').replace('months', ''))
    except:
        semesters = 'na'
    try:
        deadline_end = soup.find('div', class_='FactItemInformation Deadline').find('time').text
    except:
        deadline_end = 'na'
    try:
        toefl = soup.find('div', class_='CardContents EnglishCardContents TOEFLCard js-CardTOEFL').find('div', class_='MainContent').find('div', class_='ScoreInformationContainer').find('div', class_='ScoreContainer').find('div', class_='Score').text
    except:
        toefl = 'na'
    try:
        disciplines = ""
        for link in soup.find_all('a', class_="TextOnly"):
            if "View" in link.text:
                pass
            else:
                disciplines += link.text + ","
    except:
        disciplines = "na"
    try:
        living_cost = soup.find("div", class_="CostsOfLiving").find("div", class_="FeeDetails").find("div", class_="Costs").find("span", class_="Amount")
        living = living_cost.text.replace(".", "").split("-")
        living_cost = (int(living[0]) + int(living[1])) / 2
    except:
        living_cost = "na"
    try:
        general_req = ""
        for link in soup.find('div', class_="OtherRequirementsContent").find('div'):
            for ul in link:
                for li in ul:
                    general_req += link.text + ", "
        general_req = general_req.replace('General requirements,', '')
    except:
        general_req = "na"

    disciplines = disciplines[:-2]

    final = {
        'Link': links[masters_count],
        'Program': program_name,
        'University Name': university_name,
        'University Rank': uni_rank,
        'Country': country,
        'City': city,
        'Price per Year': price_year,
        'Semesters (months)': semesters,
        'Deadline End Date': deadline_end,
        'TOEFL Requirement': toefl,
        'Disciplines': disciplines,
        'Living Cost Average': living_cost,
        'General Requirements': general_req.replace(' ,                      ,', '')
    }

    programs.append(final)
    print(final)


print(programs)
keys = programs[0].keys()

with open('masters_table.csv', 'w', newline='', encoding="utf-8") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(programs)