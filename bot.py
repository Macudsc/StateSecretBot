#import asyncio
from aiogram import Bot, Dispatcher, types,  executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import message
import markups as nav


BOT_TOKEN = "2113305271:AAGV6ReW77-yrSUo7KtfUIvwQ42TEH1kTyE"

bot = Bot( token = BOT_TOKEN )

dp = Dispatcher( bot = bot )



@dp.message_handler( commands = 'start' )
async def say_hello( event: types.Message ):
    notification_by_person.clear()
    user_answers.clear()
    await event.answer( f"Добрый день, { event.from_user.get_mention( as_html = True ) }, Вы обратились за помощью к боту-помшнику по обеспечению безопаснотсти! \n Вы готовы начать?",
        parse_mode = types.ParseMode.HTML, reply_markup = nav.startMeny
    )

@dp.message_handler( Text( equals = 'Приступим', ignore_case = True ), state = '*' )
async def first_type( event: types.Message, state: FSMContext ):
    notification_by_person.clear()
    user_answers.clear()
    await event.reply( f"Хорошо, { event.from_user.get_mention( as_html = True ) }, поехали... Выбери тип тайны", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.typesMeny
    )

user_answers = []


@dp.message_handler( Text( equals = 'Коммерческая тайна', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    notification_by_person.clear()
    user_answers.clear()
    user_answers.append( 'KT' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, ввели ли Вы режим коммерческой тайны?", parse_mode = types.ParseMode.HTML, 
                     reply_markup = nav.yourModeMeny
   )


@dp.message_handler( Text( equals = 'Нет, не ввел', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    user_answers.append( 'N' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, {do_help()}", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.completeMenu
    )

@dp.message_handler( Text( equals = 'Да, ввел', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    user_answers.append( 'Y' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, существует ли в вашем предприятии отдел взаимодействующий с коммерческой тайной?",  parse_mode = types.ParseMode.HTML,
                      reply_markup = nav.haveDepartament
    )


@dp.message_handler( Text( equals = 'Нет, не существует', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    user_answers.append( 'N' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, уверенны ли Вы в квалифицированности вашего персонала?", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.acceptQualification
    )


@dp.message_handler( Text( equals = 'Да, существует', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    user_answers.append( 'Y' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, уверенны ли Вы в квалифицированности вашего персонала?", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.acceptQualification
    )

@dp.message_handler( Text( equals = 'Сомневаюсь', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    user_answers.append( 'N' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, организована ли у Вас техническая база для защиты информации?", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.techBase
    )


@dp.message_handler( Text( equals = 'Да, уверен', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    user_answers.append( 'Y' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, организована ли у Вас техническая база для защиты информации?", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.techBase
    )


@dp.message_handler( Text( equals = 'Не уверен', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    user_answers.append( 'N' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, по результатам анализа ответов, мы предлагаем вам следущее: \n\n {do_help()}\n", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.completeMenu
    )


@dp.message_handler( Text( equals = 'База организована', ignore_case = True ), state = '*' )
async def second_type( event: types.Message, state: FSMContext ):
    user_answers.append( 'Y' )
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, по результатам анализа ответов, мы предлагаем вам следущее: \n\n {do_help()}\n", parse_mode = types.ParseMode.HTML,
                      reply_markup = nav.completeMenu
    )




if_mode_none = f"Введение режима коммерческой тайны - основополагающий этап! \n\n Для введения этого режима, Вам необходимо: \n 1) Определить перечень информации, которая является коммерческой тайной; \n 2) Установить порядок работы и контроля за соблдением режима коммерческой тайны; \n 3) Организовать учет лиц, получивших доступ к коммерческой тайне; \n 4) Нанести на носители информации соответсвующий гриф 'Коммерческая тайна' и указадать данные ее обладателя. \n "

if_havent_departament = f"Так как у Вас нет специального отдела, Вам необходимо: \n\n 1) Создать специальный отдел, который будет взаимодействовать с коммерческой тайной; \n 2) Назначить ответсвенного за обеспечение конфиденциальности; \n 3) Организовать кадровое делопроизводство (КДП); \n 4) Разработать и внедрить разрешительную систему доступа к информации. \n 5) Организовать цикл процессов УИБ и его работу. \n"

if_have_departament = f"Так как у Вас есть специальный отдел, Вам необходимо проверить: \n\n 1) Все ли нормативные акты введены в использование;  \n 2) Правильно ли установлено взаимодействие с отделом; \n 3) Назначен ли ответсвенный, обеспечивающий конфиденциальность;\n  4) Органзована ли система разрешительная система доступа к информации; \n 5) Органзовано ли кадровое делопроизводство (КДП). \n"

if_have_departament = f"Так как у Вас есть специальный отдел, Вам необходимо проверить: \n\n 1) Все ли нормативные акты введены в использование; \n 2) Правильно ли установлено взаимодействие с отделом; \n 3) Назначен ли ответсвенный, обеспечивающий конфиденциальность; \n 4) Органзована ли система разрешительная система доступа к информации; \n 5) Органзовано ли кадровое делопроизводство (КДП). \n"

if_qualification_bad = f"Если Вы сомневатесь в квалифицированности вашего персонала, то: \n\n 1) Необходимо проводить регулярные провервки соответсвия; \n 2) При приеме на работу, необходимо убедиться в опыте взаимодействия с конфиденциальной информацией у будущего сотрудника. В случае отсутствия таких навыков, провести разъяснительные беседы. \n"

if_qualification_good = f"Если Вы уверены в квалификации вашего персонала, то советуем: \n\n 1) Выдерживать благоприятные рабочие условия; \n 2) Не забывать проводить регулярные дополнительные проверки."

if_base_bad = f"Если Вы не уверены в организации вашей технической базы, то необходимо: \n\n 1) Установка технических средств защиты информации: \n\n *Защита рабочей станции; \n *Шлюз безопасности; \n *Программа контроля и управления доступом; \n *SIEM-система; \n *DLP-система; \n *IDS\IPS - система; \n *Программа доверительного удаления файлов. \n\n 2) Установка спец средств для защиты информации. \n"

if_base_good = f"Если Вы уверены в организации вашей технической базы, то: \n\n 1) Не забывайте своевременно обновлять ПО по мере выхода обновлений; \n 2) Не забывайте проводить анализ созданной системы безпасности с целью выявляения критических проблем; \n 3) Не забывайте обновлять специфичные средства безопасности по мере достижения срока выхода из эксплуатации."

do_check_act = f"Перечисленные рекомендации являются этапом планирования при создании безопасности для информации. Так как безопасность основа на цикле Деминга, то необходимо учесть еще 3 этапа: \n\n 1) 'DO': \n Вам необходимо запустить в реализации все этапы, названные на этапе планирования; \n Начать фиксировать сообщение от систем мониторинга, журналирования, логирования о неисправностях системы, ошибках, реализованных угрозах. \n\n 2)'CHECK': \n На основе аналитических данных, системных ответах, отчетах журналирования, необходимо оценить действенность предложенного плана защиты информации; \n Создать контрольный лист, в котором будут описаны незакрытые угрозы безопасности, фактические инциденты зарегестрированные системами; \n Предоставить контрольный лист отделу по реагированию на критические инциденты для прогнозирования и локализации дальнейшего развития инциденты и его последствий, получить отчет; \n Передать собранные сведения в отдел конфиденциального делопроизводства. \n\n 3) 'ACT': \n На основе собранных данных, внести правки в планирование организации безопасности коммерческой тайны и все подрядные; \n Передать новый план на этап планирования. \n "

doc_base = f"Все перечисленные рекомендации подготовлены на основе следующих нормативных документах: \n\n 1) 'Положение о коммерческой тайне': https://yar-ipoteka.ru/files/uploads/documenty/pers-dannye/Polozhenie-o-kommercheskoi-taine.pdf; \n 2) ФЗ-98 'О коммерческой тайне': http://ivo.garant.ru/#/document/12136454/paragraph/12089:0; \n 3) Методика определения угроз безопасности информации в информационных системах: https://fstec.ru/component/%20attachments/download/812; \n 4) 'ГОСТ Р 57580-1-2017 Безопасность финансовых (банковских) операций. Защита информации финансовых организаций. Базовый состав организационных и технических мер': https://internet-law.ru/gosts/gost/64887/. \n"

doc_base_if_mode_none = f"Все перечисленные рекомендации подготовлены на основе нормативного документа: \n\n ФЗ-98 'О коммерческой тайне': http://ivo.garant.ru/#/document/12136454/paragraph/12089:0. \n"

notification_by_person = []

def do_help():
    if user_answers[0] == 'KT':
        if user_answers[1] == 'N':
            return (f"{if_mode_none} \n\n{doc_base_if_mode_none}")
        if user_answers[1] == 'Y':
            if user_answers[2] == 'N':
                notification_by_person.append( if_havent_departament )
            if user_answers[2] == 'Y':
                notification_by_person.append( if_have_departament )
            if user_answers[3] == 'N':
                notification_by_person.append( if_qualification_bad )
            if user_answers[3] == 'Y':
                notification_by_person.append( if_qualification_good ) 
            if user_answers[4] == 'N':
                notification_by_person.append( if_base_bad )
            if user_answers[4] == 'Y':
                notification_by_person.append( if_base_good )
    notification_by_person.append( do_check_act )
    notification_by_person.append( doc_base )
    return (f"{notification_by_person[0]} \n\n{notification_by_person[1]} \n\n{notification_by_person[2]} \n\n{notification_by_person[3]} \n\n {notification_by_person[4]}")

        
            

@dp.message_handler( Text( equals = 'Вернуться в начало', ignore_case = True ), state = '*' )
async def retry( event: types.Message, state: FSMContext ):
    user_answers.clear()
    notification_by_person.clear()
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, давайте наченем сначала...", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.startMeny
    )

@dp.message_handler( Text( equals = 'Завершить', ignore_case = True ), state = '*' )
async def retry( event: types.Message, state: FSMContext ):
    user_answers.clear()
    notification_by_person.clear()
    await event.reply( f"{ event.from_user.get_mention( as_html = True ) }, спасибо, что воспользовались нашим помощником", parse_mode = types.ParseMode.HTML, 
                      reply_markup = nav.startMeny
    )


if __name__ == '__main__':
    executor.start_polling( dp )
    