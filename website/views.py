from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json


views = Blueprint('views', __name__)


from flask import Blueprint, render_template, request, flash, jsonify
from .models import Drink
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])

def home():
    return render_template("home.html")

@views.route('/menu')
def menu():
    nonalcohol=["Coca Cola","Coca Cola Zero","Sprite","Fanta","Schweppes Bitter","Schweppes Tonic","Guarana","Knjaz Miloš"]
    prices_nonalcohol=[100,100,100,100,120,120,120,80]
    nonalcohol_negazirano=["Narandža","Borovnica","Jagoda","Cedevita","Ceđena limunada","Rosa"]
    prices_nonalcohol_negazirano=[110,110,110,100,90,80]
    kafe=['Espresso','Caffe Macchiato','Caffe Late','Ice Latte','Freddo Espresso','Freddo Cappuccino','Nes Kafa','Domaća kafa']
    prices_kafe=[100,100,110,120,130,130,120,80]
    piva=['Heineken','Birra Moretti','Laško','Zaječarsko','Točeno pivo 0,25l','Točeno pivo 0,50l']
    prices_piva=[180,180,180,150,130,180]
    spirits=['Vodka','Džin','Tekila','Viski','Vinjak']
    prices_spirits=[100,100,160,170,120]
    data_nonalcohol=zip(nonalcohol,prices_nonalcohol)
    data_negazirano=zip(nonalcohol_negazirano,prices_nonalcohol_negazirano)
    data_kafe=zip(kafe,prices_kafe)
    data_piva=zip(piva,prices_piva)
    data_spirits=zip(spirits,prices_spirits)
    data_kokteli=zip(['Margarita','Blue Lagoon','Tequila Sunrise','Tequila bum','Screwdriver'],[250,220,220,200,200])
    return render_template("menu.html",
                        data_nonalcohol=data_nonalcohol,
                        data_kafe=data_kafe,
                        data_piva=data_piva,
                        data_spirits=data_spirits,
                        data_kokteli=data_kokteli,
                        data_negazirano=data_negazirano,
                        )


@views.route('/contact-us')
def contact():
    names=['Nemanja','Belma']
    numbers=['collapseOne','collapseTwo']
    
    return render_template("contact-us.html",names=names,numbers=numbers)

