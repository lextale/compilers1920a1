"""
Κώδικας που θα χρησιμοποιηθεί ως βάση για την 1η εργασία
των Μεταγλωττιστών (αναγνώριση κειμένου μέσω αυτομάτου DFA).

ΠΡΟΣΟΧΗ: Προσθήκες στον κώδικα επιτρέπονται μόνο
στα σημεία (Α), (Β) και (Γ) - διαβάστε τα σχόλια!
"""


transitions = { 

	# (Α) Συμπληρώστε τον πίνακα μεταβάσεων ως λεξικό (dictionary).
	# Η αρχική κατάσταση πρέπει να ονομάζεται 's0'.
	# Για λεπτομέρειες δείτε στο:
	# http://mixstef.github.io/courses/compilers/lecturedoc/unit1/module1.html#id7
	
	's0':{'DIGIT':'s1', '.':'s3', '0':'s5'},
	's1':{'0':'s1', 'DIGIT':'s1', '.':'s2'},
	's2':{'0':'s2', 'DIGIT':'s2'},
	's3':{'0':'s4', 'DIGIT':'s4'},
	's4':{'0':'s4', 'DIGIT':'s4'},
	's5':{'.':'s6'},
	's6':{'0':'s7', 'DIGIT':'s7'},
	's7':{'0':'s7', 'DIGIT':'s7'}
	} 


accepts = { 

	# (Β) Συμπληρώστε το λεξικό των καταστάσεων αποδοχής και των
	# αντίστοιχων επιστρεφόμενων συμβόλων (tokens)
	# Για λεπτομέρειες δείτε στο:
	# http://mixstef.github.io/courses/compilers/lecturedoc/unit1/module1.html#id8
	
	's2':'FLOAT_TOKEN',
	's4':'FLOAT_TOKEN',
	's7':'FLOAT_TOKEN'

     	  }


def get_char(text,pos):
	""" Returns char (or char category) at position `pos` of `text`,
	or None if out of bounds. """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# (Γ) Προαιρετικά, μπορείτε να ομαδοποιήσετε τους
	# χαρακτήρες εισόδου εδώ.
	# Για λεπτομέρειες δείτε στο:
	# http://mixstef.github.io/courses/compilers/lecturedoc/unit1/module1.html#id11
	
	if c>'0' and c<='9':
		return 'DIGIT'
	
	return c
	

# Δεν επιτρέπεται η παρέμβαση στον κώδικα από αυτό το σημείο και κάτω! 

def scan(text,transitions,accepts,state):
	""" Starting from inital `state`, scans `text` while transitions
	exist in `transitions` dict. After that, if on a state belonging to
	`accepts` dict, returns the corresponding token object, else None.
	"""
	
	# initial position on text
	pos = 0
	
	# memory object for last seen accepting state
	matched = None
	
	while True:
		
		c = get_char(text,pos)	# get next char (or char category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char			

			# remember if current state is accepting
			if state in accepts:
				matched = { 'token':  accepts[state],
					    'lexeme': text[:pos] }
			
		else:	# no transition found, return last match or None
			return matched
			

# testing inputs
for test in ['12.456','6789.','.66998','1234','.']:
	m = scan(test,transitions,accepts,'s0')
	print("Testing '{}'\nResult: {}\n".format(test,m))


