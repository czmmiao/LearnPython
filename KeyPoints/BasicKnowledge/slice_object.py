import numbers
import bisect
from typing import MutableSequence, Container
from collections import abc

class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])
        return self.staffs[item]

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

staffs =["user1","user2","user3","user4"]
group = Group(company_name="imooc", group_name="user", staffs=staffs)

sub_group= group[:2]
print(group[:2], type(group[:2]))
print(group[0], type(group[0]))
print(sub_group[:2])

for user in sub_group:
    print(user)

print(len(sub_group))
print(reversed(sub_group))


for user in sub_group:
    print(user)
