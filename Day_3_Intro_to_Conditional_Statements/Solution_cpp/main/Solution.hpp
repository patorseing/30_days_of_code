using namespace std;

string solve(int N)
{
    string str = "";
    if (N % 2 == 1)
    {
        str = "Weird";
    }
    else
    {
        if (N > 1 && N < 6)
        {
            str = "Not Weird";
        }
        else if (N > 5 && N < 21)
        {
            str = "Weird";
        }
        else
        {
            str = "Not Weird";
        }
    }
    return str;
}
