from fastapi.security import OAuth2PasswordBearer
class oauth():

    @staticmethod
    def get_oauthscheme():
        return OAuth2PasswordBearer(tokenUrl='token')

    @staticmethod
    def get_jwtsecret():
        return "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY0MzIyNTIxNSwiaWF0IjoxNjQzMjI1MjE1fQ.rptEt13F1UQidSjXzPzTyFXVIRW99pFKqMet70d0C80"
