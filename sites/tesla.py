from scraper_peviitor import Scraper, Rules, loadingData, ScraperSelenium

import time
import uuid
import os

#Folosim ScraperSelenium deoarece joburile sunt incarcate prin AJAX
scraper = ScraperSelenium("https://www.tesla.com/ro_RO/careers/search/?site=RO")
scraper.get()
time.sleep(5)

#Luam codul HTML
dom = scraper.getDom()

#Setam dom-ul intr-un obiect Scraper
scraper = Scraper()
scraper.soup = dom
rules = Rules(scraper)

#Luam toate joburile
jobs = rules.getTag("tbody", {"class": "tds-table-body"}).find_all("tr")

finaljobs = list()

#Pentru fiecare job luam titlul, linkul, compania, tara si orasul
for job in jobs:
    id = uuid.uuid4()
    job_title = job.find("a").text
    job_link = "https://www.tesla.com" + job.find("a").get("href")
    company = "Tesla"
    country = "Romania"
    city = job.find_all("td")[2].text.split(",")[0].strip()

    print(job_title + " -> " + city)

    finaljobs.append({
        "id": str(id),
        "job_title": job_title,
        "job_link": job_link,
        "company": company,
        "country": country,
        "city": city
    })

#Afisam numarul total de joburi
print("Total jobs: " + str(len(finaljobs)))

#Incarcam joburile in baza de date
loadingData(finaljobs, "182b157-bb68-e3c5-5146-5f27dcd7a4c8", "Tesla")