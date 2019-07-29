import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb


class CssiUser(ndb.Model):
    first_name = ndb.StringProperty()
    email = ndb.StringProperty()
    age = ndb.IntegerProperty()



class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_address = user.nickname()
            logout_url = users.create_logout_url('/')
            logout_button = '<a href="%s"> sign in </a>' % logout_url
            self.response.write('you are logged in ' + email_address + '!<br>' + logout_url)

            existing_user = CssiUser.query().filter(CssiUser.email == email_address).get()
            if existing_user:
                pass
            else:
                self.response.write('''Please register!
                <form method='post' action='/'>
                    <input type='text' name='first_name'>
                    <input type='text' name='age'>
                    <input type='submit'>
                    </form>
                    <br>
                    %s

                ''' % logout_button)
        else:
            login_url = users.create_login_url('/')
            login_button = '<a href="%s"> sign in </a>' % login_url

            self.response.write('please log in<br>' + login_button)
    def post(self):
        user = users.get_current_user()
        if user:
            cssi_user = CssiUser(
                first_name=self.request.get('first_name'),
                age= int(self.request.get('age')),
                email = user.nickname()
            )
            cssi_user.put()
            self.response.write('Thanks for registering')





#initilization cxode
app = webapp2.WSGIApplication(
    [('/',MainHandler)],
    debug=True


)
