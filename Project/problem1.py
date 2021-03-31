"""
Problem1

Implement a group_by_owner function that:
1) Accept a dictionary name containing file owner name for each file name.
2) Returns a dictionary containing a list of file name for each owner, in any order.

"""

Input_dict = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
} # Input Dictionary


def group_by_owners(Input_dict):
  authors = sorted( list( set( Input_dict.values() ) ) )
  author_books = { author : list( filter( lambda title : Input_dict[title] == author, Input_dict ) ) for author in authors }
  return author_books

print(group_by_owners(Input_dict))