import random;
import json
import urllib.request as urlib

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
    #local_dict[last_key] = [local_str[i]]
    if (last_key in dict_):
      buf = dict_.get(last_key);
      buf = buf + local_dict.get(last_key);
      dict_.update({last_key:buf});
    else:
      dict_.update({last_key:local_dict.get(last_key)})
    if (last_key[-1] == '!' or last_key[-1] == '?' or last_key[-1] == '.'):
      dict_.update({last_key:local_dict.get(last_key) + ['END']});
      if (i != len(local_str)):
        next_key = str(local_str[i+1]);
        dict_.update ({'BEGIN':dict_.get('BEGIN')+[next_key]});
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

url = "http://46.21.249.29:8000/api/text/1"
url2 = "http://46.21.249.29:8000/api/dict"
webUrl = urlib.urlopen(url)
data = webUrl.read()
encoding = webUrl.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))
dict_1 = {};
for n in JSON_object:
    (check_text(n['text']))
for key,value in dict_1.items():
  new_value = {'word':key,'values':value};
  print (new_value)
  for i in value:
    new_small_value = {'word':key,'values':[i]}
    params = json.dumps(new_small_value).encode('utf-8');
    req = urlib.Request(url2, data=params,
      headers={'content-type': 'application/json'});
    response = urlib.urlopen(req);
    print(response.read().decode('utf-8'));
#print(JSON_object[0]['id'])
