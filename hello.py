from bottle import route, post, delete, run, request
import json
import requests
import urllib

base_url = 'https://<yourserver>.<yourdomain>.<xyz>'

@route('/hello')
def hello():
    return "Hello World!"


@post('/rebrand')
def do_rebrand():
    access_token = authenticate()

    rebrand_data = request.forms['value'].replace('\t','').replace('\n','')
    rebrand_url = base_url + '/api/branding'
    rebrand_headers = {
        'accept': 'application/json', 
        'Content-Type': 'application/json',
        'authorization': 'Bearer ' + access_token
    }
    rebrand_response = requests.post(rebrand_url, data=rebrand_data, params=None, headers=rebrand_headers)

    return rebrand_response


@post('/reset')
def do_reset():
    access_token = authenticate()

    reset_url = base_url + '/api/branding'
    reset_headers = {
        'accept': 'application/json', 
        'Content-Type': 'application/json',
        'authorization': 'Bearer ' + access_token
    }
    reset_response = requests.delete(reset_url, headers=reset_headers)
    return reset_response


@post('/palette')
def do_palette():
    access_token = authenticate()

    palette_data = request.forms['value'].replace('\t','').replace('\n','')
    palette_url = base_url + '/api/palettes'
    palette_headers = {
        'accept': 'application/json', 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    palette_response = requests.post(palette_url, data=palette_data, params=None, headers=palette_headers)

    return palette_response


@post('/removePalette')
def do_removePalette():
    access_token = authenticate()
    palette_name = request.forms['value']
    palette_url = base_url + '/api/palettes/' + palette_name
    palette_headers = {
        'accept': 'application/json', 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    palette_response = requests.delete(palette_url, headers=palette_headers)
    return palette_response


@post('/createUser')
def do_createUser():
    access_token = authenticate()
    user_name = request.forms['user']
    country = request.forms['country']

    role = request.forms['role']
    if role == 'Data Designer':
        role = '5cfab3e4b612768fd37705ef'
    elif role == 'Dashboard Designer':
        role = '5cfab3e4b612768fd37705f5'
    else:
        role = '5cfab3e4b612768fd37705f6'

    create_user_url = base_url + '/api/users'
    create_user_headers = {
        'accept': 'application/json', 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    create_user_data = [{
        'email': user_name,
        'roleId': role,
        'password': 'TotallySecurePassword123'
    }]
    create_user_response = requests.post(create_user_url, data=json.dumps(create_user_data), headers=create_user_headers)
    user_id = create_user_response.json()[0][0]['_id']

    security_data = [{
        'server': 'LocalHost',
        'elasticube': 'Sample ECommerce',
        'table': 'Country',
        'column': 'Country',
        'datatype': 'text',
        'shares': [{
            'party': user_id,
            'type': 'user'
        }],
        'members': [
            country
        ]
    }]
    security_url = base_url + '/api/elasticubes/datasecurity'
    security_response = requests.post(security_url, data=json.dumps(security_data), headers=create_user_headers)
    return security_response


def authenticate():
    payload = {
        'username': 'username@domain.xyz',
        'password': 'verysecurepassword'
    }
    data = json.dumps(payload)
    headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
    login_url = base_url + '/api/v1/authentication/login'
    response = requests.post(login_url, data=data, params=None, headers=headers)
    response_data = response.json()
    return response_data['access_token']


run(host='localhost', port=8080, debug=True)