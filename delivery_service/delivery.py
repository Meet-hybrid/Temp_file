def get_riders_wage(percentage):
	if percentage < 50:
		return percentage * 160 + 5000
	elif percentage >= 50 and percentage <= 59:
		return percentage * 200 + 5000	
	elif percentage >= 60 and percentage < 70:
		return percentage * 250 + 5000
	elif percentage >= 70 and percentage <= 100:
		return percentage * 500 + 5000
	
