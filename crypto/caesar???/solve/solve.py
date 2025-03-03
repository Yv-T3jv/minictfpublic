chinese_ascii_start = 13312
chinese_ascii_end = 40959
num_char = chinese_ascii_end - chinese_ascii_start + 1
def to_int(c):
  idx = ord(c) - chinese_ascii_start
  return idx 
def to_chinese(idx):
  return chr(idx + chinese_ascii_start)
def enc_message(msg, offset):
  res = ""
  for c in msg:
    if ord(c) >= chinese_ascii_start and ord(c) <= chinese_ascii_end:
      idx = to_int(c)
      newidx = (idx + offset) % num_char 
      newchar = to_chinese(newidx)
      res += newchar
    else:
      res += c
  return res 
enc = '''Chinese Caesar Cipher? Here's my encrypted message: 
䟶䔑侽屚菞洇娥舫

侽屚菞岲䒃灐唂䩚憥虑洇䙤囲刌䟫扗菞嗥喒，屫䶫蚝虊聦䠶䒃獾䢚夃嶲妔墛巨婓䧊䩅䒑皈洇痔畟刌䟫夃瞀䬏䵥貢䪋䗟瞀䤞。虔哷巨，贒淃䙤囲夃嶲洇虈榞䩔勘，侽屚菞蚓撓墓䒽乼䟾痔畟刌䟫䔽壐洇衐耄尼喒。嶯尊劉䕑侽屚菞洇怅噸、狾与䕨䩍垒䓌䒌䒭尼跥虞经娥舫。

䒃、䕃䓋岲侽屚菞
侽屚菞岲䙤囲刌䟫載乢洇䒃灐扗菞嗥喒，䩅菞皈趃耄蚝虊䢉帓、溷聦、蚉䪔、斒採妙娛燌夃嶲壎戸夁䢳贓籒洇浱床，蚝咻灳䓎䒽“屚咟”。扗菞虊炎䒰，䩅菞皈䒐䕈趃耄虓殫依灐夃嶲湨艉，虛趃耄噮蚢凩䓣尳湨艉，䕨唗剼䒐䪏狾与洇妔墛。

䔏、侽屚菞洇䒾耄狾与
侽屚菞蚝咻䢉䒽䕨䒎䡣灐狾与：

聦輛悤喒
䶫虜灐扗菞悤喒䒰，䩅菞皈趃耄刏墓䒃獾䢚楯煎洇妔墛䕾䤤，䘎倅剉溄凩、贓䠜嶲、蚉䪔䢉帓䬏斒採䢬殫燌。扒刏墓䒃䒭䕾䤤，䩅菞皈䧶䩲稺䩙剼唗洇“屚咟”，哹蚝虊婓䔧屚咟嘚䢉。

宾貵悤喒
䩅菞皈趃耄䙠大硭呴洇嶐䤤䳫䟐䩚宾䡾，䪏屹艁捘宾溷剼壎洇嶐䤤䳫。䶫虜灐悤喒䒎，夃嶲䬏燙毨䪏庺衐耄，䵥貢䧒䗟劧䒽䟶讱。

畿䪋悤喒
畖䪋䔉聦輛悤喒䬏宾貵悤喒洇棼朼，䩅菞皈履趃耄溷聦䕾䤤稺䩙畂玥，䩋趃耄䶫宾貵剼多䒰䙠大硭呴洇墓帟。

䒌、侽屚菞洇垒䓌
婓䧊夃嶲瞀䤞
侽屚菞耉浙䔉䙤囲刌䟫載乢洇依䒭尼䪔，蚝虊扗菞，䩅菞皈䩲䕨䶫刡葸䒰呬䵽湨艉，婓䧊夃嶲抷哶。

乼䟾䵥貢䪋䗟
屣舽岲聦輛悤喒虛岲宾貵悤喒，䵥貢䧒䗟螀岲侽屚菞䒰䒐䩲墙疽洇䒃蝫䢉。蚝虊扗菞，䩅菞皈䩲䕨凩䖝倅䗘酛寋䶳䒑䕙䔽䧒䗟，䟴䪏刏墓浱床。

娫䤫夃嶲䢞尳
舻依扗菞䒰洇輛浱螀玪葢夃嶲䩔勘洇䣐捂，䩅菞皈趃耄䒐尰凩䓣尳洇夃嶲䬏周䟺，䕑皏娫䤫寷䒭䙤囲刌䟫載乢洇䢞尳䒑虞懨。

䵞、畖巢艰
侽屚菞䒐䕈岲䒃䶽夃嶲扗奿，嵷岲䒃灐凩䓣䬏墓谂洇虊炎。分䒽䙤囲刌䟫梴倀皈婓䘞䔉䒃䒭勘樳硭墔洇哶䩳，䪏屹䓢娫䤫䔉痔畟刌䟫经䒝洇䩔勘。蚝虊䩅䒑侽屚菞，䩅菞皈䒐䕈瞀侢婓䧊硭蔮夃嶲，虛瞀畖艉噚䪏蛖䪋洇嶎䩎，䒽硭呴洇盏䒝殢搲壖䒎䷝刡洇乽滃。

䶫虜䒭䙤囲䦙噮蚢䩔勘洇屹䕦，侽屚菞洇䕺䚿型䤣峁樳。分履岲䒃灐妔墛，䓢岲䒃灐嶽蛊，晃䤴淃屣寳䔽虋䪔嵷酛洇夃嶲呈即。

倅䗘稺䩙妊初洇屚咟？
墔䕯劉扒䒭凚熩嶂姥䒽剼唗洇䒰尊婒虳：

侪䠜凚扐熯䓠䗐
侪䠜凚扐熯䧄䟮䗐
侪䠜凚扐熯䧄䓠䗐
呩侪奯䩺
寳凚䒃
䒎䢕畂
侪䠜凚扐熯䧄䔏䗐
寳凚赹
侪䠜凚扐熯䔏䧄䔏䗐
寳凚䒌
䒎䢕畂
劒䠜凚扐熯䒌䗐
侪䠜凚扐熯䟮䗐
寳凚䒃
侪䠜凚扐熯䧄䵞䗐
寳凚䒌
劒䠜凚扐熯䧄䓠䗐
劒䠜凚扐熯䔗䗐
䩶侪奯䩺
'''
occ = {}
for c in enc:
  if ord(c) <= chinese_ascii_end and ord(c) >= chinese_ascii_start:
    try:
      occ[c] += 1 
    except:
      occ[c] = 1
maxx = 0 
mostcommon = ''
for k in occ:
  if occ[k] > maxx:
    mostcommon = k 
    maxx = occ[k] 
gg = (to_int('的') - to_int(mostcommon)) % num_char
print(enc_message(enc, gg))