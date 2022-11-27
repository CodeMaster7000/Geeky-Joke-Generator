import pyjokes
import time

print ("10 geeky jokes to have you cracking up: \n")
time.sleep(1.5)
jokes = pyjokes.get_jokes(language='en', category='neutral')
for i in range(10):
    print(i+1,':',jokes[i])
    time.sleep(2)

print("\n")
print("Well? How were they? Share with friends & family!")
