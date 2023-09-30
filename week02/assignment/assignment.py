"""
Course: CSE 251 
Lesson Week: 02
File: assignment.py 
Author: Jacob Graham

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here
class APICallThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        global call_count
        call_count += 1


# TODO Add any functions you need here


def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    # TODO Retrieve Top API urls
    top_api_result = {}
    top_api_thread = APICallThread(TOP_API_URL)
    top_api_thread.start()
    top_api_thread.join()
    top_api_urls = top_api_thread.run

    # TODO Retireve Details on film 6
    film_url = top_api_urls['films']
    film_6_thread = APICallThread(film_url + '6/')
    film_6_thread.start()
    film_6_thread.join()
    film_6_details = film_6_thread.result

    # TODO Display results
    log.write('Top API URLs:')
    for key, value in top_api_result.items():
      log.write(f'{key}: {value}')

    log.write('\nDetails of Film 6:')
    log.write(f'Title: {film_6_details["title"]}')
    log.write(f'Director: {film_6_details["director"]}')
    log.write(f'Release Date: {film_6_details["release_date"]}')
    log.write(f'Producer: {film_6_details["producer"]}')
    log.write('Characters:')
    for character in film_6_details["characters"]:
        log.write(f'- {character}')
    log.write('Planets:')
    for planet in film_6_details["planets"]:
        log.write(f'- {planet}')
    log.write('Starships:')
    for starship in film_6_details["starships"]:
        log.write(f'- {starship}')
        log.write('Vehicles:')
    for vehicle in film_6_details["vehicles"]:
        log.write(f'- {vehicle}')
        log.write('Species:')
    for species in film_6_details["species"]:
        log.write(f'- {species}')

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')
    

if __name__ == "__main__":
    main()
