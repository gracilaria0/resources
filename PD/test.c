#include <stdio.h>
#include <string.h>

char TOPRINT[200];
#define P(x, T) sprintf(TOPRINT, "%%s\tis\t%%%s\n", #T); printf(TOPRINT, #x, x)

void arrName()
{
	char a[] = "abc";
	char b[] = "abc";
	char *c = "abc";
	char *d = "abc";
	c[0] = 1;
	P(a==b, d);
	P(c==d, d);
	P(strcmp(a, c), d);
}

void constPointer()
{
	// int arr[3] = {1, 2, 3}, brr[3];
	// brr = arr;
	// int a = 2, b = 5;
	// int *const p = &a;
	// p = &b;
	// const int *q = &a;
	// *q = 5;
}

void ddArray()
{
	int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
	P(a, p);
	P(a+1, p);
	P(*a, p);
	P(*a+1, p);
	P(*(a+1), p);
	P(*(a+1)+1, p);
	P(**a, p);
}

int main()
{	
	arrName();
	return 0;
}