def CreateUser(email,firstname,lastname,password,username):
    createUser_data = {'command':'createUser','account':'admin','email':email,'firstname': firstname,
                        'lastname': lastname, 'username':username, 'password': password, 'response': 'json'}
    createUser = admin.post(url, data=createUser_data)
    resp_status = createUser.status_code
    if(resp_status == 200):
        return getLoginStatus(username,password)
    return createUser.status_code