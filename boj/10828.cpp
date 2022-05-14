#include <iostream>
#include <string>
using namespace std;
#define EMPTY -1

int main(void)
{
  int numOfCmd;
  scanf("%d", &numOfCmd);

  int stack[10000];
  int top = EMPTY;
  do
  {
    string cmd;
    getline(cin, cmd);

    if (!cmd.compare("pop"))
    {
      cout << (top == EMPTY ? -1 : stack[top--]) << endl;
    }
    else if (!cmd.compare("size"))
    {
      cout << top + 1 << endl;
    }
    else if (!cmd.compare("top"))
    {
      cout << (top == EMPTY ? -1 : stack[top]) << endl;
    }
    else if (!cmd.compare("empty"))
    {
      cout << (top == EMPTY ? 1 : 0) << endl;
    }
    else if (!cmd.compare(""))
    {
      continue;
    }
    else // "push" case
    {
      // cout << "trying to push...";
      int space = cmd.find(' ');
      stack[++top] = stoi(cmd.substr(space));
    }
  } while (numOfCmd--);
  return 0;
}
