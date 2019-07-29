#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
    def __str__(self):
        return str(self.balance) + ' is the balance of ' + self.label
    def withdraw (self, amount):
        if amount > 0 and amount < self.balance:
            self.balance = self.balance - amount
        else: print('cannot withdraw this amount')
    def deposit(self, add):
        if add > 0:
            self.balance = self.balance + add
        else:
            print('you cannot deposit a negative amount')
    def rename(self, newName):
        if newName == '':
            self.label = self.label
        else:
            self.label = newName
    def transfer (self, dest_account, amount):
        acc1 = self
        acc2 = dest_account
        if amount > 0 and amount < self.balance:
            acc1.balance = acc1.balance - amount
            acc2.balance = acc2.balance + amount
