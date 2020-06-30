#We can use "if statements" to run code based on specific conditions
temperature = 80
#The print statement will only print if the temperature value is greater than 75
if temperature > 75:
  print ('It is time to go to the beach!')

#When we use an if statement, we put a colon at the end, and then all of the lines that will run when the if statement is true should be indented the same amount
#All of the indented lines are called a block of code

#Try changing temperature to 81 to see the block of code below run
if temperature > 80:
  print('I need a slushie!')
  print('And an ice cream sandwich.')

#What happens when the code below is run?
if temperature > 80:
  print('I need a slushie!')
print('And an ice cream sandwich.')

#The code below will give an 'IndentationError: unexpected indent' if you uncomment the second print statement because there is an extra space on that line, making it not line up with the rest of the code block
if temperature > 80:
  print('I need a slushie!')
  print('And a popsicle')
  # print('And an ice cream sandwich.')