"""
This is currency exchange module that contains the Currency Exchange class which calls ExchangeRate-APIs
"""

import requests
from app.logger import log
from app import config

class Currency_Exchange():
    """
    This class is used to call ExchangeRate-APIs
    """

    def __init__(self):
        self.api_key = config.API_KEY
        self.query_response_standard = {}
        self.query_response_pair_conversion = "Please check if target currency code and Amount was entered "
        self.query_response_pair_conversion_rate = "Please check if target currency code was entered"
        self.query_response_enriched_rate = "Please check if target currency code was entered"
        self.query_response_enriched = "Please check if target currency code was entered"
        self.query_response_history = {} 
        # Call Supported Codes ExchangeRate-API endpoint.
        self.supported_codes = self.__call_api('https://v6.exchangerate-api.com/v6/'+self.api_key+'/codes')



    def execute_search(self, currency_code=str, target_currency_code=None, amount=None, year=None, month=None, day=None):
        '''
        This function takes in currency code,target currency code, year, month and day as user input and retrieves 
        information from apis accordingly
        '''
        log('Currency Exchange search : ')

        
        # Call Standard ExchangeRate-API endpoint    
        query_response_standard = self.__call_api('https://v6.exchangerate-api.com/v6/'+self.api_key+'/latest/'+currency_code)
        self.query_response_standard = query_response_standard.get('conversion_rates')

        if target_currency_code is not None:
            # Call Pair ExchangeRate-API endpoint.
            query_response_pair_conversion_rate = self.__call_api('https://v6.exchangerate-api.com/v6/'+self.api_key+'/pair/'+currency_code+'/'+target_currency_code)
            self.query_response_pair_conversion_rate = query_response_pair_conversion_rate.get('conversion_rate')

            if amount is not None:
                query_response_pair_conversion = self.__call_api('https://v6.exchangerate-api.com/v6/'+self.api_key+'/pair/'+currency_code+'/'+target_currency_code+'/'+amount)
                self.query_response_pair_conversion = query_response_pair_conversion.get('conversion_result')

            # Call Enriched ExchangeRate-API endpoint
            query_response_enriched = self.__call_api('https://v6.exchangerate-api.com/v6/'+self.api_key+'/enriched/'+currency_code+'/'+target_currency_code)
            self.query_response_enriched_rate = query_response_enriched.get('conversion_rate')
            self.query_response_enriched = query_response_enriched.get("target_data")
        
        if year and month and day is not None:
            # Call Historical Data ExchangeRate-API endpoint
            query_response_history = self.__call_api('https://v6.exchangerate-api.com/v6/'+self.api_key+'/history/'+currency_code+'/'+year+'/'+month+'/'+day)
            self.query_response_history = query_response_history.get('conversion_rates')

        return {'response' : 'Success'}

    def __call_api(self, url) :
        """
        This function is used to call get requests for different urls
        url : str -> link to pass get requests.
        """
        headers = {}
        headers['Content-Type'] = 'application/json'
        response = requests.get(url, headers= headers)
        if response.json()['result']=="success" and response.status_code == 200:
            return response.json()
        else:
            return {"error" : "Invalid argument. Please try again."}

    