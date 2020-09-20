# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 01:41:11 2020

@author: Samuel
"""
#from my_app.models import User
#from my_app.views import user_list
#from ANGIE import check_status
#from voter_email import email_update
#get_status = lambda u: check_status(u.first, u.last, u.county, u.dob)
#email = lambda u, status: email_update(u.first, u.last, u.email, status) 
   
def roster_sweep(user_list):
    '''Given a list of User objects, return a dictionary of three sets:
        1. users previously not active but now active
        2. users previously not inactive but now inactive
        3. users previously not invalid but now invalid
        4. errors
        
    Each user who falls into one of these three sets is sent an email
    '''
    deactivated, invalidated, activated, error = set(), set(), set(), set()
    for u in user_list:
        #print(u)
        status = get_status(u)
        #print(status, type(status), u.status, type(u.status))
        if status != u.status:
            
            if status == 'ACTIVE':
                email(u, 'ACTIVE')
                activated.add(u.uid)
                
            elif status == 'INACTIVE':
                email(u, 'INACTIVE')
                deactivated.add(u.uid)
                
            elif status == 'INVALID':
                email(u, 'INVALID')
                invalidated.add(u.uid)
                
            else:
                email(u, 'ERROR')
                error.add(u.uid)
                
            u.status = status
                
    return {'deactivated':deactivated,'invalidated':invalidated,
            'activated':activated, 'error':error} 

#Example
class User():
    def __init__(self, uid, first, last, county, dob, email, status):
        self.uid, self.first, self.last, self.county, = uid, first, last, county
        self.dob, self.email, self.status = dob, email, status

stay_active = User(0, 'V', 'CHEN', 'FULTON', 10262000, 'chen.victoria123@gmail.com', 'ACTIVE')
active_to_inactive = User(1, 'L', 'LAZIBONES', 'COOB', 12311900, 'chen.victoria123@gmail.com', 'ACTIVE')
active_to_invalid = User(2, 'S', 'SCREWED', 'GOOP', 3132001, 'chen.victoria123@gmail.com', 'ACTIVE')

stay_inactive = User(3, 'A', 'HAMILTON', 'DISNEYPLUS', 10101700, 'chen.victoria123@gmail.com', 'INACTIVE')
inactive_to_active = User (4, 'F', 'AWAKENS', 'STARREDWAR', 12251915, 'chen.victoria123@gmail.com', 'INACTIVE')   
inactive_to_invalid = User(5, 'D', 'DROPPEDBOI', 'POOMACHO', 5252000, 'chen.victoria123@gmail.com', 'INACTIVE')

stay_invalid = User(6, 'C', 'VHEN', 'ULFTON', 2132001, 'chen.victoria123@gmail.com', 'INVALID')
invalid_to_active = User(7, 'V', 'VICTOR', 'BUTTERCUP', 9242001, 'chen.victoria123@gmail.com', 'INVALID')
invalid_to_inactive = User(8, 'C', 'CONFUZZLED', 'FULTON', 5051925, 'chen.victoria123@gmail.com', 'INVALID')

example_status_dict = {stay_active:'ACTIVE',
                       active_to_inactive:'INACTIVE',
                       active_to_invalid:'INVALID',
                       stay_inactive:'INACTIVE',
                       inactive_to_active:'ACTIVE',
                       inactive_to_invalid: 'INVALID',
                       stay_invalid: 'INVALID',
                       invalid_to_active: 'ACTIVE',
                       invalid_to_inactive: 'INACTIVE'}

get_status = lambda u: example_status_dict.get(u,None)
email = lambda u, status: print(f'hi {u.first}. {u.last}, (email: {u.email}), \
                                your voter registration status was recently changed to {status}\n')

print(roster_sweep([stay_active, active_to_inactive, active_to_invalid,
                    stay_inactive, inactive_to_active, inactive_to_invalid,
                    stay_invalid, invalid_to_active, invalid_to_inactive]))