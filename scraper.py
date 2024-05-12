import requests
from bs4 import BeautifulSoup
# import sysconfig
# import sys
# purelib is a dir that contains modules written with python only
# contains binaries that arent necessarily written in python.. .dll, .so
# print(sysconfig.get_path("purelib"))
# print(sysconfig.get_path("platlib"))  # Linux Dists such as Fedora and Redhat put the contains in separate directories 

# URL = sys.argv[1]
URL = "https://realpython.github.io/fake-jobs/"
job_data=[]
try:
    page = requests.get(URL)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content,"html.parser")
        results = soup.find(id="ResultsContainer")
        # filter_python  = results.find_all("h2",string="python")
        python_jobs = results.find_all(string=lambda text: "python" in text.lower())
        # job_elements = results.find_all("div", class_="card-content")
     
        python_job_elements = [h2_element.parent.parent.parent.parent for h2_element in python_jobs]
        for python_job in python_job_elements:
            links = python_job.find_all("a")[1]['href']
        for link in links:
            print(link)
            # print(python_job.find('h2',class_="title").text.strip())
            # print(python_job.find('h3',class_='company').text.strip())
            # print(python_job.find('p',class_='location').text.strip())
        #     title_element = python_job.find("h2", class_="title")
        #     company_element = python_job.find("h3", class_="company")
        #     location_element = python_job.find("p", class_="location")
        #     curr = {
        #         "title":title_element.text.strip(),
        #         "company":company_element.text.strip(),
        #         "location":location_element.text.strip(),
        #         }
        #     job_data.append(curr)
        #     print()
        # print(page.content)
        # print(job_data)
    else:
        print("Failed to retrieve the page: Status code", page.status_code)
except requests.exceptions.RequestException as e:
    print("Error during requests to {0} : {1}".format(URL, str(e)))
    