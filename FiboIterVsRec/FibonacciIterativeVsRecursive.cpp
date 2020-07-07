//RECURSIVE
#include<iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;
int fibo(int n)
{
    if(n == 0 || n == 1)
        return n;
    else
        return fibo(n - 2) + fibo(n - 1);
}

int main()
{
    int num = 40;
    auto start = high_resolution_clock::now();
    cout << "Factorial de " << num << " es " << fibo(num) << endl;
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Tiempo "<< duration.count()<< " microseconds" << endl;
    return 0;
}
/*
//ITERATIVE
#include<iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;
// function to find factorial of given number
int fib(int num) {
    int x = 0, y = 1, z = 0;
    for (int i = 0; i < num; i++) {
        z = x + y;
        x = y;
        y = z;
    }
    return y;
}
int main()
{
    long num = 40;
    auto start = high_resolution_clock::now();
    cout << "Factorial " << num << " es " << fib(num) << endl;
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Tiempo: "
         << duration.count()<< " microseconds" << endl;
    return 0;
}*/