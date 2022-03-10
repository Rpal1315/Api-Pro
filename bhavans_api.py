import json

from flask import Flask, jsonify
from flask_restful import Api, Resource
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import datetime
import asyncio

app = Flask(__name__)
api = Api(app)
source = requests.get('https://bhavansgkvidyamandir.edu.in/notice/').text
soup = BeautifulSoup(source, 'lxml')
notice_head = soup.find_all('a')
notice_head_text = []
post_links = []
for i in notice_head:
    if i.text == 'About Us' or i.text == 'History' or i.text == 'Our Mission' or i.text == 'Anthem and Prayer' or i.text == 'Rules and Regulations' or i.text == 'Primary' or i.text == 'Secondary' or i.text == 'School Uniform' or i.text == 'Primary' or i.text == 'Secondary' or i.text == 'School Timings' or i.text == 'Primary' or i.text == 'Secondary' or i.text == 'Holiday List' or i.text == 'Primary' or i.text == 'Secondary' or i.text == 'Exam Format' or i.text == 'Primary' or i.text == 'Secondary' or i.text == 'Staff' or i.text == 'Primary' or i.text == 'Secondary' or i.text == 'Mandatory Public Disclosure' or i.text == 'Infrastructure' or i.text == 'Classrooms' or i.text == 'AV Room & Auditorium' or i.text == 'Activity Rooms' or i.text == 'Canteen' or i.text == 'Admission & TC' or i.text == 'Procedure' or i.text == 'Primary Section' or i.text == 'Secondary Section' or i.text == 'TC Verification' or i.text == 'TC Verification-2020' or i.text == 'Gallery' or i.text == 'Primary' or i.text == 'Secondary' or i.text == 'Secondary Activities' or i.text == '\n\n' or i.text == '' or i.text == '' or i.text == '' or i.text == 'Home' or i.text == 'Management Committee' or i.text == 'School Information' or i.text == 'Library' or i.text == 'Laboratories' or i.text == 'Games & Sports' or i.text == 'Art Room' or i.text == 'Contact us' or i.text == 'Home':
        pass
    else:
        notice_head_raw_text = i.text

        notice_head_text.append(notice_head_raw_text)
        post_links.append(i.get('href'))
        notice_full = dict(zip(notice_head_text, post_links))

output = [{
    'date': datetime.datetime.now().strftime("%d-%m-%Y"),
    'time': datetime.datetime.now().strftime("%H:%M:%S"),
    'notice_title': notice_head_text,
    'notice_links': post_links,
    'notice_dict': notice_full
}]
json.dump(output, open('notice.json', 'w'))
file = open('notice.json', 'r')
file_data = json.load(file)


class Notice(Resource):
    def get(self):
        return file_data, 200


api.add_resource(Notice, '/')

if "__main__" == __name__:
    app.run(debug=True)
