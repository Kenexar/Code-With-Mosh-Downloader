import os
import time
from pathlib import Path

import requests
from alive_progress import alive_bar
from bs4 import BeautifulSoup
from dotenv import dotenv_values, load_dotenv

load_dotenv()
header = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50',
    'cookie': f'{dotenv_values().get("AUTH_COOKIE")}'}


class LectureObj:
    download_link = ""
    path = ""

    lecture_id = ""
    course_id = ""

    def __init__(self, course_id, lecture_id):
        self.course_id = course_id
        self.lecture_id = lecture_id
        self.download_link = get_lecture_download_link(lecture_id, course_id)
        self.generate_path()

    def generate_path(self):
        response = requests.get(f"https://codewithmosh.com/courses/enrolled/{self.course_id}", headers=header)

        soup = BeautifulSoup(response.text, "html.parser")

        s1 = soup.select('.col-sm-12')

        for s3 in s1:
            for s4 in s3.select("li"):
                if s4.get("data-lecture-id") == self.lecture_id:
                    title = s3.find('div', class_='section-title').contents[2].getText().strip()

        s2 = soup.select_one('.course-sidebar')
        self.path = f"{s2.h2.text}/{title}/"

        print(self.path)

    def get_download_link(self):
        return self.download_link

    def get_path(self):
        return self.path


def get_course_lecture_ids(course_id: str) -> dict:
    return_list = {}
    response = requests.get(f"https://codewithmosh.com/courses/enrolled/{course_id}", headers=header)

    soup = BeautifulSoup(response.text, "html.parser")

    s2 = soup.select('.col-sm-12')

    for s1 in s2:
        id_list = []
        title = s1.find('div', class_='section-title').contents[2].getText().strip()
        for s3 in s1.select("li"):
            return_list[s3.get("data-lecture-id")] = title

    return return_list


def get_course_lecture_pure_ids(course_id: str) -> list:
    id_list = []
    response = requests.get(f"https://codewithmosh.com/courses/enrolled/{course_id}", headers=header)

    soup = BeautifulSoup(response.text, "html.parser")

    s2 = soup.select('.col-sm-12')

    for s1 in s2:
        for s3 in s1.select("li"):
            id_list.append(s3.get("data-lecture-id"))

    return id_list


def get_courses_ids() -> list:
    id_list = []

    response = requests.get("https://codewithmosh.com/courses/enrolled/240431", headers=header)

    soup = BeautifulSoup(response.text, "html.parser")

    soup_select = soup.select(".course-listing")
    for rq in soup_select:
        id_list.append(rq.get("data-course-id"))

    return id_list


def get_lecture_download_link(lecture_id: str, course_id: str) -> str:
    response = requests.get(f"https://codewithmosh.com/courses/{course_id}/lectures/{lecture_id}", headers=header)

    soup = BeautifulSoup(response.text, "html.parser")

    soup_select = soup.select(".download")
    try:
        return soup_select[0].get("href")
    except IndexError:
        return ""


def download_video(link: str, path=""):
    start = time.time()

    if link == "":
        return

    ensure_dir(path)

    r = requests.get(link, stream=True)

    file_name = r.headers['x-file-name']

    if Path(path + file_name).is_file():
        return

    print(path + file_name)

    with alive_bar(title=f'Downloading "{file_name}" ', bar='classic', monitor=False, elapsed=False) as bar:
        with open(path + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    bar()
                    f.flush()
    end = time.time()
    print(f"Done! File: {path + file_name} \nTime: {end - start:.2f} sec")


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def main():
    for c_id in get_courses_ids():
        for l_id in get_course_lecture_pure_ids(str(c_id)):
            lct_obj = LectureObj(str(c_id), str(l_id))
            download_video(lct_obj.download_link, "output/" + lct_obj.path)


start = time.time()

if __name__ == "__main__":
    main()

end = time.time()
print(f'Time: {end - start:.2f} sec')
