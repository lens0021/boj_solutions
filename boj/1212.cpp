#include <cstdio>

int main(void)
{
  int num;
  scanf("%o", &num);
  if (num == 0)
  {
    printf("0");
  }
  else
  {
    char str[100], i=0;
    while (num)
    {
      str[i++] = num % 2 ? '1' : '0';
      num /= 2;
    }
    int len = str.length();
    printf("%s", str);
  }
}
