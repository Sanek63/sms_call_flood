import requests
import random
import string

def send_for_titan(phone, fullName = "Киревичев Дмитрий Сергеевич"):
    for _ in range(1):
        request_timeout = 0.0000002
        phone1 = '+' + phone[0] + ' ' + '(' + phone[1] + phone[2] + phone[3] + ')' + " " + phone[4] + phone[5] + phone[
            6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
        phone2 = phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone[8] + phone[9] + \
                 phone[10]
        phone_stand = "+" + phone

        splitName = fullName.split(" ")


        try:
            requests.post("https://xn----dtbfcdjf3bhgadvu6dyfwb.xn--p1ai/buy-one-click?form&1586174241402",
                          {"d[0]": phone_stand,
                           "d[1]": "",
                           "d[2]": "Titan+Gel+интимный+гель-лубрикант+для+мужчин+(Оригинал)",
                           "d[3]": "https://xn----dtbfcdjf3bhgadvu6dyfwb.xn--p1ai/shop/product/titangel"})
        except:
            pass

        try:
            requests.post("https://ru-titan-gel.com/wp-content/themes/TitanGel/order.php",
                          {"sub1":"",
                           "sub2":"",
                           "sub3":"",
                           "sub4":"",
                           "sub5":"",
                           "name":[{"0": splitName[0] + " " + splitName[1] + " " + splitName[2]},{"1":"Оформить+заказ"}],
                           "phone": phone_stand[1:]
                           }
            )
        except:
            pass

        try:
            requests.post("https://vip-increase-gel.gorgeous-shop.com/order",
                          {
                              "name": splitName[0] + " " + splitName[1] + " " + splitName[2],
                              "phone": phone_stand
            })
        except:
            pass

        try:
            requests.post("https://greennutrashop.com/index.php?route=extension/module/oneclick/confirm",
                          {
                              "quantity": "1",
                              "name": splitName[1],
                              "telephone": phone_stand,
                              "product_id": "341"
                          })
        except:
            pass

        try:
            requests.post("https://aptekapoisk.net/ajax/ctr.php",
                          {
                              "pid":"232",
                              "sub_id":"return",
                              "site_id":"53",
                              "name":splitName[1],
                              "phone_cod":"7",
                              "phone":phone_stand[2:]
                          })
        except:
            pass
