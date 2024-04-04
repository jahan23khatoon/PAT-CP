def find_cow_bull(secret,guess):
    bull_cow=[0,0]
    i=0
    for s in secret:
        if s in guess:
            if secret[i]=guess[i]:
                bull_cow[0]+=1 #0---bull count
            else:
                bull_cow[1]+=1 #1---cow count
            i+=1
        return str(bull_cow[0])+"B"+str(bull_cow[1])+"C"
secret_num=[digit for digit in input("enter secret num:")]
guess_num=[digit for digit in input("enter guess num:")]
ans=find_cow_bull(secret_num,guess_num)
print(ans)
