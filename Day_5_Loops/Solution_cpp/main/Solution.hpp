using namespace std;

string solve (int n, int i) {
  char buffer [50];
  sprintf(buffer, "%d x %d = %d", n, i, n*i);
  return buffer;
}
