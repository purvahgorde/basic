def fibonacci_series(n):
   
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


num_terms = int(input("Enter the number of terms: "))
fibonacci_series(num_terms)
