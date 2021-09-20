from flask import Flask, request, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>Document</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous"/><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script></head><body><nav class="navbar navbar-expand-lg navbar-light bg-light"><div class="container-fluid"><a class="navbar-brand" href="#">Navbar</a><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav me-auto mb-2 mb-lg-0"><li class="nav-item"><a class="nav-link" aria-current="page" href="#">Mail</a></li></ul></div></div></nav><div class="container"><div class="col-lg-4 block-border"><form action="/" method="post" enctype="multipart/form-data"><div class="form-group"><label class="control-label"> To : </label><input type="text" name="email" class="form-control" /></div><div class="form-group"><label class="control-label"> CC : </label><input type="text" name="cc" class="form-control" /></div><div class="form-group"><label class="control-label"> BCC : </label><input type="text" name="bcc" class="form-control" /></div><div class="form-group"><label class="control-label"> Subject : </label><input type="text" name="subject" class="form-control" /></div><div class="form-group"><label class="control-label"> Message : </label><textarea name="body" class="form-control" rows="5"></textarea></div><div class="form-group"><label class="control-label"> Html Body : </label><textarea name="html" class="form-control" rows="5"></textarea></div><div class="form-group"><label class="control-label"> File : </label><input type="file" name="file" class="form-control" /></div><div class="form-group"><button type="submit" class="btn btn-success">Send Mail With File</button></div></form></div></div></body></html>'
        # return '<form action="/" method="POST" enctype="multipart/form-data"><label>To :</label><input name="email"><label>CC :</label><input type="text" name="cc"><label>BCC :</label><input type="text" name="bcc"><label>Subject :</label><input type="text" name="subject"><label>Body :</label><textarea name="body"></textarea><label>HTML Page :</label><textarea name="html"></textarea><input type="file" name="file"><input type="submit"></form>'
        
    
    email = request.form['email']
    cc = request.form['cc']
    bcc = request.form['bcc']
    
    msg = Message(request.form['subject'],sender=('Pune Management Association','pmacoe.it@gmail.com'),reply_to='pmacoe.it@gmail.com', recipients=email.split(','))
    msg.sender == "Pune Management Association <pmacoe.it@gmail.com>"
    msg.cc = cc.split(',')
    msg.bcc = bcc.split(',')
    msg.body = request.form['body']
    msg.html = request.form['html']
    file = request.files['file']
    msg.attach(file.filename,"application/pdf",file.read())  
    print(file.filename)
    mail.send(msg)

    return '<h1>Mail sent to {}</h1>'.format(email)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    # app.run(debug=True)