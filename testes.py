from requests import get,post
import os

os.system('clear')
url='http://192.168.43.66:5000/'
api_tokens=post(url+'token/',json={'username':'saidino','password':'root'})

# print(api_tokens.json())
def get_acess_token():
    acess_token=None
    if 'access' in api_tokens.json():
        print('yes got token sucessfully')
        print(f'{api_tokens.json()}'if 'y'in  input('what to see ? n/y') else '')
        acess_token=api_tokens.json()['access']

    else: 
        
        print('no token found')
    return acess_token

def get_api_data(access_token):
    if access_token != None:
        data =get(url+'saidin-book/', headers={'Authorization':f'Bearer {access_token}'})
        print(data.json())

if __name__ =='__main__':
    api_key=get_acess_token()
    data =get_api_data(api_key)
    
