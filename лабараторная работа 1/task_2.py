# TODO Найдите количество книг, которое можно разместить на дискете

mb_info = 1.44
bait_in_kb = 1024
kb_in_mb = 1024

bait_info = mb_info * bait_in_kb * kb_in_mb

number_of_pages = 100
string_in_page = 50
simbols_in_string = 25
baits_in_symbol = 4

book_weight = number_of_pages * string_in_page * simbols_in_string * baits_in_symbol

books_total = round(bait_info // book_weight)


print("Количество книг, помещающихся на дискету:", books_total)
