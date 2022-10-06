def countdown(n):
    while n>-10:
        print(n)
        n=n-1
    print("blastoff")
countdown(10)
def sequence(n):
    while n!=1:
        print(n)
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
sequence(150)