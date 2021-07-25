from pyrogram import Client
# Enable logging
import keyS
API_URL=None
_token=keyS.bot_token



api_id = keyS.api_id
api_hash = keyS.api_hash

adpp=Client("my_account", api_id, api_hash) 
async def re():
    async with adpp:
    	with open('session.txt','w') as f:
    		p=await adpp.export_session_string()
    		f.write(str(p))
     
 

if __name__ == '__main__':
    adpp.run(re())