from time import time
from datetime import datetime
from tweepy import API, OAuthHandler


class Tweets_Search(object):
    def __init__(self):
        _consumer_key = 'LsjVMAnVZ8GBriWyVTlek7Zfe'
        _consumer_secret = 'TNpDElapTz36hYILYPGaXn7vb9HTW4OilzOzknOT9Dv2DBY5jG'
        _access_token = '1260273957799952385-3jmfl9H4im09vpu7LXKcE7yGUxpTiV'
        _access_secret = 'ZnZJPdE1xeBPn3H9IPKlIrZSl6C5wlqFLHSvRZY4UMGjK'
        _authentication = OAuthHandler(_consumer_key, _consumer_secret)
        _authentication.set_access_token(_access_token, _access_secret)
        self._api = API(_authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_errors=True)

    def check_authentication(self):
        try:
            self._api.verify_credentials()
        except Exception as err:
            print("Error creating API")
            raise err
        print("API created")

    @staticmethod
    def datetime_from_utc_to_local(utc_datetime):  # UTC (+0000) to local time
        now_timestamp = time()
        offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
        return utc_datetime + offset

    def seacher(self, query, language, result_numbers):
        _result_list = []
        for tweet in self._api.search(q=query, lang=language, count=result_numbers, result_type='recent'):
            tweet_created_at = self.datetime_from_utc_to_local(tweet.created_at)
            _result_list.append(f"[{tweet_created_at}] {tweet.text}")
        return _result_list


if __name__ == '__main__':
    query = 'Petrobrás'
    language = 'pt-br'
    result_numbers = 10

    results_list = Tweets_Search().seacher(query, language, result_numbers)
    for result in results_list:
        print(result)
