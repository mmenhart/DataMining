import pandas as pd

data = pd.read_csv('test.csv')


def model(input):
    prediction = [[],[]]
    number = []
    pred = []
    for i in range(len(input)):
        if input.loc[i,'Sex'] == 'male':
            response = '0'
        elif input.loc[i,'Sex'] == 'female':
            if input.loc[i,'Pclass'] == '3:' and input.loc[i,'Embarked'] == 'S':
                response = '0'
            else:
                response = '1'

        temp_val = str(input.loc[i,'PassengerId'])

        # temp_val = temp_val + ',' + response

        prediction[0].append(temp_val)
        number.append(temp_val)
        prediction[1].append(response)
        pred.append(response)

    return prediction, number, pred


answer, numb, value = model(data)

file = open('submission.txt','w')
for i in answer:
    file.write(i)
    file.write('\n')

file.close()

full_data = list(zip(numb,value))

df = pd.DataFrame(data=full_data)

df.to_csv('titanic_predictions.csv',index=False,header=False)