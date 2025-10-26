import os
from pathlib import Path
from datetime import datetime
from dateutil.relativedelta import relativedelta
from colorama import Fore, Back, Style, init
import sys

class Config:


    def __init__(self):
        pass


    def load(self):
        print('')
        print (f'{Fore.CYAN}config.load() ...{Style.RESET_ALL}')
        # (1) load dotenv first
        try:
            #env_path = Path.cwd() / '../../../.env'
            env_path = Path.cwd() / '.env'
            print(f'  loading env file: {env_path}')
            if env_path.exists() and env_path.is_file():
                print(f'  env file found')
                from dotenv import load_dotenv
                load_dotenv()
                #print(f'  ... {os.getenv('XATA_PASSWORD')}')
                print(f'  loaded .env file')
        except ImportError as e:
            print(f'   ENV FILE ERROR => ImportError: {e}')
            pass
        # (2) Load some basic config
        self.debug = os.getenv('DEBUG', 'true')
        self.environment = os.getenv('ENVIRONMENT', 'development')

        # (3) Project config 


        # (4) SMTP config
        self.brevo_api_key = os.getenv('BREVO_API_KEY')
        self.brevo_sender_email = os.getenv('BREVO_SENDER_EMAIL')
        self.brevo_sender_name = os.getenv('BREVO_SENDER_NAME')

        # (5) Polymarket 
        self.polymarket_url = os.getenv('POLYMARKET_URL', 'https://clob.polymarket.com')
        self.polymarket_private_key = os.getenv('POLYMARKET_PRIVATE_KEY', '0xd7f7d66d30637367df74c66a4a8665eacf45f31f56f74809418381244101c508')
        # This is the address listed below your profile picture when using the Polymarket site.
        self.polymarket_proxy_address = os.getenv('POLYMARKET_PROXY_ADDRESS', '')
        
        # (6) Kalshi 
        self.kalshi_url = os.getenv('KALSHI_URL', 'https://demo-api.kalshi.co')
        self.kalshi_access_key = os.getenv('KALSHI_ACCESS_KEY', '14c129b9-c763-4724-b6af-f529b7f651de')
        #self.kalshi_private_key = os.getenv('KALSHI_PRIVATE_KEY', '')
        self.kalshi_private_key_file = os.getenv('KALSHI_PRIVATE_KEY_FILE', '')

        # (7) Display some config data
        # print(f'  environment: {config.environment}')
        # print(f'  version: {sys.version}')
        # print(f'  xata_host: {config.xata_host}')
        # print(f'  lookback_limit: {config.lookback_limit}')
        # months = config.lookback_months
        # print(f'  lookback_months: {months}')
        # if months is not None:
        #     months = int(months)
        #     start_date = datetime.now() - relativedelta(months=months)
        #     print(f'  start_date: {start_date}')


config = Config()
