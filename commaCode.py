
def list_to_string(list_value):
    result = []
    final_result = ''
    for i in range(len(list_value)):
        if len(list_value) > 0 and i == len(list_value) - 1:
            result.append('and ' + list_value[-1])
        else:
            result.append(list_value[i] + ', ')
            
    print(result)
    for j in result:
        final_result = final_result + j
    print(final_result) 
    return final_result

spam = ['apples', 'bananas', 'tofu', 'cats']
list_to_string(spam)
