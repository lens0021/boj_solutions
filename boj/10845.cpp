#include <iostream>
#include <string>
using namespace std;

int main(void)
{
  int numOfCmd;
  scanf("%d ", &numOfCmd);

  int queue[10000];
  int front = 0, back = 0;

  string cmd;
  while (numOfCmd--)
  {
    getline(cin, cmd);

    if (!cmd.compare("pop"))
    {
      cout <<(front == back ? -1 : queue[front++]) << endl;
    }
    else if (!cmd.compare("empty"))
    {
      cout << (front == back ? 1 : 0) << endl;
    }
    else if (!cmd.compare("back"))
    {
      cout <<(front == back ? -1 : queue[back - 1]) << endl;
    }
    else if (!cmd.compare("front"))
    {
      cout <<(front == back ? -1 : queue[front]) << endl;
    }
    else if (!cmd.compare("size"))
    {
      cout <<back - front << endl;
    }
    else if (!cmd.compare("print"))
    {
      for (int i = front; i < back; i++)
      {
        cout << i << ':' << queue[i] << ' ';
      }
      cout << endl;
    }
    else // push
    {
      int num = stoi(cmd.substr(cmd.find(' ')));
      queue[back++] = num;
    }
  }

  return 0;
}
