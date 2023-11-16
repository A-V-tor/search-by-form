from wsgi import app

# пустой запрос
res = app.test_client().post('/get_form')
print('1) Запрос /get_form\n\nОтвет: ', res.text)

# запрос с совпадением шаблона в бд
res = app.test_client().post('/get_form?phone_check=+7 900 888 80 80&data_check=2023-10-10&desc_check=Description of this form&email_check=check@example.com')
print('\n\n2) Запрос /get_form?phone_check=+7 900 888 80 80&data_check=2023-10-10&desc_check=Description of this form&email_check=check@example.com\n\nОтвет: ', res.text)

# запрос без совпаденией с шаблоном в бд
res = app.test_client().post('/get_form?phone_check=900 888 80 80&data_check=2023-10-10&desc_check=Description of this form&email_check=check@example.com')
print('\n\n3) Запрос /get_form?phone_check=900 888 80 80&data_check=2023-10-10&desc_check=Description of this form&email_check=check@example.com\n\nОтвет: ', res.text)

# запрос с совпадением шаблона в бд и дополнительным номером телефона
res = app.test_client().post('/get_form?phone_check=+7 900 888 80 80&data_check=2023-10-10&desc_check=Description of this form&email_check=check@example.com&number=+7 700 700 70 70')
print('\n\n4) Запрос /get_form?phone_check=+7 900 888 80 80&data_check=2023-10-10&desc_check=Description of this form&email_check=check@example.com&number=+7 700 700 70 70\n\nОтвет: ', res.text)