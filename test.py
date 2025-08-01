# addition
def addition(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.") 

addition(5, 10)
addition(20, 30)
addition(7.5, 2.5)
# game

# def menu(list, question):
#     for entry in list:
#        print(1 + list.index(entry),end="")
#         print (") " + entry)

#    return eval(input(question))

# items = ["blanket","painting","vase","suitcases","clothes","cabinets","frames","empty_bottles"]


# loop = 1

# #Give some introductary text:
# print("you went to the store room to find an old painting, but due to somereason the door closed as soon as you entered.")

# print("Now, you find yourself locked in the store. You don't know how to escape ")
# print("you find a paper saying: to escape this room check the places listed to find the final clue.")
# print(len(items), "things:")
# for x in items:
#     print(x)
# print("")
# print("The door is locked. Could there be a key somewhere?")

# while loop == 1:
#     choice = menu(items,"What do you want to inspect? ")
#     if choice == 1:
#         print("You found the word :The.")
#         print("")
#     elif choice == 2:
#         print("You found nothing behind the painting.")
#         print("")
#     elif choice == 3:
#         print("You found the word : key.")
#         print("")
#     elif choice == 4:
#         print("You found the word :is .")
#         print("")
#     elif choice == 5:
#         print("You found the word : under.")
#         print("")
#     elif choice == 6:
#         print("You found the word : the.")
#         print("")
#     elif choice == 7:
#         print("You found the word : door.")
#         print("")
#     elif choice == 8:
#         print("You found the word : matt.")
#         print("")
#     elif choice == 9:
#         loop = 0
#         print(" ")
#     else:
#         #print("Choice is :", choice)
#         print("The door is locked, you need to find a key.")
#         print("")
       
# print("as soon as you put in the key and the door opens \
# you start to get excited and relived. ")





# def greet(name):
#     print("Hello, %s" % name)
#     print("It's great to see you %s" % name)
#     print("Have a fantastic day %s \n" % name)

# people = ["Alice", "Bob", "Charlie"]

# for person in people:
#     greet(person)





#     def full_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     print(f"Hello, {full_name}.")

# full_name("Alice","Brown")
# full_name("Jessica","Winter")
# full_name("Natsaha","John")





# def addition(num1, num2):
#     result = num1 + num2
#     print(f"The sum of {num1} and {num2} is {result}.") 

# addition(5, 10)
# addition(20, 30)
# addition(7.5, 2.5)
    
# def return_addition(number1, number2):
#     return number1 + number2

# number1, number2 = 2, 5
# result1 = return_addition(number1, number2)
# print(f"The sum of {number1} and {number2} is {result1}")

# number1, number2 = 10, 5
# result2 = return_addition(number1, number2)
# print(f"The sum of {number1} and {number2} is {result2}")

# number1, number2 = 13, 5
# result3 = return_addition(number1, number2)
# print(f"The sum of {number1} and {number2} is {result3}")






# def apply_discount(total, code):
#     if code == 'save10':
#         return total * 0.9
#     elif code == 'HALFOFF':
#         return total *0.5
#     else:
#         return total

# total_amount = 1500
# discounted_total_1 = apply_discount(total_amount, 'save10')
# print('Total after SAVE10 discount: ${:.2f}'.format(discounted_total_1))
# discounted_total_2 = apply_discount(total_amount,'HALFOFF')
# print('Total after HALFOFF discount: ${:.2f}'.format(discounted_total_2))
# discounted_total_3 = apply_discount(total_amount, 'INVALID')
# print('Total with no discount: ${:.2f}'.format(discounted_total_3))




# def order_summary(order):
#     print("Order Summary:")
#     total_items = 0
    
#     for item, quantity in order.items():
#         print(item, quantity)
#         total_items += quantity

#     print("Total items", total_items)

# order = {
#     "Plums": 2,
#     "Bananas": 2,
#     "Oranges": 5,
#     "Mangoes": 2
# }
# order_summary(order)





# from openai import OpenAI

# OPENAI_API_KEY = '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'

# client = OpenAI(api_key=OPENAI_API_KEY)
# prompt = "Hi, can you tell me a joke?"
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": prompt}]
# )

# print(response)
# # Extract the AI's response from the API result
# reply = response.choices[0].message.content.strip()


# # Show both sides of the conversation
# print("Prompt:", prompt)
# print("Response:", reply)