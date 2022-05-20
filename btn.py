from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#---Hello---#

btnStart = KeyboardButton( 'Я готов!' )
startMenu = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnStart )


#---Return---#

btnMain = KeyboardButton( 'Вернуться в начало' ) 
btnBack = KeyboardButton( 'Назад' )
mainbtn = ReplyKeyboardMarkup( resize_keyboard=True ).add(btnMain, btnBack) 

#---Menu---#

btnGos = KeyboardButton( 'Государственная тайна' )
typesMenu = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnGos, btnMain )

#---Choose---#

btnOrgan = KeyboardButton( 'Об органах' )
btnSubject = KeyboardButton( 'О субъектах' )
ChooseBTNS = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnOrgan, btnSubject, btnMain )


#---Organs---#

btnFDA = KeyboardButton( 'Федеральное дорожное агентство' )
btnFSB = KeyboardButton( 'ФСБ' )
btnGTK = KeyboardButton( 'ГосТехКомиссия' )
btnMVD = KeyboardButton( 'МВД' )
btnFSTEK = KeyboardButton( 'ФСТЭК' )
OrgansBTNS = ReplyKeyboardMarkup( resize_keyboard=True ).add(btnFDA, btnFSB, btnGTK, btnMVD, btnFSTEK, btnBack)

#---Subjects---#

btnDopusk = KeyboardButton('Допуск к гос. тайне')
btnZasec = KeyboardButton('Засекречивание сведений')
btnPropusk = KeyboardButton('Организация пропускного режима')
btnRegime = KeyboardButton('Осуществление режима секретности')
btnNositel = KeyboardButton('Обращение с носителями')
btnPriem = KeyboardButton('Прием, сдача носиетелей')
btnDP = KeyboardButton('Ведение секретного делопроизводства')
btnRassled = KeyboardButton('Служебные расследования')
SubjectBTNS = ReplyKeyboardMarkup( resize_keyboard=True ).add(btnDopusk, btnZasec, btnPropusk, btnRegime, btnNositel, btnPriem, btnDP, btnRassled, btnBack)

#---Complete---#

btnComplete = KeyboardButton( 'Завершить' )
completeMenu = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnComplete )






