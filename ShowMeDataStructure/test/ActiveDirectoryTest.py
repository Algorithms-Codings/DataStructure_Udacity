from src.ActiveDirectory  import ActiveDirectory
from src.ActiveDirectory import Group
import unittest
class ActiveDirectoryTest(unittest.TestCase):
    
    def test(self):
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

        parent_user1 = "parent_user1"
        parent_user2 = "parent_user2"
        parent_user3 = "parent_user3"
        parent.add_user(parent_user1)
        parent.add_user(parent_user2)
        parent.add_user(parent_user3)

        ac = ActiveDirectory()

        self.assertTrue(ac.is_user_in_group("parent_user1", parent),"parent_user1  Not present in parent")
        self.assertTrue(ac.is_user_in_group("sub_child_user1", parent))
        self.assertTrue(ac.is_user_in_group("child_user2", parent))
        self.assertTrue(ac.is_user_in_group("sub_child_user2", sub_child2))
        self.assertTrue(ac.is_user_in_group("sub_child_user3", parent))
        self.assertFalse(ac.is_user_in_group("child_user2", sub_child2))
        self.assertTrue(ac.is_user_in_group("sub_child_user1", child3))

        


if __name__ == '__main__':
    ActiveDirectoryTest.main()
