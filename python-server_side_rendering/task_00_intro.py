#!.usr/bin/python3

import os
def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str):
            raise TypeError("template is empty")
        
        if len(template) == 0:
            raise IndexError("string is empty")

        if not isinstance(attendees, list): 
            raise TypeError("attendees not a list")
        
        if len(attendees) == 0:
            raise IndexError("No data provided")
        
        if not isinstance(attendees[0], dict):
            raise TypeError("not a list of dicts")
        
        for i in range(len(attendees)):
        
            for f, h in attendees[i].items():
            
                invitation_text1 = template.replace("{name}", attendees[i]["name"])
                invitation_text2 = invitation_text1.replace("{event_title}", attendees[i]["event_title"])
                invitation_text3 = invitation_text2.replace("{event_date}", attendees[i]["event_date"])
                invitation_text4 = invitation_text3.replace("{event_location}", attendees[i]["event_location"])

            with open(f"output_{i+1}.txt", 'w') as file:
                file.write(invitation_text4)
                
                if os.path.exists(f"output_{i+1}.txt") == False:
                    file.write(invitation_text4)
                else:
                    file.write(invitation_text4)
        
    except Exception as e:
        print(e)
