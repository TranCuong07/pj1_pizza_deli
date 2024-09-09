from pydantic import BaseModel

class Settings(BaseModel):
    authjwt_secret_key: str = 'rG9Y6nX8z3KxQ1J7V2b4T5n8w9Y7d3F2vG6hJ1L5rG3'
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_secure: bool = False
    authjwt_cookie_csrf_protect: bool = False

settings = Settings()
