from telethon.sync import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, TogglePreHistoryHiddenRequest, InviteToChannelRequest, EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.errors import SessionPasswordNeededError
from datetime import datetime
import asyncio
import os  

api_id = 27692725
api_hash = 'c4069ea0a7e03e277e3a9e24b6e5f565'
phone = '+998334438384'

client = TelegramClient('my_session', api_id, api_hash)

BOT_USERNAMES = ['sokmang_bot', 'JoinDelBot', 'TozaIovchi_Bot']


async def login():
    await client.connect()
    if not await client.is_user_authorized():
        print("📲 Telegram raqamingizga kod yuborildi.")
        await client.send_code_request(phone)
        code = input("✉️ KOD: ")
        try:
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            password = input("🔑 Telegram parolingiz (2FA): ")
            await client.sign_in(password=password)
    else:
        print("✅ Allaqachon avtorizatsiya qilingan.")

async def create_supergroup():
    now = datetime.now()
    group_name = f"SupperGuruh {now.strftime('%Y-%m-%d-%H-%M-%S')}"

    # Superguruh yaratish
    result = await client(CreateChannelRequest(
        title=group_name,
        about="Auto-created group",
        megagroup=True
    ))

    group = result.chats[0]
    print(f"✅ Guruh yaratildi: {group.title} (ID: {group.id})")

    # ➕ Faylga guruh nomi va ID yozish
    save_dir = "2025"
    os.makedirs(save_dir, exist_ok=True)
    with open(f"{save_dir}/guruhlar.txt", "a", encoding="utf-8") as file:
        file.write(f"Guruh nomi: {group.title}\n")
        file.write(f"Guruh ID: {group.id}\n")
        file.write("-" * 30 + "\n")

    # Chat tarixini ko‘rsatish (ochish)
    try:
        await client(TogglePreHistoryHiddenRequest(
            channel=group,
            enabled=False
        ))
        print("📜 Chat tarixi ochiq qilindi.")
    except Exception as e:
        if "wasn't modified" in str(e):
            print("ℹ️ Chat tarixi allaqachon ochiq.")
        else:
            print(f"⚠️ Chat tarixini ochishda xatolik: {e}")

    # Botlarni qo‘shish
    try:
        bot_users = [f"@{bot}" for bot in BOT_USERNAMES]
        await client(InviteToChannelRequest(channel=group, users=bot_users))
        print("🤖 Botlar guruhga qo‘shildi.")
    except Exception as e:
        print(f"⚠️ Botlarni qo‘shishda xatolik: {e}")

    # Admin huquqlari
    rights = ChatAdminRights(
        post_messages=True,
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=False,
        delete_messages=True,
        pin_messages=True,
        edit_messages=True
    )

    # Har bir botni admin qilish
    for bot in BOT_USERNAMES:
        try:
            await client(EditAdminRequest(
                channel=group,
                user_id=f"@{bot}",
                admin_rights=rights,
                rank="BotAdmin"
            ))
            print(f"✅ @{bot} admin qilindi.")
        except Exception as e:
            print(f"⚠️ @{bot}ni admin qilishda xatolik: {e}")

async def main():
    await login()  # loginni alohida bajarish
    while True:
        await create_supergroup()
        await asyncio.sleep(10)

with client:
    client.loop.run_until_complete(main())
