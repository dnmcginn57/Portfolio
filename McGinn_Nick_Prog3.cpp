//Nick McGinn
//4-5-17
//2433
//This program includes a really bad implimentation of
//	The Sieve of Eratosthenes and then also a pretty okay algorithm


#include<iostream>
#include<iomanip>
#include<ctime>
#include<vector>
#include<cmath>
using namespace std;



//basic Sieve function, accepts a vector passed by reference
void badSieve(vector<int>& toSieve) 
{
	vector<int> primes;
	int curPrime;
	int counter = 0;
	bool needLine = false;
	double t1,t2;
	
	cout << "Bad way\n";
	
	t1 = clock();
	//populates an array to modify
	for(unsigned int i = 0; i < toSieve.size(); i++)
	{
		primes.push_back(toSieve[i]);
	}
	
	//nested for loop locates composite numbers and replaces them with 0's
	for (unsigned int i = 0; i < primes.size(); i++)
	{
		curPrime = primes[i];
		//replaces composite numbers with 0
		if (curPrime != 0) 
		{
			for (unsigned int j = i + curPrime; j < primes.size(); j = j + curPrime)
			{
				primes[j] = 0;
			}//end of inner for loop
		}//end of if statement
		

	}//end of outer for loop

	t2 = clock();




	//prints the primes less than 500
	if (primes.size() < 500) 
	{
		for (unsigned int i = 0; i < primes.size(); i++)
		{
			//ensures no 0's are printed
			if (primes[i] != 0)
			{
				cout << left << setw(5) << primes[i];
				counter++;
				needLine = true;
			}
			if (counter % 5 == 0 && needLine)
			{
				cout << endl;
				needLine = false;
			}
				
		}
		cout << "\n\nthere are " << counter << " primes less than 500\n" <<endl;
	}
	//prints the number of primes found
	else
	{
		for (unsigned int i = 0; i < primes.size(); i++)
		{
			//ensures no 0's are counted
			if (primes[i] != 0)
				counter++;
		}
		cout << "the Sieve found " << counter << " prime numbers\n";
	}
	//prints time taken
	cout << setprecision(4) << "\nFinished in " << (t2 - t1) / CLK_TCK << " seconds\n\n";




}



//Improved Sieve function, accepts a vector passed by reference
void goodSieve(vector<int>& toSieve)
{
	//vector<int> primes;
	int curPrime;
	int counter = 0, sentinel = ceil(sqrt(toSieve[toSieve.size()-1]));
	bool needLine = false;
	double t1, t2;

	cout << "Good Way\n";

	t1 = clock();
	//another improvement, since this is always called second
		//why not just do the thing to the vector that is passed in
		//instead of making a copy? :^)
	
		////populates an array to modify
	//for (unsigned int i = 0; i < toSieve.size(); i++)
	//{
	//	primes.push_back(toSieve[i]);
	//}

	//nested for loop locates composite numbers and replaces them with 0's
	//improvement here, now only checks to the sentinel
	for (int i = 0; i <= sentinel; i++)
	{
		curPrime = toSieve[i];
		//replaces composite numbers with 0
		if (curPrime != 0)
		{
			for (unsigned int j = i + curPrime; j < toSieve.size(); j = j + curPrime)
			{
				toSieve[j] = 0;
			}//end of inner for loop
		}//end of if statement


	}//end of outer for loop

	t2 = clock();




	//prints the primes less than 500
	if (toSieve.size() < 500)
	{
		for (unsigned int i = 0; i < toSieve.size(); i++)
		{
			//ensures no 0's are printed
			if (toSieve[i] != 0)
			{
				cout << left << setw(5) << toSieve[i];
				counter++;
				needLine = true;
			}
			if (counter % 5 == 0 && needLine)
			{
				cout << endl;
				needLine = false;
			}

		}
		cout << "\n\nthere are " << counter << " primes less than 500\n" << endl;
	}
	//prints the number of primes found
	else
	{
		for (unsigned int i = 0; i < toSieve.size(); i++)
		{
			//ensures no 0's are counted
			if (toSieve[i] != 0)
				counter++;
		}
		cout << "the Sieve found " << counter << " prime numbers\n";
	}
	//prints time taken
	cout << setprecision(4) << "\nFinished in " << (t2 - t1) / CLK_TCK << " seconds\n\n";




}

int main() 
{
	vector<int> toSieve;

	for (int i = 2; i <= 500; i++) {
		toSieve.push_back(i);
	}


	//methods executed with 500 numbers
	badSieve(toSieve);
	goodSieve(toSieve);

	toSieve.clear();
	for (int i = 2; i <= 5000; i++) {
		toSieve.push_back(i);
	}

	//methods executed with 5,000
	badSieve(toSieve);
	goodSieve(toSieve);

	toSieve.clear();
	for (int i = 2; i <= 50000; i++) {
		toSieve.push_back(i);
	}
	//methods executed with 50,000
	badSieve(toSieve);
	goodSieve(toSieve);
	
	toSieve.clear();
	for (int i = 2; i <= 100000; i++) {
		toSieve.push_back(i);
	}
	//methods executed with 100,000
	badSieve(toSieve);
	goodSieve(toSieve);



	return 0;
}