#main.property

import webapp2
import jinja2
import os
from models import memeInfo
from google.appengine.api import urlfetch
import json


# This initalizes the jinja2 enviromemnt
#same for every app built
#jinja2.enviromemnt is a constructor
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
        api_url = 'https://api.imgflip.com/get_memes'
        imgflip_response = urlfetch.fetch(api_url).content
        imgflip_response_json = json.loads(imgflip_response)
        # print(imgflip_response_json['data']['memes'])
        meme_templates = []
        for meme_template in imgflip_response_json['data']['memes']:
            meme_templates.append(meme_template['url'])
        memeDict ={
            'imgs': meme_templates
        }
        HTML_template = jinja_env.get_template('HTML.html')
        self.response.write(HTML_template.render(memeDict))


class ResultPage(webapp2.RequestHandler):
    def post(self):
        top_line = self.request.get('top-line')
        bottom_line = self.request.get('bottom-line')
        memeURL = self.request.get('template')
        data_dict = {
            "top": top_line,
            'bottom': bottom_line,
            'url': memeURL
        }
        result_template = jinja_env.get_template('result.html')
        self.response.write(result_template.render(data_dict))
        meme = memeInfo(memeTextTop = top_line, memeUrl = memeURL, memeTextBottom = bottom_line)
        meme.put()

class allMemesPage(webapp2.RequestHandler):
    def get(self):
        allMemes = memeInfo.query().fetch()
        dataMemes = {
            'storedMemes' : allMemes,
        }
        allMemesTemplate = jinja_env.get_template('allMemes.html')
        self.response.write(allMemesTemplate.render(dataMemes))




# The app configuration section
app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/result', ResultPage),
        ('/allMemes', allMemesPage)
    ],
    debug=True
)
