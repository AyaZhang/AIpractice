from practice import *

############################################################
# Problem 1a

print 'Testing Problem 1a\n'

string1 = 'Mary had a little lamb'
ans1 = compute_max_word_length(string1)
print 'test 1\nyour answer:\t', ans1, '\ncorrect answer:\t little'

string2 = 'good golly miss molly'
ans2 = compute_max_word_length(string2)
print 'test 2\nyour answer:\t', ans2, '\ncorrect answer:\t molly'

############################################################
# Problem 1b

print '\nTesting Problem 1b\n'

a1 = (3,5)
a2 = (-4,10)
ans1 = manhattan_distance(a1, a2)
print 'test 1\nyour answer:\t', ans1, '\ncorrect answer:\t 12'

b1 = (0,100)
b2 = (-100, -1)
ans2 = manhattan_distance(b1, b2)
print 'test 2\nyour answer:\t', ans2, '\ncorrect answer:\t 201'

############################################################
# Problem 1c

print '\nTesting Problem 1c\n'

a1 = collections.Counter('aaabbbcccd')
a2 = collections.Counter('bcdd')
ans1 = sparse_vector_dot_product(a1, a2)
print 'test 1\nyour answer:\t', ans1, '\ncorrect answer:\t 8'

b1 = collections.Counter('abcdefg')
b2 = collections.Counter('aaabbbcccf')
ans2 = sparse_vector_dot_product(b1, b2)
print 'test 2\nyour answer:\t', ans2, '\ncorrect answer:\t 10'

############################################################
# Problem 1d

print '\nTesting Problem 1d\n'

string1 = 'bad bad not good'
ans1 = compute_most_frequent_word(string1)
print "test 1\nyour answer:\t", ans1, "\ncorrect answer:\t (set(['bad']), 2)"

string2 = 'really really really bad bad bad'
ans2 = compute_most_frequent_word(string2)
print "test 2\nyour answer:\t", ans2, "\ncorrect answer:\t (set(['bad', 'really']), 3)"


############################################################
# Problem 1e

print '\nTesting Problem 1e\n'

string1 = '(a+b)*c'
ans1 = correct_parentheses(string1)
print "test 1\nyour answer:\t", ans1, "\ncorrect answer:\t True"

string2 = '((a+b)'
ans2 = correct_parentheses(string2)
print "test 2\nyour answer:\t", ans2, "\ncorrect answer:\t False"
"""
############################################################
# Problem 1f

print '\nTesting Problem 1f\n'

string1 = '(())'
ans1 = nested_parentheses(string1)
print "test 1\nyour answer:\t", ans1, "\ncorrect answer:\t True"

string2 = '(((x))'
ans2 = nested_parentheses(string2)
print "test 2\nyour answer:\t", ans2, "\ncorrect answer:\t False"
"""
