from flask import *
from db_islemleri import *
import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['POST', 'GET'])
def index():
    birimler = birimistele()
    if request.method == 'POST':
        bilgiler = request.form.to_dict()
        servis_id = int(bilgiler['servis_id'])
        birim_id = int(bilgiler['birim_id'])
        servis = session.query(Talep).filter_by(talep_id=servis_id,talep_birimi=birim_id).first()
        servis = servis if servis != None else False
        return render_template("index.html",servis=servis,birimler=birimler)
    else:
        return render_template("index.html",birimler=birimler,servis=False)


if __name__ == '__main__':
    app.run(debug=True)
