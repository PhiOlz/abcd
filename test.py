import webapp2

from google.appengine.ext import db

class Comment(db.Model):
    content = db.StringProperty(multiline=True)
    comment = db.StringProperty(multiline=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><h1>Project Parallel</h1>')
        self.query = Comment.all()
        self.response.write("""Post & Comment Here:
        <form method="post">
        <input type="textarea" name="post"></input>
        <input type="textarea" name="posts"></input>
        <input type="submit"></input></form>
        </br>Delete Here:
        <form method="post">
        <select name="del">
        """)
        for self.comment in self.query:
            self.response.write('<option>%s</option>' % self.comment.content)
        self.response.write("""<input type="submit"></input></br>""")
        self.response.write('Search Here: ')
        self.response.write('<table><tr>')
        for self.comment in self.query:
            self.response.write('<td><option>%s' % self.comment.content)
            self.response.write('(%s)</option></td>' % self.comment.comment)
        self.response.write('</tr></table>')
        for self.comment in self.query:
            self.response.write('<p1>%s</p1>' % self.comment.content)
            self.response.write('<p2>(%s)</P2></br>' % self.comment.comment)
        self.response.write('</body></html>')

    def post(self):
        i=1
        self.comment = Comment(id=i,content=self.request.get('post'),comment=self.request.get('posts'))
        self.comment.put()
        i=i+1
        self.redirect('/')

    #def delete(self):
        #self.comment = Comment.filter("content =", self.request.get('del'))
        #self.comment.content = ' '
        #self.comment.comment = ' '
        #self.comment.key.delete()
        #dele = self.request.get('del')
        #Comment(content = dele).delete()
        #del.key.delete()
        #po = Comment.comment(self.request.get('del'))
        #abc = self.request.get('del').get()
        #abc.comment = "This comment was deleted"
        #abc.content = "This post was deleted"
        #abc.put()
        #self.redirect('/')

        
class DeletionHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.get('del') in Comment(content):
            com = Comment.get_by_id(int(self.request.get("id")))
            com.delete()
            self.redirect("/")
        else:
            self.redirect("/")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
