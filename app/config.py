class Config:
    SECRET_KEY = "SUPER SECRET"



class DevelopmentConfig(Config):
    DEBUG = True


config = {
    "develomenp": DevelopmentConfig,
    "default": DevelopmentConfig
}