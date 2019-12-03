import os

from flask import Flask
from flask import render_template
from flask import request

from amadeus import Client, ResponseError
from amadeus import Location

from flask_sqlalchemy import SQLAlchemy

#import helper_libs


"""
DATABASE SETUP

1. Database Schema -->
    - User Login - Logout Scenario
    - Storage of User Profile Data
    - Storage of user flight data
    - Storage of user hotel booking data.

2. Testing the database -->
    - TO BE DONE : Check for persistence, etc.
    - TO BE DONE : Check if the entire scene works.
    - TO BE DONE : Check user booking data.

"""

def create_app(test_config=None):

    #Create and configure this application

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY ='dev',
        DATABASE= os.path.join(app.instance_path, 'traveleasy')
    )

    if test_config is None:
        #Load the instance config, if it still exists, when not Testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        #Load the test_config if passed in
        app.config.from_mapping(test_config)

    #Let's now ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Get the access credentials from Prajwal
    amadeus = Client(
        client_id = 'REPLACE THIS',
        client_secret = 'REPLACE THIS TOO'
    )

    @app.route('/hello')
    def hello():
        return 'Hello World!'
        """

                `
                project_directory = os.path.dirname(os.path.abspath(__file__))
                database_file="sqlite:///{}".format(os.path.join(project_directory),"traveldatabase.db")

                app = Flask(__name__)
                app.config[]"SQLALCHEMY_DATABASE_URI"] = database_file

                db=SQLAlchemy(app)

        """
        """

        FOR AMADEUS -->


        ACCESS CREDENTIALS : PLEASE INSERT

        """


        """
        HOME PAGE -->


        BEAUTIFUL LANDING PAGE WITH ONE BIG CALL TO ACTION


        Let's get this party started
        _______________________________________________________


        """
    @app.route("/",methods =('GET','POST'))
    def home():
        if request.method == 'POST':
            origin_location_code = request.form['origin_location_code']
            db = get_db()
            error = None

            if not origin_location_code:
                error = 'Location is required to show code'


            if error is None:
                flight_inspiration(origin_location_code)

            flash(error)

        return render_template("home.html")

    """

    STEP BY STEP GUIDE  -- 1

    after form is submitted

    SEARCH AIRPORTS -->
        1. CLOSEST TO YOUR LOCATION.


    """
    @app.route("/search_departure_airports/<str>origin_id/")
    #Add previous location to the code
    def search_dep_airports():
        if request.method == 'POST':
            origin_location_code = request.form['origin_location_code']
            depart_location_code = request.form['depart_location_code']

            db = get_db()
            error = None

            if not origin_location_code:
                error = 'Origin location code is required'
            elif not depart_location_code:
                error = 'Departure location code is required'

            if error is None:
                flight_inspiration(origin_location_code)

            flash(error)

        return render_template("departure.html")

    """

    STEP BY STEP GUIDE  -- 2

    after the form is submitted

    SEARCH AIRPORTS THAT ARE CLOSEST TO YOUR DESTINATION -->
        1. CLOSEST TO YOUR LOCATION.


    """
    @app.route("/search_arrival_airports/<str>origin_id/<str>arrival_id")
    #Add the next location to the code
    def search_arr_airports():

        response = amadeus.reference_data.locations.get(
            keyword='LON',
            subType=Location.ANY
        )

        print(response.body) #=> The RAW response as a string is being printed
        print(response.result) #=> JSON being parsed
        print(response.data) #=> List of locations, extracted from JSON.


    """

    STEP BY STEP GUIDE  -- 3

    find the UI to be able to display this, don't think it will be easy

    SEARCH AIRPORTS -->
        1. CHEAPEST FLIGHT DATE

    """
    @app.route("/search_arrival_airports/<str>origin_id/<str>arrival_id/cheapest_flight_date")
    def cheapest_flight_date():
        pass

    @app.route("/search_arrival_airports/<str>origin_id/<str>arrival_id/cheapest_flight_date/cheapest_individual flight")
    def cheapest_individual_flight():
        pass

    @app.route("/search_arrival_airports/<str>origin_id/<str>arrival_id/cheapest_flight_date/cheapest_individual flight/booking_confirmation")
    def booking_confirmation():
        pass

    @app.route("/search_arrival_airports/<str>origin_id/<str>arrival_id/cheapest_flight_date/cheapest_individual flight/booking_confirmation/payment")
    def payment():
        pass

    @app.route("/search_arrival_airports/<str>origin_id/<str>arrival_id/cheapest_flight_date/cheapest_individual flight/booking_confirmation/payment/authenticate")
    def authenticate():
        pass

    @app.route("/check_bookings")
    def check_bookings():
        pass

    @app.route("/book_hotels")
    def book_hotels():
        pass


    """
    MAKE SURE EVERYTHING AFTER THIS SECTION REMAINS AT THE END OF THE FILE.



    """


    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
