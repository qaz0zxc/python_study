import web

urls = ('/hello','Index')

app = web.application(urls, globals())
render = web.template.render('templates/',base='layout')
class Index:
    def GET(self):
        #form = web.input(greet="hello",name="Nobody")
        #greeting = "%s %s " % (form.greet, form.name)
        #return render.index(greeting)
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s , %s" % (form.greet, form.name)
        return render.index(greeting = greeting)


if __name__ == "__main__":
    app.run()
