from item import *
sample_book = Inscription("book", "This book smells of musty paper. It is an ancient thing.")
sample_book.add_page("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
anim id est laborum.""")
sample_book.add_page("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
anim id est laborum.""")

dirty_page = Inscription("dirty page", "This page is dirty")
dirty_page.add_page("""I don't care how filthy it is! I'm putting it in my game to test my ReGeX!""")

holy_book = Inscription("holy book", "* heavenly choir sound effects *")
holy_book.add_page("""Random Scripture stuff. Too bored to complete it.""")
holy_book.add_page("""Testing page 2""")