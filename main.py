import os
import dotenv



def initialize_environment():

    # Load environment variables from .env file

    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

    if os.path.exists(env_path):
        dotenv.load_dotenv(env_path)
        print("Environment variables loaded successfully.")
    else:
        raise FileNotFoundError(f".env file not found at {env_path}")





def main():
    pass


if __name__ == "__main__":
    main()
    





