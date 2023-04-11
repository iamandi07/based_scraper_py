from scraper_peviitor import Scraper, Rules, loadingData
import uuid
import time
import os

#Cream o instanta a clasei Scraper
url = "https://www.selgros.ro/posturi-disponibile?p=1"
scraper = Scraper(url)
rules = Rules(scraper)

#Obtinem numarul total de pagini
numberPages = int(rules.getTag("a", {"class": "last"}).find_all("span")[1].text)

finaljobs = list()

#Iteram prin fiecare pagina
for page in range(1, numberPages + 1):
    #Setam url-ul paginii curente
    url = "https://www.selgros.ro/posturi-disponibile?p=" + str(page)
    scraper.url = url

    #Luam toate joburile de pe pagina curenta
    jobs = rules.getTags("div", {"class": "text-content"})
    
    #Iteram prin fiecare job
    for job in jobs:
        id = uuid.uuid4()
        job_title = job.find("div", {"class":"title"}).text
        job_link = job.find("a")["href"]
        company = "Selgros"
        country = "Romania"
        city = job.find("div", {"class":"type-location"}).text.split(",")[1]
        print(job_title + " -> " + city)

        finaljobs.append({
            "id": str(id),
            "job_title": job_title,
            "job_link": job_link,
            "company": company,
            "country": country,
            "city": city
        })

    time.sleep(3)

#Afisam numarul total de joburi
print(len(finaljobs))

#Incarcam datele in baza de date
loadingData(finaljobs, "182b157-bb68-e3c5-5146-5f27dcd7a4c8", "Selgros")