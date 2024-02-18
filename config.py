# Don't Remove Credit @flstudiofruity
# Subscribe YouTube Channel For Amazing Bot @flstudiofruity
# Ask Doubt on telegram @flstudiofruity


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "14084834")

API_HASH = os.environ.get("API_HASH", "3370f5b5ed3ac5ad6931724413f529f6")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6569891735:AAGmrfy-CF3_scVWMPV8OSwwvWImbCAPihM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "flstudiofruity") 

             # Don't Remove Credit @flstudiofruity
             # Subscribe YouTube Channel For Amazing Bot flstudiofruity
             # Ask Doubt on telegram @flstudiofruity

DB_NAME = os.environ.get("DB_NAME", "filewizardpro")     

DB_URL = os.environ.get("DB_URL", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1602317498').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
