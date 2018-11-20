# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from contacts.py")

def data():
    rows = db(db.contacts).select()
    return locals()

def add():
    form = SQLFORM(db.contacts).process()
    return locals()

def view():
    if request.args(0) is None:
        rows = db(db.contacts).select(orderby=db.contacts.last_name | db.contacts.first_name)
    else:
        letter = request.args(0)
        rows = db(db.contacts.last_name.startswith(letter)).select(orderby=db.contacts.last_name | db.contacts.first_name)
    return locals()

def update():
    record = db.contacts(request.args(0)) or redirect(URL('view'))
    form = SQLFORM(db.contacts, record)
    if form.process().accepted:
        response.flash = T("Record update")
    else:
        response.flash = T("Please Complete the form")
    return locals()
