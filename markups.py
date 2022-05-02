from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#---Hello---#

btnStart = KeyboardButton( 'Приступим' )
startMeny = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnStart )


#---Rerutn---#

btnMain = KeyboardButton( 'Вернуться в начало' ) 

#---Commercy Menu---#

btnCom = KeyboardButton( 'Коммерческая тайна' )
typesMeny = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnCom, btnMain )

#---U Mode Menu---#

btnYourMode_is_false = KeyboardButton( 'Нет, не ввел' )
btnYourMode_is_True = KeyboardButton( 'Да, ввел' )
yourModeMeny = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnYourMode_is_True, btnYourMode_is_false, btnMain )

#---Have Departament---#

btnHave = KeyboardButton( 'Да, существует' )
btnHavent = KeyboardButton( 'Нет, не существует' )
haveDepartament = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnHave, btnHavent, btnMain )  

#---accept Qalification---#

btnQualGood = KeyboardButton( 'Да, уверен' )
btnQualBad = KeyboardButton( 'Сомневаюсь' )
acceptQualification = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnQualGood, btnQualBad, btnMain)


#---tech Base---#

btnTechOrganized = KeyboardButton( 'База организована' )
btnTechNonOraganized = KeyboardButton( 'Не уверен' ) 
techBase = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnTechOrganized, btnTechNonOraganized, btnMain )

#---Complete---#

btnComplete = KeyboardButton( 'Завершить' )
completeMenu = ReplyKeyboardMarkup( resize_keyboard=True ).add( btnComplete )