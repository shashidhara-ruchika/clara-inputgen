#include<stdio.h>
int greatest(int a, int b, int c)
{
	if(a>=b)
	{
		if(a>=c)
			return a;
	}
	else if(b>=a)
	{
		if(b>=c)
			return b;
	}
	else if(c>=a)
	{
		if(c>=b)
			return c;
	}
}
//This is a comment
int main()
{
	int a, b, c;
	short d;
	unsigned short e;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	printf("Greatest of 3 is %d\n", greatest(a, b, c)); //This is another comment
	return 0;
}

void foo(int a)
{
}

int bar()
{
	return 0;
}
