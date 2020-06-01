# These are Py4E autograder assignments. 

# Exercise 2.3
hrs = input("Enter Hours:")
rte = input("Enter Rate per Hour:")
hours = float(hrs)
rate = float(rte)
pay = hours * rate
print ("Pay:", pay)

# Exercise 3.1
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40 :
    pay = 40*r + (1.5*r*(h-40))
    print(pay)
else :
    print(h*r)
    
# Exercise 3.3
score = input("Enter Score: ")
pe = float(score)
if pe >= 0.9 :
    print("A")
elif pe >= 0.8 :
    print("B")
    
# Exercise 4.6
def computepay(a,b):
    '''Computes the hourly pay and accounts for overtime.'''
    if a>40 :
        return (b*40) + ((1.5*b)*(a-40))
    else :
        return a*b

hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
p = computepay(h,r)
print("Pay",p)

# Exercise 5.2
largest = None
smallest = None
while True:
    ent = input("Enter a number: ")
    if ent == "done" :
            break
    try: 
        num = int(ent)
        if smallest is None :
            smallest = num
        if largest is None : 
            largest = num
        if num < smallest :
            smallest = num
        if num > largest :
            largest = num
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)

# Exercise 6.5
text = "X-DSPAM-Confidence:    0.8475"
ab = text.find("0")
ac = text[ab:]
ad = float(ac)
print(ad)

# Exercise 7.2
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total_line = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    line_f = float(line[20:])
    total_line = total_line + line_f
print("Average spam confidence:", total_line / count)

# Exercise 8.4
inp = input("Enter file name:")
romeo = open(inp)
lst = list()
for line in romeo:
    line = line.rstrip()
    words = line.split()
    for word in words :
        if word not in lst :
            lst.append(word)
        else : continue
lst.sort()
print(lst)

# Exercise 8.5
fh = open("mbox-short.txt")
count = 0
for line in fh :
    line = line.rstrip()
    if line.startswith("From:") :
        count = count + 1
        r_line = line.split()
        email = r_line[1]
    else : continue
    print(email)
print("There were", count, "lines in the file with From as the first word")

# Exercise 9.4
mbox_file = open("mbox-short.txt")
counts = dict()

for line in mbox_file : 
    if line.startswith("From:") :
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
    else : continue

freq_email = None
freq_count = None

for email,count in counts.items() :
    if freq_count is None or count > freq_count :
        freq_email = email
        freq_count = count

print(freq_email, freq_count)

# Exercise 10.2
mbox_file = open("mbox-short.txt")
counts = dict()

for line in mbox_file :
    if line.startswith("From ") :
        words = line.split()
        time = words[5]
        hour = time[:2]
        counts[hour] = counts.get(hour, 0) + 1
    else : continue

lst = list()
for hour, count in counts.items() :
    tup = (hour, count)
    lst.append(tup)

lst = sorted(lst)

for hour, count in lst :
    print(hour, count)

# All other assignments are not auto-graded.  
# They are separate in the repository. 
