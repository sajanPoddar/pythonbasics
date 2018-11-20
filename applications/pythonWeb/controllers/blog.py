# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from blog.py")

@auth.requires_membership('blog_poster')
def post():
    form = SQLFORM(db.blog).process()
    return locals()

@auth.requires_login()
def view():
    rows = db(db.blog).select(orderby=~db.blog.id)
    return locals()

def display_forms():
    form = SQLFORM(db.blog)
    if form.process().accepted:
        session.flash = 'form accepted'
        redirect(URL('thanks'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'Please fill out the form'
    return locals()

def thanks():
    return locals()

def update():
    record = db.blog(request.args(0)) or redirect(URL('post'))
    form = SQLFORM(db.blog, record)
    if form.process().accepted:
        response.flash = T("Record update")
    else:
        response.flash = T("Please Complete the form")
    return locals()
