# Module 3 Assignment
#Eugene Bellau

file = open("question.txt","r+")

question = file.read()

response = input(question)

file.write(response)

file.close()




