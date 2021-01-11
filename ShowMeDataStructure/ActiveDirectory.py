#completed
'''
Created on Apr 14, 2020

@author: Rajeswari_S
'''

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    traversed_groups=set()
    return is_in_group_(user, group,traversed_groups)

def is_in_group_(user, group,traversed_groups):
    users=group.get_users()
    traversed_groups.add(group)
    if user in users:
        return True
    else:
        groups=group.get_groups()
        for g in groups:           
            if g  not in traversed_groups: #if group is checked already, no need to check again
                if is_user_in_group(user, g):
                    return True
    return False


parent = Group("parent")

child1 = Group("child1")
child2 = Group("child2")
child3 = Group("child3")

sub_child1 = Group("subchild1")
sub_child2 = Group("subchild2")
sub_child3 = Group("subchild3")

child1.add_group(sub_child1)
parent.add_group(child1)

child2.add_group(sub_child2)
parent.add_group(child2)

child3.add_group(sub_child3)
parent.add_group(child3)

child3.add_group(sub_child1)



sub_child_user1 = "sub_child_user1"
sub_child_user2 = "sub_child_user2"
sub_child_user3 = "sub_child_user3"
sub_child1.add_user(sub_child_user1)
sub_child2.add_user(sub_child_user2)
sub_child3.add_user(sub_child_user3)

child_user1 = "child_user1"
child_user2 = "child_user2"
child_user3 = "child_user3"
child1.add_user(child_user1)
child2.add_user(child_user2)
child3.add_user(child_user3)


parent_user1="parent_user1"
parent_user2="parent_user2"
parent_user3="parent_user3"
parent.add_user(parent_user1)
parent.add_user(parent_user2)
parent.add_user(parent_user3)

if is_user_in_group("parent_user1", parent):
    print("present in group")
else:
    print("Not present in group")
