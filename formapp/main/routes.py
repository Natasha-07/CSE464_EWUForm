from flask import Blueprint, flash, redirect, render_template, request, url_for
from formapp.extensions import mongo
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)


@main.route('/')
def index():
    form_collection = mongo.db.form_db
    form = form_collection.find()
    return render_template('index.html', form=form)


@main.route('/form', methods=['POST'])
def form():
    form_collection = mongo.db.form_db
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    gender = request.form.get('gender')
    dateOfBirth = request.form.get('dateOfBirth')
    country = request.form.get('country')
    religion = request.form.get('religion')
    nationality = request.form.get('nationality')
    street1 = request.form.get('street1')
    street2 = request.form.get('street2')
    city = request.form.get('city')
    police_station = request.form.get('police_station')
    postal_code = request.form.get('postal_code')
    phone = request.form.get('phone')
    email = request.form.get('email')
    program = request.form.get('program')
    semester = request.form.get('semester')
    dpt_name = request.form.get('dpt_name')
    form_collection.insert_one({
        'first_name': first_name,
        'last_name': last_name,
        'gender': gender,
        'dateOfBirth': dateOfBirth,
        'country': country,
        'religion': religion,
        'nationality': nationality,
        'street1': street1,
        'street2': street2,
        'city': city,
        'police_station': police_station,
        'postal_code': postal_code,
        'phone': phone,
        'email': email,
        'program': program,
        'semester': semester,
        'dpt_name': dpt_name,
    })
    return redirect(url_for('main.index'))

@main.route('/all-forms')
def all_form():
    form_collection = mongo.db.form_db
    forms = form_collection.find({})
    return render_template('forms.html', forms=forms)
