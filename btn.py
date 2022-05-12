from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#---Hello---#

btnStart = KeyboardButton( 'Я готов!' )
startMeny = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnStart )


#---Rerutn---#

btnMain = KeyboardButton( 'Вернуться в начало' ) 
btnBack = KeyboardButton( 'Назад' )
mainbtn = ReplyKeyboardMarkup( resize_keyboard=True ).add(btnMain, btnBack) 

#---Commercy Menu---#

btnCom = KeyboardButton( 'Государственная тайна' )
typesMeny = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnCom, btnMain )

#---U Mode Menu---#

btnYourMode_is_false = KeyboardButton( 'Об органах' )
btnYourMode_is_True = KeyboardButton( 'О субъектах' )
yourModeMeny = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnYourMode_is_True, btnYourMode_is_false, btnMain )

#---Have Departament---#

btnHave = KeyboardButton( 'О государственной' )
btnHavent = KeyboardButton( 'О негосударственной' )
haveDepartament = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnHave, btnHavent, btnMain )  

#---accept Qalification---#

btnQualGood = KeyboardButton( 'Узнать о допуске' )
btnQualBad = KeyboardButton( 'Не узнавать о допуске' )
acceptQualification = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnQualGood, btnQualBad, btnMain)


#---tech Base---#

btnTechOrganized = KeyboardButton( 'Узнать о засекречивании' )
btnTechNonOraganized = KeyboardButton( 'Не узнавать о засекречивании' ) 
techBase = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized, btnTechNonOraganized, btnMain )

#---tech Base---#

btnTechOrganized1 = KeyboardButton( 'Узнать о пропускном режиме' )
btnTechNonOraganized1 = KeyboardButton( 'Не узнавать о пропускном режиме' ) 
techBase1 = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized1, btnTechNonOraganized1, btnMain )

#---tech Base---#

btnTechOrganized2 = KeyboardButton( 'Узнать об обеспечении режима' )
btnTechNonOraganized2 = KeyboardButton( 'Не узнавать об обеспечении режима' ) 
techBase2 = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized2, btnTechNonOraganized2, btnMain )

#---tech Base---#

btnTechOrganized3 = KeyboardButton( 'Узнать об обращении к носителям' )
btnTechNonOraganized3 = KeyboardButton( 'Не узнавать об обращении к носителям' ) 
techBase3 = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized3, btnTechNonOraganized3, btnMain )

#---tech Base---#

btnTechOrganized4 = KeyboardButton( 'Узнать о приёме' )
btnTechNonOraganized4 = KeyboardButton( 'Не узнавать об приёме' ) 
techBase4 = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized4, btnTechNonOraganized4, btnMain )

#---tech Base---#

btnTechOrganized5 = KeyboardButton( 'Узнать о делопроизводстве' )
btnTechNonOraganized5 = KeyboardButton( 'Не узнавать о делопроизводстве' ) 
techBase5 = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized5, btnTechNonOraganized5, btnMain )

#---tech Base---#

btnTechOrganized6 = KeyboardButton( 'Узнать о расследовании' )
btnTechNonOraganized6 = KeyboardButton( 'Не узнавать о расследовании' ) 
techBase6 = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized6, btnTechNonOraganized6, btnMain )

#---tech Base---#

btnTechOrganized7 = KeyboardButton( 'Да' )
btnTechNonOraganized7 = KeyboardButton( 'Нет' ) 
techBase7 = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized7, btnTechNonOraganized7, btnMain )
#---tech Base---#

btnTechOrganized8 = KeyboardButton( 'Да' )
btnTechNonOraganized8 = KeyboardButton( 'Нет' ) 
techBase8 = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized8, btnTechNonOraganized8, btnMain )



#---Complete---#

btnComplete = KeyboardButton( 'Завершить' )
completeMenu = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnComplete )

#---Organi---#

btnFDA = KeyboardButton( 'Федеральное дорожное агентство' )
btnFSB = KeyboardButton( 'ФСБ' )
btnGTK = KeyboardButton( 'ГосТехКомиссия' )
btnMVD = KeyboardButton( 'МВД' )
btnFSTEK = KeyboardButton( 'ФСТЭК' )
OrgansBTNS = ReplyKeyboardMarkup( resize_keyboard=True ).add(btnFDA, btnFSB, btnGTK, btnMVD, btnFSTEK, btnBack)


btnDopusk = KeyboardButton('Допуск к гос. тайне')
btnZasec = KeyboardButton('Засекречивание сведений')
btnPropusk = KeyboardButton('Организация пропускного режима')
btnRegime = KeyboardButton('Осуществление режима секретности')
btnNositel = KeyboardButton('Обращение с носителями')
btnPriem = KeyboardButton('Прием, сдача носиетелей')
btnDP = KeyboardButton('Ведение секретного делопроизводства')
btnRassled = KeyboardButton('Служебные расследования')
SubjectBTNS = ReplyKeyboardMarkup( resize_keyboard=True ).add(btnDopusk, btnZasec, btnPropusk, btnRegime, btnNositel, btnPriem, btnDP, btnRassled, btnBack)