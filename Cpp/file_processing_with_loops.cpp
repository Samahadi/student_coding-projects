/* Student name: Sameer Ahadi
Date Written: 04/02/2026
Class: CSC100AA
Program Purpose: Using file with loops.
*/
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile;
    int num;
    string lastName, firstName;
    int count = 0;
    int sum = 0;

    cout << "This program reads data from a file" << endl;
    cout << "------------------------------" << endl;

    infile.open("testData.txt");

    if (infile.fail())
    {
        cout << "Error opening file." << endl;
    }
    else
    {
        while (infile >> num >> lastName >> firstName)
        {
            cout << "President " << firstName << " " << lastName
                << " had a popularity score of " << num << "." << endl;

            sum = sum + num;
            count = count + 1;
        }

        cout << "There were " << count << " values in the file." << endl;
        cout << "The sum of all the values is " << sum << "." << endl;
    }

    infile.close();

    return 0;
}

/*
Sample Output:
This program reads data from a file
------------------------------
President George Washington had a popularity score of 95.
President John Adams had a popularity score of 97.
President Thomas Jefferson had a popularity score of 98.
President James Madison had a popularity score of 100.
President James Monroe had a popularity score of 93.
There were 5 values in the file.
The sum of all the values is 483.

*/