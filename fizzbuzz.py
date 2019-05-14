def fizzbuzz():
    for i in range(1, 101):
        if not i % 3:
            print('fizz')
        elif i % 5 :
            print('buzz')

        else:
            print(i)
