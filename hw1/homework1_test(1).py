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

string3 = 'a'
ans3 = compute_max_word_length(string3)
print 'test 3\nyour answer:\t', ans3, '\ncorrect answer:\t a'

string4 = ''
ans4 = compute_max_word_length(string4)
print 'test 4\nyour answer:\t', ans4, '\ncorrect answer:\t '

string5 = 'good molly miss golly'
ans5 = compute_max_word_length(string5)
print 'test 5\nyour answer:\t', ans5, '\ncorrect answer:\t molly'

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

c1 = (0,0)
c2 = (0, 0)
ans3 = manhattan_distance(c1, c2)
print 'test 3\nyour answer:\t', ans3, '\ncorrect answer:\t 0'

d1 = (-100, -1)
d2 = (-200, -1)
ans4 = manhattan_distance(d1, d2)
print 'test 4\nyour answer:\t', ans4, '\ncorrect answer:\t 100'


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

c1 = collections.Counter('abcddddefggg')
c2 = collections.Counter('aaaccchyyyyyyyyyy')
ans3 = sparse_vector_dot_product(c1, c2)
print 'test 3\nyour answer:\t', ans3, '\ncorrect answer:\t 6'


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

string3 = '(8*(a+5)-4)/6'
ans3 = correct_parentheses(string3)
print "test 3\nyour answer:\t", ans3, "\ncorrect answer:\t True"

string4 = '8*(a+5)-4)/6'
ans4 = correct_parentheses(string4)
print "test 4\nyour answer:\t", ans4, "\ncorrect answer:\t False"

############################################################
# Problem 1f

print '\nTesting Problem 1f\n'

string1 = '(())'
ans1 = nested_parentheses(string1)
print "test 1\nyour answer:\t", ans1, "\ncorrect answer:\t True"

string2 = '(((x))'
ans2 = nested_parentheses(string2)
print "test 2\nyour answer:\t", ans2, "\ncorrect answer:\t False"

string3 = '(((()))))'
ans3 = nested_parentheses(string3)
print "test 3\nyour answer:\t", ans3, "\ncorrect answer:\t False"

string4 = ''
ans4 = nested_parentheses(string4)
print "test 4\nyour answer:\t", ans4, "\ncorrect answer:\t True"