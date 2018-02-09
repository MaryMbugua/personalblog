import os



class Config:
    ''' 
    general configuration  parent class
    '''
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nish:Nish@localhost/personalblog'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class ProdConfig(Config):
    '''
    production configuration child class
    Args:
    Config: The parent configuration class
    with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    development configurationchild class
    Args:
    Config:The parent configuration class with general
    configuration settings
    '''
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}