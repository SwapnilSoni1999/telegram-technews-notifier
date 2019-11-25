import time
from sites import (
                beebom, 
                digit, 
                gadgetsnow, 
                gizmodo, 
                androidauthority, 
                xda,
                techradar,
                bgr,
                hexus,
                gsmarena
            )
from service import telegram
import random

# initiate all sites
beebom = beebom.Beebom()
digit = digit.Digit()
gadgetsnow = gadgetsnow.GadgetsNow()
gizmodo = gizmodo.Gizmodo()
androidauthority = androidauthority.AndroidAuthority()
xda = xda.XDA()
techradar = techradar.TechRadar()
bgr = bgr.BGR()
hexus = hexus.Hexus()
gsmarena = gsmarena.GSMArena()

print('Starting Watch on Websites...')
telegram.sendMessage('Starting Watch on Websites...')

# get all posts from all sites
beebom_post = beebom.latest_post()
digit_post = digit.latest_news()
gadgetsnow_post = gadgetsnow.get_latest_news()
gizmodo_post = gizmodo.latest_post()
androidauthority_post = androidauthority.latest_news()
xda_post = xda.latest_post()
techradar_post = techradar.latest_news()
bgr_post = bgr.latest_post()
hexus_post = hexus.latest_news()
gsmarena_post = gsmarena.latest_post()

print('Service Started!')
telegram.sendMessage('Started Service!')

while True:
    # Beebom
    new_post_beebom = beebom.latest_post()
    if new_post_beebom['time'] > beebom_post['time']:
        print('Found new post on Beebom!', new_post_beebom)
        beebom_post = new_post_beebom
        telegram.send_alert('Beebom', new_post_beebom['title'], new_post_beebom['url'])
    else:
        print('No new post found on beebom')

    # Digit
    curr_title = digit_post['title']
    new_post_digit = digit.latest_news()
    if curr_title != new_post_digit['title']:
        print('New Post found on digit!', new_post_digit)
        digit_post = new_post_digit
        telegram.send_alert('Digit', new_post_digit['title'], new_post_digit['url'])
    else:
        print('No new post found on digit')

    # GadgetsNow
    new_post_gn = gadgetsnow.get_latest_news()
    if new_post_gn['time'] > gadgetsnow_post['time']:
        print('New post found on Gadgets Now', new_post_gn)
        gadgetsnow_post = new_post_gn
        telegram.send_alert('GadgetsNow', new_post_gn['title'], new_post_gn['url'])
    else:
        print('No new post found on GadgetsNow!')

    # GizModo
    new_post_gizmodo = gizmodo.latest_post()
    if new_post_gizmodo['title'] != gizmodo_post['title']:
        print('New post found on GizModo!', new_post_gizmodo)
        gizmodo_post = new_post_gizmodo
        telegram.send_alert('GizModo', new_post_gizmodo['title'], new_post_gizmodo['url'])
    else:
        print('No new post found on GizModo')

    # AndroidAuthority
    new_post_androidauthority = androidauthority.latest_news()
    if new_post_androidauthority['title'] != androidauthority_post['title']:
       print('New post found on AndroidAuthority!', new_post_androidauthority)
       androidauthority_post = new_post_androidauthority
       telegram.send_alert('AndroidAuthority', new_post_androidauthority['title'], new_post_androidauthority['url'])
    else:
       print('No new post found on AndroidAuthority!')

    # xda-developers
    new_post_xda = xda.latest_post()
    if new_post_xda['title'] != xda_post['title']:
        print('New post found on xda-developers!', new_post_xda)
        xda_post = new_post_xda
        telegram.send_alert('xda-developers', new_post_xda['title'], new_post_xda['url'])
    else:
        print('No new post found on xda-developers')

    # TechRadar
    new_post_techradar = techradar.latest_news()
    if new_post_techradar['title'] != techradar_post['title']:
        print('New post found on TechRadar!', new_post_techradar)
        techradar_post = new_post_techradar
        telegram.send_alert('TechRadar', new_post_techradar['title'], new_post_techradar['url'])
    else:
        print('No new post found on TechRadar')
    
    # BGR
    new_post_bgr = bgr.latest_post()
    if new_post_bgr['title'] != bgr_post['title']:
        print('New post found on BGR!', new_post_bgr)
        bgr_post = new_post_bgr
        telegram.send_alert('BGR', new_post_bgr['title'], new_post_bgr['url'])
    else:
        print('No new post found on BGR!')

    # Hexus
    new_post_hexus = hexus.latest_news()
    if new_post_hexus['title'] != hexus_post['title']:
        print('New post found on Hexus!', new_post_hexus)
        hexus_post = new_post_hexus
        telegram.send_alert('Hexus', new_post_hexus['title'], new_post_hexus['url'])
    else:
        print('No new post found on Hexus')

    # GSMArena
    new_post_gsmarena = gsmarena.latest_post()
    if new_post_gsmarena['title'] != gsmarena_post['title']:
        print('New post found on GSMArena!', new_post_gsmarena)
        gsmarena_post = new_post_gsmarena
        telegram.send_alert('GSMArena', new_post_gsmarena['title'], new_post_gsmarena['url'])
    else:
        print('No new post found on GSMArena!')

    time.sleep(random.randint(60,100))
    
