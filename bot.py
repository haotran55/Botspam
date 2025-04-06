#Không hiểu về code xem kĩ video
import telebot
import datetime
import time
import os
import re
import subprocess
import requests
import sys
from keep_alive import keep_alive
#Điền bot token của bạn
bot_token = '7949863057:AAETRiCemVJk4lsb2-Y_7KEVzE5fsfZ0Jd4'
bot = telebot.TeleBot(bot_token)
#Điền id tele của mình
processes = []
ADMIN_ID = '7658079324'

def TimeStamp():
    return str(datetime.date.today())

def get_user_file_path(user_id):
    today_day = datetime.date.today().day
    user_dir = f'./user/{today_day}'
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    return f'{user_dir}/{user_id}_key.txt'

def is_key_expired(user_id):
    file_path = get_user_file_path(user_id)
    if not os.path.exists(file_path):
        return True
    with open(file_path, 'r') as f:
        timestamp = f.read().strip()
    try:
        key_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d')
    except ValueError:
        return True
    return (datetime.datetime.now() - key_time).days >= 1

@bot.message_handler(commands=['getkey'])
def startkey(message):
    user_id = message.from_user.id
    today_day = datetime.date.today().day
    key = "haoesport" + str(user_id * today_day - 2007)

    api_token = '67c1fe72a448b83a9c7e7340'
    key_url = f"https://dichvukey.site/key.html?key={key}"

    try:
        response = requests.get(f'https://link4m.co/api-shorten/v2?api={api_token}&url={key_url}')
        response.raise_for_status()
        url_data = response.json()
        print(key)

        if 'shortenedUrl' in url_data:
            url_key = url_data['shortenedUrl']
            text = (f'Link Lấy Key Ngày {TimeStamp()} LÀ: {url_key}\n'
                    'KHI LẤY KEY XONG, DÙNG LỆNH /key vLongzZxXxx ĐỂ TIẾP TỤC Hoặc /muavip đỡ vượt tốn thời gian nhé')
            bot.reply_to(message, text)
        else:
            bot.reply_to(message, 'Lỗi.')
    except requests.RequestException:
        bot.reply_to(message, 'Lỗi.'

@bot.message_handler(commands=['key'])
def key(message):
    if len(message.text.split()) != 2:
        bot.reply_to(message, 'Key Đã Vượt Là? đã vượt thì nhập /key chưa vượt thì /muavip nhé')
        return

    user_id = message.from_user.id
    key = message.text.split()[1]
    today_day = datetime.date.today().day
    expected_key = "haoesport" + str(user_id * today_day - 2007)  # Đảm bảo công thức khớp với công thức tạo key

    if key == expected_key:
        text_message = f'<blockquote>[ KEY HỢP LỆ ] NGƯỜI DÙNG CÓ ID: [ {user_id} ] ĐƯỢC PHÉP ĐƯỢC SỬ DỤNG CÁC LỆNH TRONG [/help]</blockquote>'
        video_url = 'https://v16m-default.akamaized.net/4e91716006f611b4064fb417539f7a57/66a9164c/video/tos/alisg/tos-alisg-pve-0037c001/o4VRzDLftQGT9YgAc2pAefIqZeIoGLgGAFIWtF/?a=0&bti=OTg7QGo5QHM6OjZALTAzYCMvcCMxNDNg&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=2138&bt=1069&cs=0&ds=6&ft=XE5bCqT0majPD12fFa-73wUOx5EcMeF~O5&mime_type=video_mp4&qs=0&rc=PGloZWg2aTVoOGc7OzllZkBpanA0ZXA5cjplczMzODczNEAtXmAwMWEyXjUxNWFgLjYuYSNxZ3IyMmRrNHNgLS1kMS1zcw%3D%3D&vvpl=1&l=20240730103502EC9CCAF9227AE804B708&btag=e00088000'  # Đổi URL đến video của bạn
        bot.send_video(message.chat.id, video_url, caption=text_message, parse_mode='HTML')
        
        user_path = f'./user/{today_day}'
        os.makedirs(user_path, exist_ok=True)
        with open(f'{user_path}/{user_id}.txt', "w") as fi:
            fi.write("")
    else:
        bot.reply_to(message, 'KEY KHÔNG HỢP LỆ.')



@bot.message_handler(commands=['superspam'])
def superspam(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./vip/{user_id}.txt"):
        bot.reply_to(message, 'Đăng Kí Vip Đi Rẻ Lắm😭')
        return
    with open(f"./vip/{user_id}.txt") as fo:
        data = fo.read().split("|")
    past_date = data[0].split('-')
    past_date = datetime.date(int(past_date[0]), int(past_date[1]), int(past_date[2]))
    today_date = datetime.date.today()
    days_passed = (today_date - past_date).days
    if days_passed < 0:
        bot.reply_to(message, 'Key Vip Cài Vào ngày khác')
        return
    if days_passed >= int(data[1]):
        bot.reply_to(message, 'Key Vip Hết Hạn Mua Típ Đi😪')
        os.remove(f"./vip/{user_id}.txt")
        return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI')
        return
    if len(message.text.split()) == 2:
        bot.reply_to(message, 'Thiếu dữ kiện !!!')
        return
    lap = message.text.split()[2]
    if lap.isnumeric():
        if not (1 <= int(lap) <= 30):
            bot.reply_to(message, "Spam Không Hợp Lệ Chỉ Spam Từ 1-30 Lần🚨")
            return
    lap = message.text.split()[2]
    if not lap.isnumeric():
        bot.reply_to(message, "Sai dữ kiện !!!")
        return
    phone_number = message.text.split()[1]
    if not re.search(r"^(?:\+84|0)(3[2-9]|5[6-9]|7[0-9]|8[0-689]|9[0-4])[0-9]{7}$", phone_number):
        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return
    if phone_number in ["0528300000"]:
        bot.reply_to(message, "Spam cái đầu buồi tao huhu")
        return
    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
    bot.reply_to(message, f'🌠 Tấn Công Thành Công 🌠 \n+ Bot 👾: smsdevsp_bot \n+ Số Tấn Công 📱: [ {phone_number} ]\n+ Lặp lại : {lap}\n+ Admin 👑: Đoàn LongThành\n+ Tiktok : DoanLongThanh_15\n+ Key : vip')

@bot.message_handler(commands=['spam'])
def spam(message):
    user_id = message.from_user.id
    if not os.path.exists(get_user_file_path(user_id)):
        bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
        return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI')
        return
    if len(message.text.split()) == 2:
        bot.reply_to(message, 'Thiếu dữ kiện !!!')
        return
    lap = message.text.split()[2]
    if lap.isnumeric():
        if not (1 <= int(lap) <= 10):
            bot.reply_to(message, "Spam Không Hợp Lệ Chỉ Spam Từ 1-10 Lần🚨")
            return
    else:
        bot.reply_to(message, "Sai dữ kiện !!!")
        return
    phone_number = message.text.split()[1]
    if not re.search(r"^(?:\+84|0)(3[2-9]|5[6-9]|7[0-9]|8[0-689]|9[0-4])[0-9]{7}$", phone_number):
        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return
    if phone_number in ["0528300000"]:
        bot.reply_to(message, "Spam cái đầu buồi tao huhu")
        return
    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
    bot.reply_to(message, f'🌠 Tấn Công Thành Công 🌠 \n+ Bot 👾: smsdevsp_bot \n+ Số Tấn Công 📱: [ {phone_number} ]\n+ Lặp lại : {lap}\n+ Admin 👑: Đoàn LongThành\n+ Tiktok : DoanLongThanh_15\n+ Key : free')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """<blockquote>
Danh sách lệnh:
┌───────────────⭓ 
│• /getkey: Lấy Key Dùng Lệnh🔑
│• /key {key}: Nhập key Thường🔒
│• /spam : Spam free📱
│• /superspam : SpamVip🎗️
│• /help: Danh sách lệnh📄
│• /status : Admin
│• /restart : Admin
│• /stop : Admin
│• /them : Admin
└────────────────
</blockquote>""", parse_mode='HTML')


@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Làm Cái Trò Gì Zậy😀')
        return
    process_count = len(processes)
    bot.reply_to(message, f'Số quy trình đang chạy: {process_count}.')

@bot.message_handler(commands=['restart'])
def restart(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Làm Cái Trò Gì Zậy😀')
        return
    bot.reply_to(message, 'Bot sẽ được khởi động lại trong giây lát...')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.message_handler(commands=['stop'])
def stop(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Làm Cái Trò Gì Zậy😀')
        return
    bot.reply_to(message, 'Bot sẽ dừng lại trong giây lát...')
    time.sleep(2)
    bot.stop_polling()

@bot.message_handler(commands=['them'])
def them(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Làm Cái Trò Gì Zậy😀')
        return
    try:
        idvip = message.text.split()[1]
        ngay = message.text.split()[2]
        hethan = message.text.split()[3]
        with open(f"./vip/{idvip}.txt", "w") as fii:
            fii.write(f"{ngay}|{hethan}")
        bot.reply_to(message, f'Thêm Thành Công {idvip} Làm Vip')
    except IndexError:
        bot.reply_to(message, 'Vui lòng cung cấp đủ thông tin: /them <idvip> <ngay> <hethan>')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Lệnh Không Hợp lệ Vui Lòng Ghi /help để xem các lệnh📄')

# Kích hoạt web server keep_alive
keep_alive()

# Chạy bot
print("Bot đang chạy...")
bot.polling()
