/* Student name: Sameer Ahadi
Date Written: 03/29/2026
Class: CSC100AA
Program Purpose: Show me the money.
*/


#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int days, day; // Number of days worked and loop control variable
	double pay, totalPay; // Pay for the current day and total pay accumulated
	char choice; // User's choice to repeat the program

    do
    {
        cout << "How many days did the employee work this month? ";
        cin >> days;

        while (days < 1 || days > 31)
        {
            cout << "The number of days must be between 1 and 31." << endl;
            cout << "Please re-enter days worked. ";
            cin >> days;
        }

		pay = 0.01; // Initial pay for the first day
		totalPay = 0.0; // Initialize total pay to zero

        cout << fixed << setprecision(2);
        cout << "Day\tPay" << endl;
        cout << "------------------" << endl;

        for (day = 1; day <= days; day++)
        {
            cout << day << "\t" << pay << endl;
            totalPay = totalPay + pay;
            pay = pay * 2;
        }

        cout << "------------------" << endl;
        cout << "Total $ " << totalPay << endl;

        cout << "Do you want to try again? (Y or N) ";
		cin >> choice; // Get user's choice to repeat the program

    } while (choice == 'Y' || choice == 'y');

    return 0;
}

/*
Output:
How many days did the employee work this month? 3
Day     Pay
------------------
1       0.01
2       0.02
3       0.04
------------------
Total $ 0.07
Do you want to try again? (Y or N) y
How many days did the employee work this month? 45
The number of days must be between 1 and 31.
Please re-enter days worked. -2
The number of days must be between 1 and 31.
Please re-enter days worked. 3
Day     Pay
------------------
1       0.01
2       0.02
3       0.04
------------------
Total $ 0.07
Do you want to try again? (Y or N)

*/