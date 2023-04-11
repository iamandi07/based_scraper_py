from scraper_peviitor import Scraper, Rules, loadingData
import uuid
import os

#Cream o instanta a clasei Scraper
scraper = Scraper("https://erstegroup-careers.com/bcr/search/?createNewAlert=false&q=&locations")
rules = Rules(scraper)

#Cautam elementele care contin joburile
elements = rules.getTags("tr", {"class" : "data-row"})

finalJobs = list()

#Iteram prin elementele gasite si extragem informatiile necesare
for element in elements:
    id = uuid.uuid4()
    job_title = element.find("a", {"class": "jobTitle-link"}).text
    job_link = "https://erstegroup-careers.com" + element.find("a", {"class": "jobTitle-link"})["href"]
    company = "BCR"
    country = "Romania"
    city = element.find("span", {"class": "jobShifttype"}).text

    finalJobs.append({
        "id": str(id),
        "job_title": job_title,
        "job_link": job_link,
        "company": company,
        "country": country,
        "city": city
    })

    print(job_title + " -> " + city)

#afișăm numărul total de joburi
print(len(finalJobs))

#Salvăm datele in baza de date
loadingData(finalJobs, "182b157-bb68-e3c5-5146-5f27dcd7a4c8", "BCR")