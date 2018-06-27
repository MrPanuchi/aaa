import random;

def check_text (text_):
  text_local_split = text_.split('\n\t');
  for i in range (0,len(text_local_split)):
    check_str(text_local_split[i],dict_1);
  rndmz (dict_1);

def check_str (str_,dict_):
  local_str = str_.split();
  local_dict = {'BEGIN':[]};
  last_key = 'BEGIN';
  for i in range (0,len(local_str)):
    local_dict.update({last_key:[local_str[i]]});
    if (last_key in dict_):
      buf = dict_.get(last_key);
      buf = buf + local_dict.get(last_key);
      dict_.update({last_key:buf});
    else:
      dict_.update({last_key:local_dict.get(last_key)})
    last_key = str(local_str[i]);
  'local_dict.update({last_key:''END''});'
  dict_.update({last_key:['END']});

def rndmz (dict_):
  text_rndmz = '';
  buf_list = dict_.get('BEGIN');
  buf_word = '';
  while (True):
    ch = random.randint(0,(len(buf_list)-1));
    if ('END' == str(buf_list[ch])):
      break;
    else:
      buf_word = buf_list[ch];
      buf_list = dict_.get(buf_word);
      text_rndmz = text_rndmz + buf_word + ' ';
  print (text_rndmz);


text_1 = '''Мороз и солнце, день чудесный!
	Еще ты дремлешь, друг прелестный –
	Пора, красавица, проснись;
	Открой сомкнуты негой взоры
	Навстречу северной Авроры,
	Звездою севера явись!
	Вечор, ты помнишь, вьюга злилась,
	На мутном небе мгла носилась;
	Луна, как бледное пятно,
	Сквозь тучи мрачные желтела,
	И ты печальная сидела –
	А нынче... погляди в окно:
	Под голубыми небесами
	Великолепными коврами,
	Блестя на солнце, снег лежит;
	Прозрачный лес один чернеет,
	И ель сквозь иней зеленеет,
	И речка подо льдом блестит.
	Вся комната янтарным блеском
	Озарена. Веселым треском
	Трещит затопленная печь.
	Приятно думать у лежанки.
	Но знаешь: не велеть ли в санки
	Кобылку бурую запречь?
	Скользя по утреннему снегу,
	Друг милый, предадимся бегу
	Нетерпеливого коня
	И навестим поля пустые,
	Леса, недавно столь густые,
	И берег, милый для меня. '''

dict_1 = {};
check_text(text_1);
