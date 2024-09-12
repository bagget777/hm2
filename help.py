# count_text = 'Hello, world'
# exp_join = ','.join(count_text) # добавляет введённый аргумент после каждого символа
# exp_split = count_text.split(',')

# print(exp_join)
# print(exp_split)

# text_ir = 'Welcome'
# exp_rjust = text_ir.ljust(30, '-') # удлиняет строку с лево-направо
# exp_ljust = text_ir.rjust(30, '+') # удлиняет строку с право-налево
# exp_center = text_ir.center(30,'*') # удлиняет строку с двух сторон

# print(exp_ljust) #left_just
# print(exp_rjust) #right_just
# print(exp_center) #center_just

# strip_text = '=====Hello world======'
# lstrip_text = '+++++Hello world+++++'
# rstrip_text = '-----Hello world-----'

# exp_strip = strip_text.strip('=') # убирает лишние знаки с двух сторон
# exp_lstrip = lstrip_text.lstrip('+') # убирает лишние знаки с левого края
# exp_rstrip = rstrip_text.rstrip('-') # убирает лишние знаки с правого края 

# print(exp_strip) #strip
# print(exp_lstrip) # left_strip
# print(exp_rstrip) # right_strip

# text_up = 'hello World'
# exp_upper = text_up.upper() # меняет все буквы на заглавные 
# exp_capitalize = text_up.capitalize() # первая буква становится заглавное остальные заглавные уменьшатся 

# print(exp_capitalize)
# print(exp_upper)

# text_down = 'HELLO WoRLD'
# exp_casefold = text_down.casefold() # более продвинутая форма 
# exp_lower = text_down.lower() # уменьшает все заглавные буквы но только классического алфавита

# print(exp_casefold)
# print(exp_lower)

# just_text = 'Hello world'
# exp_index = just_text.index('r') # показывает индекс
# exp_find = just_text.find('l') # ищет только первую букву
# exp_count = just_text.count('l') # ищет все буквы

# print(exp_index)
# print(exp_find)
# print(exp_count)

# ################################## это будут функции связанные с format_map, format, f-string

# name = input('Введите своё имя пожалуйста: ')
# age = input(str('Введите свой возраст пожалуйста: '))
# bio = {'name': 'Bayzak', 'age': 15 }

# bios_f_string = f'My name is {name} and I am {age} years old. In my {age} years, I have achieved a lot.'
# bios_format = '''My name is {0}. I am {1} years old and I have {1} great story.'''.format(name, age)
# info_bio = "Name {name} from Kyrgyzstan age {age} old's".format_map(bio)

# print(bios_f_string) # мы добавили f-string он добавляет переменные в наш текс которые мы можем сами ввести 
# print(bios_format) # мы добавили format он может несколько раз ставить наши переменные и тут синтаксис начинается с нуля 
# print(info_bio) # с format_map работает только картеж хоть грустна но мы не сдаёмся 

# print("Her name is {}".format('SuSaNo')) # если переменная пуста то её можно заполнить внутри format('здесь!')

# ################################## это будут функции связанные с двоичным кодом

code_text = 'Hello wolk;dsfhjdalpoasdopokpadijoferld' 

exp_encode = code_text.encode('UTF-16')  # превращает код в байт-код
exp_decode = exp_encode.decode('UTF-16') # возвращает байт-код в обычный как по моему мнение это даже очень интересно

print(exp_encode)
print(exp_decode) 

# ################################## это будут функции связанные с True or False

# endswith_text = 'Hello, World!'

# print(endswith_text.endswith('Hello')) # проверяет на наличие специальных знаков по типу:& , ? , !
# print(endswith_text.endswith('World!')) # если их нет будет True(что удостоверит что они есть) False(удостоверит что их нету)

# isalnum_text = 'Helloworld2'
# print(isalnum_text.isalnum()) # выводит True в том случаи если в тексте будут только буквы и цифры без специальных знаков

# isalpha_text = 'Helloworld'
# print(isalpha_text.isalpha()) # выводит True в том случаи если в тексте только буквы без цифр и спец.знаков

# isnumeric_text = '213232131'
# print(isnumeric_text.isnumeric()) # выводит True если в тексте только цифры без букв и спец.знаков

# isdecimal_text = '1321'
# print(isdecimal_text.isdecimal()) # выводит True в том случаи если в тексте только десятичные цифры без букв и спец.знаков

# isdigit_text = '12312'
# print(isdigit_text.isdigit()) # выводит True в том случаи если в тексте только цифры без букв и спец.знаков

# istitle_text = 'This Is My Title'
# print(istitle_text.istitle()) # выводит True если каждое новое предложение будет начинаться с заглавной буквой можно добавлять спец.знаки и цифры

# isupper_text = 'HELLO_WORLD!321'
# print(isupper_text.isupper()) # выводит True если все будут заглавными и туда можно добавлять спец.знаки с цифрами

# islower_text = 'hello world!'
# print(islower_text.islower()) # выводит True в том случаи если в тексте не будет заглавной буквы

# isprintable_text = 'daw_123A'
# print(isprintable_text.isprintable()) # выводит True если все символы в строке печатаются

# isidentifier_text = 'func_py'
# print(isidentifier_text.isidentifier()) # выводит True если в тексте не будет спец.знаков исключение '_' так же нельзя чтобы первая строка начиналась с цифры 

# isspace_text = ' '
# print(isspace_text.isspace()) # выводит True когда в строки только ' ' пробелы

# ##################################
