# the sum of the squares of positive odd integers less than 16
q0 =    reduce(lambda x, y: x + y, 
            map(lambda x: x * x, 
                filter(lambda x: x % 2 == 1, range(16))))

assert q0 == 1*1 + 3*3 + 5*5 + 7*7 + 9*9 + 11*11 + 13*13 + 15*15

# the product of odd squares of positive integers less than 16
q1 =    reduce(lambda x, y: x * y,
            filter(lambda x: x % 2 == 0,
                map(lambda x: x * x, range(16))))

assert q1 == 1 * 8 * 25 * 49 * 81 * 121 * 169 * 225

def vowel_words(sentence):
    split = sentence.split(' ')
    for word in split:
        if word[0] in 'aeiou':
            yield word

euclidian_distance = lambda w, v: sum(((wi - vi)**2 for wi,vi in zip(w,v)))**.5 

