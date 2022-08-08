class Config:
    SECRET_KEY = "SUPER SECRET"



class DevelopmentConfig(Config):
    DEBUG = True


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}