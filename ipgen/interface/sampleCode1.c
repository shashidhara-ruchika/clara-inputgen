#include<crest.h>
#include <stdio.h>
int largest_num(int n1, int n2, int n3)
{
  if (n1 > n2)
  {
    if (n1 > n3)
      return n1;
    else
      return n3;

  }
  else
  {
    if (n2 > n3)
      return n2;
    else
      return n3;

  }

}

int main()
{
  int a;
  int b;
  int c;
  CREST_unsigned_short(a);
  CREST_unsigned_short(b);
  CREST_unsigned_short(c);
  largest_num(a, b, c);
  return 0;
}

