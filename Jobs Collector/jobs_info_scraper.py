import json
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_jobs():
    MAIN_URL = "https://www.ejobs.ro"
    columns = ["job_title", "company_name", "link_to_job"]
    jobs = []

    main_page = requests.get(MAIN_URL)
    soup = BeautifulSoup(main_page.content, features="html.parser")

    if not os.path.isfile("jobs.json"):
        jobs_container = soup.find(id="home-jobs").find_all("li", class_="jobitem gridview")
        for item in jobs_container:
            job_box = item.find(class_="job-box").find(class_="jobitem-body").find_all(["h2", "h3"])
            details = [job_box[0].text, job_box[1].text,
                       valid_link(job_box[0].find("a", href=True, class_="title dataLayerItemLink")["href"], MAIN_URL)]
            jobs_dict = {
                col: data for col, data in zip(columns, details)
            }
            jobs.append(jobs_dict)

        for job in tqdm(jobs, total=len(jobs), desc="Collecting jobs..."):
            soup = BeautifulSoup(requests.get(job["link_to_job"]).content, features="html.parser")
            job_content_image = soup.find(class_="jobad-wrapper jobad--customised clearfix")
            if job_content_image is not None:  # If the description of the job is an image:
                job_content = job_content_image.find(id="customJobImageContainer").find("img", alt=True)
                job["description"] = job_content["alt"]
            else:  # The description of the job is actual text in page
                job_contents_text = soup.find(class_="jobad-wrapper jobad--normal clearfix") \
                    .find(class_="jobad-panel active animated").find(class_="row"). \
                    find("section").find_all(class_="jobad-content-block")
                for descr in job_contents_text:
                    job["description"] = "".join(descr.text)

        with open("jobs.json", mode="w") as json_file:
            json.dump(jobs, json_file, indent=2)
        print(f"Done. Scraper has collected {len(jobs)} jobs.\n")
    else:
        print("Updating...")


def get_matching_jobs():
    if os.path.isfile("jobs.json"):
        with open("jobs.json", "r") as json_file:
            jobs = json.load(json_file)

        while True:
            users_skills = input("Please type your skills (separated by comma): ").split(",")
            jobs_match = list(filter(lambda job: any(skill in job["description"] for skill in users_skills), jobs))
            for job in jobs_match:
                print(f"Job Title: {job['job_title']}")
                print(f"Company: {job['company_name']}")
                print(f"Link: {job['link_to_job']}")
                print("----------------------------------------")
            another_search = input("Do you want to search jobs that match other skills? (Y/N y/n) -- ")
            if another_search in ["n", "N"]:
                break
    else:
        print("Jobs have not been collected yet. Please enter the 1st option.\n")


def valid_link(link, MAIN_URL):
    if not link.startswith(MAIN_URL):
        return MAIN_URL + link
    return link

