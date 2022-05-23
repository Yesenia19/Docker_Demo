import web

render_app = web.template.render("templates/")

class Index():

    def GET(self):
        return render_app.index()