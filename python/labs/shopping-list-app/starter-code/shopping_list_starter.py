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

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

    choice = raw_input("Enter your choice [a|b|c|d|e]:")

    if choice == 'a':
        item = raw_input('what would you like to add? ')
        shopping_list.append(item)
    if choice == 'b':
        remItem = raw_input('What would you like to remove? ')
        shopping_list.remove(remItem)
    if choice == 'c':
        searchItem = raw_input('what are you searching for? ')
        if searchItem in shopping_list:
            print(searchItem + " is in your list.")
        else:
            print(searchItem + ' is not in your list.')
    if choice == 'd':
        print(shopping_list)
    if choice == 'e':
        break












    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
