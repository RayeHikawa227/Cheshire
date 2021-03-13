#Events
@cheshire.event
async def on_ready():
	print('Logged in as')
	print('Cheshire')
	print('made by XyleN5967')

@cheshire.event
async def on_member_join(member):
	print(f'{member} has landed on the server')

@cheshire.event
async def on_member_remove(member):
	print(f'{member} has left on the server') 
	
@cheshire.event
async def on_member_ban(member):
	print(f'{member} has banned on the server') 
