import webapp2

from google.appengine.ext import db

class Comment(db.Model):
    content = db.StringProperty(multiline=True)
    comment = db.StringProperty(multiline=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><h1>Project Parallel</h1>')
        self.query = Comment.all()
        for self.comment in self.query:
            self.response.write('<p1>%s</p1>' % self.comment.content)
            self.response.write('<p2>(%s)</P2></br>' % self.comment.comment)
        self.response.write("""Post & Comment Here:
        <form method="post">
        <input type="textarea" name="post"></input>
        <input type="textarea" name="posts"></input>
        <input type="submit"></input></form>
        <form method="post">
        <select name="del">
        """)
        for self.comment in self.query:
            self.response.write('<option>%s</option>' % self.comment.content)
        self.response.write("""<input type="submit"></input>""")
        self.response.write('</body></html>')

    def post(self):
        self.comment = Comment(content=self.request.get('post'),comment=self.request.get('posts'))
        self.comment.put()
        self.redirect('/')

    def delete(self):
        #self.comment = Comment.filter("content =", self.request.get('del'))
        #self.comment.content = ' '
        #self.comment.comment = ' '
        #self.comment.key.delete()
        dele = self.request.get('del')
        Comment(db.Comment.content == dele)
        self.redirect('/')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
