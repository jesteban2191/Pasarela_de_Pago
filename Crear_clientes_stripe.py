import os
import dotenv
from Pasarela import *



def initialize_environment():

    # Load environment variables from .env file

    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

    if os.path.exists(env_path):
        dotenv.load_dotenv(env_path)
        print("Environment variables loaded successfully.")
    else:
        raise FileNotFoundError(f".env file not found at {env_path}")





def main():
    initialize_environment()
    gateway = "stripe"
    gtway = PaymentGatewayFactory.create_gateway(gateway)

    client_info = {"name": "Nancy Pérez", 
                   "email": "napeche21@outlook.com"}

    client = gtway.create_client(**client_info)
    print(client)



if __name__ == "__main__":
    main()
    





