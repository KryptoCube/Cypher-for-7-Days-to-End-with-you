a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

userinput = input("")
word = [int(i)-1 for i in userinput.split(" ")]
for j in range(26):
    decipherd = ""
    numbers = str(j)+": "
    for i in word:
        xp = i-j
        if xp >= 26:
            xp %= 26
        if i < j:
            xp -= 1
            numbers += str(i+1)+"("+str(26 if i == 0 else i)+") "
        else:
            numbers += str(i+1)+" "
        decipherd += a[xp]
    print(decipherd+" "+numbers)
