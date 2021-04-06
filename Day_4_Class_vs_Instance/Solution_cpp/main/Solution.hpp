using namespace std;

class Person
{
public:
  int age;
  Person(int initialAge);
  void amIOld();
  void yearPasses();
  string amIOldLogic();
};

Person::Person(int initialAge)
{
  // Add some more code to run some checks on initialAge
  if (initialAge < 0)
  {
    cout << "Age is not valid, setting age to 0." << endl;
    this->age = 0;
  }
  else
  {
    this->age = initialAge;
  }
}

string Person::amIOldLogic()
{
  string str = "";
  // Do some computations in here and print out the correct statement to the console
  if (this->age < 0)
  {
    str = "Age is not valid, setting age to 0.";
  }
  else if (this->age < 13)
  {
    str = "You are young.";
  }
  else if (this->age >= 13 && this->age < 18)
  {
    str = "You are a teenager.";
  }
  else
  {
    str = "You are old.";
  }
  return str;
}

void Person::amIOld()
{
  // Do some computations in here and print out the correct statement to the console
  cout << this->amIOldLogic() << endl;
}

void Person::yearPasses()
{
  // Increment the age of the person in here
  ++this->age;
}
