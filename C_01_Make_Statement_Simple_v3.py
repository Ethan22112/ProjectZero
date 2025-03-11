#Functions Go Here
def make_statement(statement, decoration, lines = 1):
   """Creates headings(3 lines), subheadings (2 lines) and
      emphasized text / mini-headings (1 line). Only use emoji
      for single line statements"""
   
   middle = f"{decoration * 3} {statement} {decoration * 3}"
   top_bottom = decoration * len(middle)

   if lines == 1:
      print(middle)
   elif lines == 2:
      print(middle)
      print(top_bottom)
   else:
      print(top_bottom)
      print(middle)
      print(top_bottom)

#Main Routine Goes Here

make_statement(statement = 'Programming Is Fun!!!', decoration = '=', lines = 3)
make_statement(statement = 'Programming Is Still Fun!!!', decoration = '*', lines = 2)
make_statement(statement = 'Emoji In Action', decoration = '🐍')

#This Program Was Created 3/11/2025 