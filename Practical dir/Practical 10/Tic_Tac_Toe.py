def initialize(size):
	game_state=dict()
	for i in range(1, size+1):
		game_state[i]=dict().fromkeys(range(1,size+1), " ")
	return game_state

def display_Layout(board):
	
		