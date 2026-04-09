import httpx
from faker import Faker

class BookStoreService:
    def  __init__(self):
        self.base_url =  'https://demoqa.com'
        self.fake = Faker()
        self.username = self.fake.user_name()
        self.password = '8Il*8U8W~8B' # Gerei uma senha forte com o LastPass
        self.userid = None
        self.token = None

    def create_user(self):
        '''
        Create a new user
        '''
        payload = {'userName': self.username, 'password': self.password}
        return httpx.post(f'{self.base_url}/Account/v1/User', json=payload)
    
    def generate_token(self):
        '''
        Generate token
        '''
        payload = {'userName': self.username, 'password': self.password}
        response = httpx.post(f'{self.base_url}/Account/v1/GenerateToken', json=payload)
        if response.status_code == 200:
            self.token = response.json().get('token')
        return response
    
    def check_authorization(self):
        '''
        Confirm Authorization
        '''
        payload = {'userName': self.username, 'password': self.password}
        return httpx.post(f'{self.base_url}/Account/v1/Authorized', json=payload)
    
    def list_books(self):
        '''
        List all books that are available
        '''
        return httpx.get(f'{self.base_url}/BookStore/v1/Books')
    
    def rent_book(self, userid, bookid):
        '''
        Rent two books
        '''
        headers = {'Authorization': f'Bearer {self.token}'}
        payload = {
            'userId': userid,
            'collectionOfIsbns': [{'isbn': book} for book in bookid]
        }
        return httpx.post(f'{self.base_url}/BookStore/v1/Books', json=payload, headers=headers)
    
    def get_user_details(self, userid):
        '''
        List user detail with the books rented
        '''
        headers = {'Authorization': f'Bearer {self.token}'}
        return httpx.get(f'{self.base_url}/Account/v1/User/{userid}', headers=headers)
