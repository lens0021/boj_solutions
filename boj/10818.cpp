#include <cstdio>

int main()
{
  int numOfCases;
  scanf("%d", &numOfCases);
  int min, max;
  scanf(" %d", &min);
  max = min;
  while (--numOfCases)
  {
    int num;
    scanf(" %d", &num);
    if (num < min)
    {
      min = num;
    }
    if (num > max)
    {
      max = num;
    }
  }
  printf("%d %d", min, max);
}
