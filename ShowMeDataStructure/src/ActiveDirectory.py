#completed
'''
Created on Apr 14, 2020

@author: Rajeswari_S
'''
from conda.common._logic import TRUE

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def isUserPresent(self,givenUser):
        for user in self.users:
            if(givenUser==user):
                return True
        return False
    
    def isGroupPresent(self,groupName):
        for group in self.groups:
            if(group.get_Name()==groupName):
                return True
        return False
    
    def add_group(self, group):
        self.groups.add(group)
        
    def remove_group(self,group):
        self.groups.remove(group)

    def add_user(self, user):        
        self.users.add(user)
        
    def remove_user(self,user):
        self.users.remove(user)
        
    def remove_user_fromGroup(self,group,user):
        for g in self.groups:
            if(g.get_name()==group.get_name()):
                g.users.remove(user)
                break
    
    def get_subGroupSize(self):
        return len(self.groups)
    
    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_UsersCount(self):
        return len(self.users)
    
    def get_name(self):
        return self.name

class ActiveDirectory(object):
    def __init__(self):
        return
    
    def is_user_in_group(self,user, group):       
        traversed_groups=set()
        return self.is_in_group(user, group,traversed_groups)

    def is_in_group(self,user, group,traversed_groups):
        users=group.get_users()
        traversed_groups.add(group)
        if user in users: # if user is present in current group
            return True
        else: # check user is present in sub groups
            groups=group.get_groups()
            for g in groups:           
                if g  not in traversed_groups: #if group is checked already, no need to check again
                    if self.is_in_group(user, g,traversed_groups):
                        return True
        return False