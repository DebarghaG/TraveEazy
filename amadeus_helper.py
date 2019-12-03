import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from TravelWebsite.db import get_db

from amadeus import Client, ResponseError

amadeus = Client(
    client_id='REPLACE_BY_YOUR_API_KEY',
    client_secret='REPLACE_BY_YOUR_API_SECRET'
)

def flight_inspiration(origin_location_code):
    try :
        response = amadeus.shopping.flight_destinations.get(origin='{}'.format(origin_location_code))
        print(response)
        return(response)
    except ResponseError as error:
        print(error)
        return 0

def cheapest_date(origin_location_code, destination_location_code):
    try:
        response = amadeus.shopping.flight_dates.get(origin='{}'.format(origin_location_code), destination='{}'.format(destination_location_code))
        print(response)
        return(respose)
    except ResponseError as error:
        print(error)
        return 0

def lowest_fare_search(origin_location_code, destination_location_code, departure_date):
    try :
        response=amadeus.shopping.flight_offers.get(origin='{}'.format(origin_location_code, destination='{}'.format(destination_location_code), departureDate='{}'.format(departure_date)))
        print(respose)
        return(response)
    except ResponseError as error:
        print(error)
        return 0

def flight_choice_prediction(origin_location_code, destination_location_code, departureDate):
    try:
        response=amadeus.shopping.flight_offer.get(origin='{}'.format(origin_location_code, destination='{}'.format(destination_location_code), departureDate='{}'.format(departureDate))).result
        result= amadeus.shopping.flight_offers.prediction.post(result)
        print(result)
        return(result)

    except ResponseError as error:
        print(error)
        return 0

def checkin_status(airline_code):
    try:
        link = amadeus.reference_data.urls.checkin_links.get(airlineCode='{}'.format(airlineCode))
        print(link)
        return(link)

    except ResponseError as error:
        print(error)
        return 0

def airline_code_lookup(airline_code):
    try:
        code_lookup = amadeus.reference_data.airlines.get(airlines='{}'.format(airline_code))
        print(code_lookup)
        return code_lookup
    except ResponseError as error:
        print(error)
        return 0

def hotels_list(city_code):
    try:
        response = amadeus.hotel_offers.get(cityCode='{}'.format(city_code))
        print(response)
        return response
    except ResponseError as error:
        print(error)
        return 0

def hotel_by_name(hotel_name):
    try:
        response= amadeus.shopping.hotel_offers_by_hotel.get(hotelId = '{}'.format(hotel_name))
        print(response)
        return response
    except ResponseError as error:
        print(error)
        return 0

def hotel_sentiments(hotel_code):
    try:
        response = amadeus.e_reputation.hotel_sentiments.get(hotelIds = '{}'.format(hotel_code))
        print(response)
        return response
    except ResponseError as error:
        print(error)
        return 0
