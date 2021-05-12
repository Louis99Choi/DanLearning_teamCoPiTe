S = input()
acnt = 0
dcnt = 0

for i in range(len(S) - 1):
    if S[i] < S[i + 1]:
        acnt += 1
    elif S[i] > S[i + 1]:
        dcnt += 1
if S[0] == S[-1]:
    print(acnt)
else:
    result = acnt if acnt > dcnt else dcnt
    print(result)
