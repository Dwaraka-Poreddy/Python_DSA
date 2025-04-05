code = "QWERTY"
reverse = ""
for i in range(len(code)):
    reverse += code[len(code)-i-1]
    print(code[len(code)-i-1])
    
print(reverse)

code1 = "QWERTYyuiop"
reverse1 = ""
for i in range(len(code1)-1, -1, -1):
    reverse1 += code1[i]
    print(code1[i])
    
print(reverse1)



codey = "QWERTYYTREWQ"
isPalindrome = True
for i in range(len(codey)):
  if  codey[i] != codey[len(codey)-i-1]:
    isPalindrome = False
    break

print(isPalindrome)


codey = "QWERTYYTREWQ"
isPalindrome = True
for i in range(len(codey)//2): # Only need to check half the string using // operator to get the integer division
    # we can alsa use int(codey/2) to get the integer division
  if  codey[i] != codey[len(codey)-i-1]:
    isPalindrome = False
    break

print(isPalindrome)