i = raw_input ("Please state an integer \nYour integer is " )
try:
	int(i)
except ValueError:
	print "\n\n\n\n\n\n\nThat's not a number, I'm watching you! 0.0"

# Confirming it's a #
else:
	num = int(i) % 3
	numb = int(i) % 5
	if num == 0:
		print "Fizz"
		if numb == 0:
			print "FizzBuzz"
	else:
		if numb == 0:
			print "Buzz"
		else:
			print "\n\n\n\n\n\n\nYour number is pointless!"
