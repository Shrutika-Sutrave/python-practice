user = input("Do you want to encrypt or decrypt? Enter E or D: ")
word = input("Enter a word:")
r1 = 'kim'
r2 = 'cod'
if user == 'E':
    if len(word) < 3:
        print(word[::-1])
    else:
        # harry
        # arryh
        print(word[1:] + (word[0]))
        print(r1+word[1:] + (word[0])+r2)

        # kimarryhkim
        # mikhyrramik

if user == 'D':
    if len(word) < 3:
        print(word[::-1])
    else:
        u1=word[::-1]
        u2=u1[3:]
        u3=u2[:-3]
        print(u3[-1]+u3[:-1])
