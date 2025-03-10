#Functions Go Here
def make_statement(statement, decoration):
   """Emphasizes headings by adding decoration
      at the start and the end"""
   
   print(f"{decoration * 3} {statement} {decoration * 3}")

#Main Routine Goes Here
statement = 'Programming Is Fun!!!'
decoration = '👍'

make_statement(statement, decoration)